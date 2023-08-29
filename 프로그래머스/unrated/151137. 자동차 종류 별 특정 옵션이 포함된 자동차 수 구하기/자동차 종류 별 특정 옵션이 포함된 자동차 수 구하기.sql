-- 코드를 입력하세요
SELECT car_type, count(car_type) as CARS
from CAR_RENTAL_COMPANY_CAR
WHERE OPTIONS LIKE '%시트%'
group by car_type
ORDER BY CAR_TYPE
