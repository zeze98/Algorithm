-- 코드를 입력하세요
SELECT HOUR(DATETIME) as HOUR, COUNT(DATETIME) as 'COUNT'
from ANIMAL_OUTS
group by hour
having 9 <= hour and hour <=19
order by hour