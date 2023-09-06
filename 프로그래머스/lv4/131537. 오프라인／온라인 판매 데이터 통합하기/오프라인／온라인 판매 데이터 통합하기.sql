-- 코드를 입력하세요
(SELECT date_format(SALES_DATE,'%Y-%m-%d') as SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
from ONLINE_SALE as onl
where SALES_DATE like '2022-03%')
union
(select date_format(SALES_DATE,'%Y-%m-%d') as SALES_DATE, PRODUCT_ID, NULL as USER_ID, SALES_AMOUNT
 FROM OFFLINE_SALE as off
 where SALES_DATE like '2022-03%')
 order by SALES_DATE, PRODUCT_ID, USER_ID