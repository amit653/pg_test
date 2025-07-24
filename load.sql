--drop table tab;
--drop table no_vac1;
--create table tab (id int);
--insert into tab(id)  select * from generate_series(1,4000);

--create table no_vac1( id int);
--alter table no_vac1 set(autovacuum_enabled=off);
--insert into no_vac1(id)  select  * from generate_series(1,400);
drop table amit; 
create table amit(id int);
do $$
begin 
       	for i in 1..30 loop
       	insert into amit  select  from generate_series(1,8000) ;update amit set id=1000; 
        end loop;
end
$$ language plpgsql;
select relname,now(),last_autovacuum ,n_Dead_tup from pg_stat_user_tables ;
	begin; --set local statement_timeout='60s'; 
		--set idle_in_transaction_session_timeout='60s'
		select pg_backend_pid() as blocking_pid; ALTER TABLE amit  RENAME COLUMN  id TO id8;
select pg_sleep(1000);
