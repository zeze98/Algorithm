-- 코드를 입력하세요
SELECT a.BOARD_ID, a.WRITER_ID, a.TITLE, a.PRICE, 
case when a.STATUS = 'SALE' THEN '판매중'
when a.STATUS = 'RESERVED' THEN '예약중'
when a.STATUS = 'DONE' THEN '거래완료'
end as 'STATUS'
from USED_GOODS_BOARD as a
where date_format(a.CREATED_DATE, '%Y-%m-%d') = '2022-10-05'
order by a.BOARD_ID desc