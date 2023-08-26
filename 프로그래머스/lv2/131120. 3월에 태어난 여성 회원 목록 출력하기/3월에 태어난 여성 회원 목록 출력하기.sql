-- 코드를 입력하세요
SELECT MEMBER_ID, MEMBER_NAME, GENDER, date_format(date_of_birth, '%Y-%m-%d') as date_of_birth
from MEMBER_PROFILE
where TLNO != 'NULL' and date_of_birth like '%-03-%' and gender = 'W'
order by member_id