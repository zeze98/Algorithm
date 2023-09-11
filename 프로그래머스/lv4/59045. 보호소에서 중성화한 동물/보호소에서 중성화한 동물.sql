-- 코드를 입력하세요
SELECT o.ANIMAL_ID, o.ANIMAL_TYPE, o.NAME
from ANIMAL_OUTS as o
join ANIMAL_INS as i
where o.ANIMAL_ID = i.ANIMAL_ID and i.SEX_UPON_INTAKE != o.SEX_UPON_OUTCOME
order by o.ANIMAL_ID

