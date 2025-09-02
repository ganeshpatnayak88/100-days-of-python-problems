-- CREATE DATABASE WIPRO;

-- USE WIPRO;

-- CREATE TABLE EMPLOYES(EMPY_ID INT,EMPY_NAME VARCHAR(200),EMPY_DEPT VARCHAR(80));

-- DESC EMPLOYES;

-- INSERT INTO EMPLOYES VALUES(1,'SAI','TESTER'),(2,'TARUN','DEV'),(3,'DRUVA','SAP');

-- SELECT * FROM EMPLOYES;

-- CREATE TABLE WORKERS(EMPY_ID INT,EMPY_P_NO INT,EMPY_VILLAGE VARCHAR(30));

-- INSERT INTO WORKERS VALUES(1,8888888,'HYD'),(2,66666666,'BBL'),(3,999999999,'JK'),(4,7777777,'VZM');

-- DESC WORKERS;

-- SELECT * FROM WORKERS;

-- SELECT * FROM EMPLOYES INNER JOIN  WORKERS ON EMPLOYES.EMPY_ID=WORK-- ERS.EMPY_ID;

-- SELECT * FROM EMPLOYES LEFT JOIN WORKERS ON EMPLOYES.EMPY_ID=WORKERS.EMPY_ID;

-- SELECT * FROM EMPLOYES RIGHT JOIN WORKERS ON EMPLOYES.EMPY_ID=WORKERS.EMPY_ID;

-- SELECT * FROM EMPLOYES LEFT JOIN WORKERS ON EMPLOYES.EMPY_ID=WORKERS.EMPY_ID UNION
-- SELECT * FROM EMPLOYES RIGHT JOIN WORKERS ON EMPLOYES.EMPY_ID=WORKERS.EMPY_ID;

-- SELECT * FROM EMPLOYES CROSS JOIN WORKERS;

-- SELECT * FROM EMPLOYES JOIN WORKERS ON EMPLOYES.EMPY_ID=WORKERS.EMPY_ID;

-- CREATE TABLE FRESHERS(EMPY_ID INT,EMPY_CN VARCHAR(30));

-- DESC FRESHERS;

-- INSERT INTO FRESHERS VALUES(1,'BRAU'),(2,'RAGHU'),(3,'VZM');

-- SELECT * FROM EMPLOYES INNER JOIN WORKERS ON EMPLOYES.EMPY_ID=WORKERS.EMPY_ID INNER JOIN FRESHERS ON WORKERS.EMPY_ID=FRESHERS.EMPY_ID;


-- create database image101;
-- use image101;
-- create table images1001(imag_id int,imag_name longblob);

-- insert into images1001 values(101,load_file('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\20241129_121904(1).jpg'));

-- select * from images1001;


-- create database tcl_51r;
-- use tcl_51r;
-- create table emps(emp_id int,emp_name varchar(30),emp_salary int);

-- desc emps;
-- insert into emps values(1,'hari',23000),(2,'rahul',30000),(3,'tarun',35000);
-- set sql_safe_updates=0;
-- select * from emps;

-- update emps set emp_salary=45000 where emp_name='hari';

-- delete from emps;

-- start transaction;

-- rollback;
-- commit;

-- truncate table emps;


create database u;
use u;
create table brau(id int,name varchar(30),teacher_name char(40),branch varchar(25));
insert into brau values(1,'kiran','sravani','ece'),(2,'tarun','haritha','ece'),(3,'sridhar','ganesh','cse'),(4,'lokesh','radha','mec'),(5,'king','nagendra','mec'),(6,'teja','aruna','ece'),(7,'ravi','sravani','ece'),(8,'teja','ganesh','cse');
select * from brau;

alter table brau add column marks int;
set sql_safe_updates=0;
update brau set marks=case when id=1 then 89 when id=2 then 90 when id=3 then 78 when id=4 then 50 when id=5 then 85 when id=6 then 88 when id=7 then 87 when id=8 then 97 end where id in (1,2,3,4,5,6,7,8);

select * from brau where marks=(select max(marks) from brau where marks<(select max(marks) from brau where marks<(select max(marks) from brau)));

alter table brau add column place varchar(30);

update brau set place=case when id=1 then 'hyd' when id=2 then 'pune' when id=3 then 'jammu' when id=4 then 'delhi' when id=5 then 'chennai' when id=6 then 'vizag' when id=7 then 'howra' when id=8 then 'gujarat' end where id in (1,2,3,4,5,6,7,8);

create table student_details(id int,location varchar(30),cgpa float);

insert into student_details values(1,'bbl',7.0),(2,'sklm',8.0),(3,'palasa',7.9),(4,'vizag',9.0),(5,'guntur',8.8),(5,'vzm',8.5),(6,'tirupathi',6.5),(7,'rajam',7.9),(8,'tuni',8.1);
select * from student_details;

use u;
show tables;
alter table student_details change location place varchar(25);

alter table student_details modify place char(30);

desc student_details;
insert into student_details values(8,'karimnagar',7.8);

delete from student_details where id=8;

select * from brau;
start transaction;

insert into brau values(9,'sudheer','haritha','ece',96,'vizag');
savepoint hcl;

insert into brau values(10,'yugi','haritha','ece',100,'vizag');
savepoint tcs;
commit;

rollback to tcs;

start transaction;


select * from brau where marks>(select avg(marks) from brau);

select * from brau where branch='mec';

select * from student_details;

update brau set name='ganesh' where id=4;

select * from brau where marks=(select max(marks) from brau where marks<(select max(marks) from brau where marks< (select max(marks) from brau)));

SELECT *
FROM brau
WHERE marks > (SELECT marks FROM brau WHERE name = 'king')
  AND marks < (SELECT marks FROM brau WHERE name = 'sudheer');
  
  
use u;
select * from brau;