-- 코드를 입력하세요
SELECT ANIMAL_TYPE, count(ANIMAL_ID) as 'count'
from ANIMAL_INS
where animal_type = 'Cat' or animal_type = 'Dog'
group by animal_type
order by 1
