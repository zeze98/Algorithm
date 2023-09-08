-- 코드를 입력하세요
SELECT YEAR(o.SALES_DATE) as YEAR, MONTH(o.SALES_DATE) as MONTH, u.GENDER, 
count(DISTINCT u.USER_ID) as USERS
from USER_INFO as u
join ONLINE_SALE as o on u.USER_ID = o.USER_ID
where gender is not null
group by YEAR, MONTH, GENDER
order by YEAR, MONTH, GENDER

