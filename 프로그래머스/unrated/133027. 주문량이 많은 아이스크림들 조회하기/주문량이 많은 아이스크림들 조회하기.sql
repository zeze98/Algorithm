-- 코드를 입력하세요
SELECT f.FLAVOR
from FIRST_HALF as f
join (select FLAVOR, sum(TOTAL_ORDER) as TOTAL_ORDER 
      from july 
      GROUP BY FLAVOR) as j
on f.FLAVOR = j.FLAVOR
order by (f.TOTAL_ORDER + j.TOTAL_ORDER) desc
limit 3