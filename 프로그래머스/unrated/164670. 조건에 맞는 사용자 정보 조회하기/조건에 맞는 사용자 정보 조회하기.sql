-- 코드를 입력하세요
SELECT u.USER_ID, u.NICKNAME, 
concat(u.CITY,' ',u.STREET_ADDRESS1, ' ', u.STREET_ADDRESS2) as '전체주소', 
concat(SUBSTR(u.TLNO, 1, 3), '-', SUBSTR(u.TLNO,4,4), '-', SUBSTR(u.TLNO, 8)) as '전화번호'
from USED_GOODS_BOARD as b
join USED_GOODS_USER as u on b.WRITER_ID = u.USER_ID
group by WRITER_ID
having COUNT(WRITER_ID) >=3
order by u.USER_ID desc