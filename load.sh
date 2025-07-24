#!/bin/bash

# Database credentials
HOST="localhost"
PORT="5432"
DB_NAME="test"
USER="postgres"
PASSWORD="postgres"

# SQL DDL script path
DDL_SCRIPT="load.sql"

# Export password so psql doesn't prompt
export PGPASSWORD=$PASSWORD

# Execute DDL
psql -h "$HOST" -p "$PORT" -U "$USER" -d "$DB_NAME" -f "$DDL_SCRIPT"

# Unset password after execution
unset PGPASSWORD

