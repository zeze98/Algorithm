-- 코드를 입력하세요
SELECT a.AUTHOR_ID, a.AUTHOR_NAME, b.CATEGORY, 
sum(s.sales * b.price) as SALES
from BOOK as b
left join AUTHOR as a on b.AUTHOR_ID = a.AUTHOR_ID
left join BOOK_SALES as s on b.BOOK_ID = s.BOOK_ID
where s.SALES_DATE like '2022-01%'
group by b.AUTHOR_ID, b.CATEGORY
order by b.AUTHOR_ID, b.CATEGORY desc