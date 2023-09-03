-- 코드를 입력하세요
SELECT TRUNCATE(PRICE, -4) as PRICE_GROUP, count(PRODUCT_Id) as PRODUCTS
from product
group by PRICE_GROUP
order by PRICE_GROUP