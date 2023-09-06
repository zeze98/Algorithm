-- 코드를 입력하세요
SELECT ri.REST_ID, ri.REST_NAME, ri.FOOD_TYPE, ri.FAVORITES, ri.ADDRESS,
round(avg(rr.REVIEW_SCORE),2) as SCORE
from REST_INFO as ri
join REST_REVIEW as rr
on ri.REST_ID = rr.REST_ID
where ADDRESS like '서울%'
group by ri.REST_ID
order by SCORE desc, ri.FAVORITES desc
