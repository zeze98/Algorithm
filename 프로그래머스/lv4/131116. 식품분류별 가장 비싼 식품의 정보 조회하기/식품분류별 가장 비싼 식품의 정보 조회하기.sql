-- 코드를 입력하세요
SELECT CATEGORY, PRICE as MAX_PRICE, PRODUCT_NAME
from FOOD_PRODUCT
where PRICE in (select max(price) from FOOD_PRODUCT GROUP BY CATEGORY)
and CATEGORY in ('과자', '국', '김치', '식용유')
order by MAX_PRICE desc