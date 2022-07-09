#_-_encoding=utf8_-_
#__author__="huiseong.song"
import pymysql

bookdb = pymysql.connect(user="root", passwd="gozldtlqkf!23", host="localhost", db="guest_book", charset="utf8") # sql 실행
cur = bookdb.cursor() # 커서 생성

def writing(insert_data): # 글 쓰기 함수
    
    
    get_no = "SELECT no FROM written" # DB에 저장된 마지막 글의 글 넘버를 불러와서 저장
    
    no = cur.execute(get_no)+1 # 불러온 글 넘버 +1
    
    insert_data.insert(0, no) # insert_data 리스트 0번째에 no값 삽입
 
    insert_sql = "INSERT INTO written VALUES(%s, %s, %s, %s);" # SQL문 실행
    
    cur.execute(insert_sql, insert_data) # %s에 insert_data 리스트 값 순서대로 삽입
    
    bookdb.commit() # bookdb에 삽입한 데이터 커밋
    # bookdb.close() # bookdb close

def load(account):
    
    # select문 저장 변수 생성후 저장
    load_sql = "SELECT * FROM written WHERE name = %s AND password = %s"
    
    # 전달 받은 이름과 암호 값을 대입해 SELECT문 실행
    cur.execute(load_sql, account)
    
    # SELECT문 실행 후 결과값을 result에 저장
    result = cur.fetchall()
    
    if not result:
        # result 값이 빈 값일 경우 메세지 출력
        print("입력하신 정보에 해당하는 데이터가 없습니다.")
    else:
        # result 값이 빈 값이 아닐 경우 result 값 반환
        return result
    
