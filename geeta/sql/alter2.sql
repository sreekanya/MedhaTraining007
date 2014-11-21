update appointment SET
   FirstName = '' -- varchar(20)
  ,LastName = '' -- varchar(20)
  ,`Date` = '' -- varchar(10)
  ,`time` = '' -- varchar(10)
  ,comments = '' -- varchar(50)
  ,Accno = 0 -- int(11)
  where time='10:30am'
update appointment SET
   FirstName = '' -- varchar(20)
  ,LastName = '' -- varchar(20)
  ,`Date` = '' -- varchar(10)
  ,`time` = '' -- varchar(10)
  ,comments = '' -- varchar(50)
  ,Accno = 0 -- int(11)
  where time=('10:30am')
update appointment SET
   FirstName = '' -- varchar(20)
  ,LastName = '' -- varchar(20)
  ,`Date` = '' -- varchar(10)
  ,`time` = '' -- varchar(10)
  ,comments = '' -- varchar(50)
  ,Accno = 0 -- int(11)
  where time='10:30am'
select time from appointment
update appointment SET
   FirstName = 'Himangi' -- varchar(20)
  ,LastName = 'Sathe' -- varchar(20)
  ,`Date` = '05/26' -- vrchar(10)
  ,`time` = '10:00' -- varchar(10)
  ,comments = 'Headache' -- varchar(50)
  ,Accno = 2222-- int(11)
  where FirstName=('Himangi')
update appointment SET
   FirstName = 'Geeta' -- varchar(20)
  ,LastName = 'Patil' -- varchar(20)
  ,`Date` = '05/25' -- vrchar(10)
  ,`time` = '9:30' -- varchar(10)
  ,comments = 'general checkup' -- varchar(50)
  ,Accno = 1111-- int(11)
  where time=('9:30')update appointment SET
   FirstName = '' -- varchar(20)
  ,LastName = '' -- varchar(20)
  ,`Date` = '' -- varchar(10)
  ,`time` = '9:30' -- varchar(10)
  ,comments = '' -- varchar(50)
  ,Accno = 0 -- int(11)
  where FirstName=('Geeta')
insert into appointment (
   FirstName
  ,LastName
  ,`Date`
  ,`time`
  ,comments
  ,Accno
) VALUES (
   ''  -- FirstName - IN varchar(20)
  ,''  -- LastName - IN varchar(20)
  ,''  -- Date - IN varchar(10)
  ,'9:30am'  -- time - IN varchar(10)
  ,''  -- comments - IN varchar(50)
  ,0   -- Accno - IN int(11)
)
alter TABLE appointment DROP COLUMN slot4
alter TABLE appointment DROP COLUMN slot3
ALTER TABLE test.appointment
 DROP slot1,
 DROP slot2

