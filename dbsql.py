import pymysql

bookdb = pymysql.connect(user="root", passwd="gozldtlqkf!23", host="localhost", db="guest_book", charset="utf8") # sql 실행
cur = bookdb.cursor() # 커서 생성

def writing(insert_data): # 글 쓰기 함수
    
    
    get_no = "select no from written" # DB에 저장된 마지막 글의 글 넘버를 불러와서 저장
    no = cur.execute(get_no)+1 # 불러온 글 넘버 +1
    insert_data.insert(0, no) # insert_data 리스트 0번째에 no값 삽입
    
    
    insert_sql = "INSERT INTO written VALUES(%s, %s, %s, %s);" # SQL문 실행
    cur.execute(insert_sql, insert_data) # 커서 close
    
    bookdb.commit() # bookdb에 삽입한 데이터 커밋
    bookdb.close() # bookdb close
