 show databases;
+--------------------+
| Database           |
+--------------------+
| 51_rclass          |
| 51class            |
| 51r                |
| bhajans            |
| hari               |
| information_schema |
| lemonroom          |
| mine               |
| mydatabase         |
| mysql              |
| performance_schema |
| sai                |
| siva               |
| sys                |
| wipro              |
+--------------------+
 use 51class;
Database changed
mysql> show tables
    -> ;
+-------------------+
| Tables_in_51class |
+-------------------+
| emps              |
+-------------------+
1 row in set (0.00 sec)

mysql> select * from emps;
+------+---------+--------+
| s_no | names   | salary |
+------+---------+--------+
|    1 | frank   |  62000 |
|    2 | ganesh  |  67000 |
|    3 | hemanth |  68000 |
+------+---------+--------+
delete from emps where names='frank';
Query OK, 1 row affected (0.01 sec)

mysql> select * from emps;
+------+---------+--------+
| s_no | names   | salary |
+------+---------+--------+
|    2 | ganesh  |  67000 |
|    3 | hemanth |  68000 |
+------+---------+--------+
2 rows in set (0.00 sec)

insert into emps(s_no,names,salary) values(1,"frank",52000);
Query OK, 1 row affected (0.01 sec)

mysql> select * from emps;
+------+---------+--------+
| s_no | names   | salary |
+------+---------+--------+
|    2 | ganesh  |  67000 |
|    3 | hemanth |  68000 |
|    1 | frank   |  52000 |
+------+---------+--------+
3 rows in set (0.00 sec)

mysql> select * from emps order by s_no asc;
+------+---------+--------+
| s_no | names   | salary |
+------+---------+--------+
|    1 | frank   |  52000 |
|    2 | ganesh  |  67000 |
|    3 | hemanth |  68000 |
+------+---------+--------+
alter table emps add primary key(s_no);
Query OK, 0 rows affected (0.12 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> alter table emps drop primary key;
Query OK, 3 rows affected (0.10 sec)
Records: 3  Duplicates: 0  Warnings: 0

alter table emps add unique(s_no);
Query OK, 0 rows affected (0.12 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> desc emps;
+--------+----------+------+-----+---------+-------+
| Field  | Type     | Null | Key | Default | Extra |
+--------+----------+------+-----+---------+-------+
| s_no   | int      | NO   | PRI | NULL    |       |
| names  | char(20) | YES  |     | NULL    |       |
| salary | int      | YES  |     | NULL    |       |
+--------+----------+------+-----+---------+-------+
3 rows in set (0.00 sec)
alter table emps add department char(20);
Query OK, 0 rows affected (0.04 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> select * from emps;
+------+---------+--------+------------+
| s_no | names   | salary | department |
+------+---------+--------+------------+
|    1 | frank   |  52000 | NULL       |
|    2 | ganesh  |  67000 | NULL       |
|    3 | hemanth |  68000 | NULL       |
+------+---------+--------+-----------
update emps set department=case when s_no=1 then 'hr' when s_no=2 then 'sales' when s_no=3 then 'it' end where s_no in (1,2,3);
Query OK, 3 rows affected (0.01 sec)
Rows matched: 3  Changed: 3  Warnings: 0

mysql> select * from emps;
+------+---------+--------+------------+
| s_no | names   | salary | department |
+------+---------+--------+------------+
|    1 | frank   |  52000 | hr         |
|    2 | ganesh  |  67000 | sales      |
|    3 | hemanth |  68000 | it         |
+------+---------+--------+------------+
3 rows in set (0.00 sec)

select sum(salary) from emps;
+-------------+
| sum(salary) |
+-------------+
|      187000 |
+-------------+
1 row in set (0.01 sec)

mysql> select avg(salary) from emps;
+-------------+
| avg(salary) |
+-------------+
|  62333.3333 |
+-------------+
1 row in set (0.00 sec)

mysql> select * from emps where salary between 50000 and 60000;
+------+-------+--------+------------+
| s_no | names | salary | department |
+------+-------+--------+------------+
|    1 | frank |  52000 | hr         |
+------+-------+--------+------------+
1 row in set (0.04 sec)

 select * from emps where names like 'g%';
+------+--------+--------+------------+
| s_no | names  | salary | department |
+------+--------+--------+------------+
|    2 | ganesh |  67000 | sales      |
+------+--------+--------+------------+
1 row in set (0.00 sec)

mysql> select * from emps where names like '%h';
+------+---------+--------+------------+
| s_no | names   | salary | department |
+------+---------+--------+------------+
|    2 | ganesh  |  67000 | sales      |
|    3 | hemanth |  68000 | it         |
+------+---------+--------+------------+
2 rows in set (0.00 sec)

mysql> select max(salary) from emps;
+-------------+
| max(salary) |
+-------------+
|       68000 |
+-------------+
1 row in set (0.00 sec)

mysql> select count(department) from emps where department='it';
+-------------------+
| count(department) |
+-------------------+
|                 1 |
+-------------------+
1 row in set (0.00 sec)

alter table emps modify s_no int not null;
Query OK, 0 rows affected (0.02 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> desc emps;
+------------+----------+------+-----+---------+-------+
| Field      | Type     | Null | Key | Default | Extra |
+------------+----------+------+-----+---------+-------+
| s_no       | int      | NO   | PRI | NULL    |       |
| names      | char(20) | YES  |     | NULL    |       |
| salary     | int      | YES  |     | NULL    |       |
| department | char(20) | YES  |     | NULL    |       |
+------------+----------+------+-----+---------+-------+
4 rows in set (0.00 sec)

mysql> select * from emps order by salary asc;
+------+---------+--------+------------+
| s_no | names   | salary | department |
+------+---------+--------+------------+
|    1 | frank   |  52000 | hr         |
|    2 | ganesh  |  67000 | sales      |
|    3 | hemanth |  68000 | it         |
+------+---------+--------+------------+
3 rows in set (0.00 sec)

