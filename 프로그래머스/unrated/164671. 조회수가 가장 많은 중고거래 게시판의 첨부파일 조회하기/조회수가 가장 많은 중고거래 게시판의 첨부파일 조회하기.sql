-- 코드를 입력하세요
SELECT CONCAT('/home/grep/src/',f.BOARD_ID,'/', FILE_ID, FILE_NAME, FILE_EXT) as FILE_PATH
from USED_GOODS_FILE as f
where f.BOARD_ID = (select BOARD_ID 
                    from USED_GOODS_BOARD as b 
                    order by b.VIEWS desc 
                    limit 1)
order by FILE_ID desc