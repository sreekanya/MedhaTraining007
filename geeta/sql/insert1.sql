insert into profile1 (
   FirstName
  ,LastName
  ,DOB
  ,contact
  ,Adress
  ,insurance
  ,emergencycontact
  ,slot
  ,slot1
) SELECT 
   ''  AS FirstName               -- FirstName - IN varchar(25)
  ,''  AS LastName                -- LastName - IN varchar(30)
  ,''  AS DOB                     -- DOB - IN varchar(10)
  ,''  AS contact                 -- contact - IN varchar(10)
  ,''  AS Adress                  -- Adress - IN varchar(100)
  ,''  AS insurance               -- insurance - IN varchar(50)
  ,''  AS emergencycontact        -- emergencycontact - IN varchar(10)
  ,0   AS slot                    -- slot - IN int(10)
  ,0   AS slot1                   -- slot1 - IN int(10)
FROM