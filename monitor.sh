#!/bin/bash

# Database credentials
HOST="localhost"
PORT="5432"
DB_NAME="test"
USER="postgres"
PASSWORD="postgres"

# SQL DDL script path
monitor_query="monitor.sql"

# Export password so psql doesn't prompt
export PGPASSWORD=$PASSWORD

# Execute DDL
result=`psql -t -h "$HOST" -p "$PORT" -U "$USER" -d "$DB_NAME" -f "$monitor_query"`
echo $HOME ${#HOME}
echo $result ${#result}
final="$(echo "$result" | awk '{$1=$1;print}')"
echo $HOME/docker/backup/$final
sudo tail -50f $HOME/docker/backup/$final
 
# Unset password after execution
unset PGPASSWORD

