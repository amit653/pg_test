select trim(pg_current_logfile()) from pg_settings where name='data_directory';

