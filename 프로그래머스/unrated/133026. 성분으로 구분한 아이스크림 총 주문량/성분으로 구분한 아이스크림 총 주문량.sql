-- 코드를 입력하세요
SELECT ii.INGREDIENT_TYPE, sum(fh.total_order) as TOTAL_ORDER
from icecream_info as ii, first_half as fh
where ii.flavor = fh.flavor
group by ii.INGREDIENT_TYPE
order by fh.TOTAL_ORDER 

