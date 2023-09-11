-- 코드를 입력하세요
SELECT p.PRODUCT_ID, p.PRODUCT_NAME, sum(o.AMOUNT * p.PRICE) as TOTAL_SALES
from FOOD_PRODUCT as p
right join FOOD_ORDER as o on p.PRODUCT_ID = o.PRODUCT_ID
where o.PRODUCE_DATE like '2022-05%'
group by p.PRODUCT_ID
order by TOTAL_SALES desc, p.PRODUCT_ID

