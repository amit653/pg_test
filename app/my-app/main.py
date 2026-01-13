from prometheus_client import start_http_server, Gauge
import psycopg2
from datetime import datetime
#print(psycopg2.__version__)
import time

# --- PostgreSQL connection configuration ---
DB_CONFIG = {
    'dbname': 'test',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'postgres-server',
    #'host': 'pg_test-postgres-1',
    #'host': 'x.x.xx.xx',
    'port': 5432,
    'connect_timeout': 5  # Tell psycopg2 to wait up to 5s per attempt
}
# prom. gauge
custom_lock = Gauge("postgres_blocked_sessions","number of block sessions")
def get_db_connection():
    """Attempts to connect to Postgres with a retry loop for startup."""
    while True:
        try:
            conn = psycopg2.connect(**DB_CONFIG)
            return conn
        except psycopg2.OperationalError as e:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Postgres not ready yet. Retrying in 2s...")
            time.sleep(2)

def collect_metrics():
    """Connects, fetches the lock count, and updates the Gauge."""
    conn = None
    try:
        conn = get_db_connection()
        with conn.cursor() as cur:
            # Optimized query for blocked sessions
            query = """
                SELECT count(blocking.pid) 
                FROM pg_stat_activity AS activity 
                JOIN pg_stat_activity AS blocking 
                  ON blocking.pid = ANY(pg_blocking_pids(activity.pid))
            """
            cur.execute(query)
            count = cur.fetchone()[0]
            custom_lock.set(count)
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Metrics updated: {count} blocked sessions.")
    except Exception as e:
        print(f"Error during query execution: {e}")
    finally:
        if conn:
            conn.close()
       
if __name__== '__main__':
  print(f"Psycopg2 version: {psycopg2.__version__}")
  now = datetime.now()
  time_str = now.strftime('"%H:%M:%S"')
  start_http_server(8000) # Prometheus will scrape this port
  #print("Exporter started on http://localhost:8000")
  print(f"Exporter start time {time_str}  on http://localhost:8000")
  
  while (True):
    try:
      collect_metrics() 
    except Exception as e:
      print(f'Error collecting metrics {e}')
    time.sleep(15) # scrape  interval after every 15 secs
    #pass

    

