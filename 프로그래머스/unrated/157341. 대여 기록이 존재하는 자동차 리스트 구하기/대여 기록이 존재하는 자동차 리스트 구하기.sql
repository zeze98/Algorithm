-- 코드를 입력하세요
SELECT DISTINCT(h.CAR_ID)
from CAR_RENTAL_COMPANY_RENTAL_HISTORY as h
join CAR_RENTAL_COMPANY_CAR as c on h.CAR_ID = c.CAR_ID
where c.CAR_TYPE = '세단' and h.START_DATE like '2022-10%'
order by CAR_ID desc;