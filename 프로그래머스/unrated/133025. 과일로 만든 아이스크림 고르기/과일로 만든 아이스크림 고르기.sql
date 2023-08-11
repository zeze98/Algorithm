-- 코드를 입력하세요
SELECT f.FLAVOR
from FIRST_HALF as f
LEFT JOIN ICECREAM_INFO as i
on f.FLAVOR = i.FLAVOR
where f.TOTAL_ORDER > 3000 and i.INGREDIENT_TYPE like 'fruit_based'
order by TOTAL_ORDER DESC;