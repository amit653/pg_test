from prometheus_client import start_http_server, Gauge
import psycopg2
print(psycopg2.__version__)
import time

# --- PostgreSQL connection configuration ---
DB_CONFIG = {
    'dbname': 'test',
    'user': 'postgres',
    'password': 'postgres',
    'host': '192.168.29.225',
    'port': 5432
}
# prom. gauge
custom_lock = Gauge("postgres_blocked_sessions","number of block sessions")
def collect_metrics():
  #pass
  with psycopg2.connect(**DB_CONFIG) as conn:
    #pass
    with conn.cursor() as cur:
      cur.execute("SELECT count(blocking.pid) FROM pg_stat_activity AS activity JOIN " \
      "pg_stat_activity AS blocking ON blocking.pid = ANY(pg_blocking_pids(activity.pid)) ")
      custom_lock.set(cur.fetchone()[0])
       
if __name__== '__main__':
  start_http_server(8000) # Prometheus will scrape this port
  print("Exporter started on http://localhost:8000")
  while (True):
    try:
      collect_metrics() 
    except Exception as e:
      print(f'Error collecting metrics {e}')
    time.sleep(15) # scrape  interval after every 15 secs
    #pass

    

