-- 코드를 입력하세요
SELECT m.MEMBER_NAME, r.REVIEW_TEXT, date_format(r.REVIEW_DATE, '%Y-%m-%d') as REVIEW_DATE
from MEMBER_PROFILE as m
right join REST_REVIEW as r on m.MEMBER_ID = r.MEMBER_ID
where r.MEMBER_ID = (select MEMBER_ID
       from REST_REVIEW
       group by MEMBER_ID 
       order by COUNT(MEMBER_ID) desc
       limit 1)
order by REVIEW_DATE, r.REVIEW_TEXT