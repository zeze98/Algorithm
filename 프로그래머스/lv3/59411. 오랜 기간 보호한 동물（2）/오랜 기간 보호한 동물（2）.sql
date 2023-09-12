-- 코드를 입력하세요
SELECT o.ANIMAL_ID, o.NAME
from ANIMAL_INS as i
join ANIMAL_OUTS as o on i.ANIMAL_ID = o.ANIMAL_ID
order by datediff(o.DATETIME, i.DATETIME) desc
limit 2