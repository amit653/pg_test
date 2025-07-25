## Added custom_exporter to pull user defined metrics from app/main.py ##
```
edit prometheus.yml and use your docker ip <>in custom_exporter
 - job_name: 'custom_postgres_exporter'
    static_configs:
      - targets: ["docker-ip:8000"]
for example
docker0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        inet <docker-ip> 

mkdir grafana and add  user:"1000" in grafana service i.e id -u from non root user
OR as non root user mkdir grafana && chmod -R 777 grafana

sudo docker-compose up -d --force-recreate --build
sudo docker-compose ps
           Name                         Command               State                    Ports                  
--------------------------------------------------------------------------------------------------------------
docker_grafana_1             /run.sh                          Up      0.0.0.0:3000->3000/tcp,:::3000->3000/tcp
docker_postgres-exporter_1   /bin/postgres_exporter           Up      0.0.0.0:9187->9187/tcp,:::9187->9187/tcp
docker_postgres_1            docker-entrypoint.sh postgres    Up      0.0.0.0:5432->5432/tcp,:::5432->5432/tcp
docker_prometheus_1          /bin/prometheus --config.f ...   Up      0.0.0.0:9090->9090/tcp,:::9090->9090/tcp
python-server                python main.py                   Up      0.0.0.0:8000->8000/tcp,:::8000->8000/tcp

verify the custom metrics in http://0.0.0.0:8000/metrics and target in prometheus http://0.0.0.0:9090/targets
Generare locking using load.sh , verify the autovaccum Dashboard in Grafana http://0.0.0.0:3000/login
```
