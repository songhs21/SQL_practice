#_-_encoding=utf8_-_
#__author__="huiseong.song"
from tkinter import *
# import pymysql
import dbsql

root = Tk() # Tkinter 생성
root.title("방명록 시스템") # 타이틀 설정
root.geometry("640x400") # 창 크기 설정
root.resizable(False, False) # 창 크기 변경 가능 여부 설정



########################################################################################


frame1 = Frame(root) # 프레임 생성
frame1.pack(side="left", fill="both", expand=True) # 프레임 표시

#이름
Label(frame1, text="이름").pack() # "이름" 라벨 생성 후 pack
name = Entry(frame1, width=30) # 라벨을 frame1에 Entry 후 name에 저장
name.pack() # 라벨 pack

#비밀번호
Label(frame1, text="비밀번호").pack() # "비밀번호" 라벨 생성 pack
psw = Entry(frame1, width=30) #  라벨을 frame1에 Entry 후 psw에 저장
psw.pack() # 라벨 pack

# 내용
Label(frame1, text="내용").pack() # "내용" 라벨 생성 후 pack
wrt = Text(frame1, width=80, height=22) # wrt에 Text 필드 생성후 저장
wrt.pack() # 텍스트 필드 pack
########################################################################################


########################################################################################
def write(): # 글 작성 함수
    insert_data = [name.get(), psw.get(), wrt.get("1.0", END)] # insert_data에 name 텍스트 필드, psw 텍스트 필드, wrt의 텍스트 필드 값을 리스트로 저장
    
    dbsql.writing(insert_data) # sql 함수에 insert_data 값을 보내 writing 실행
    
    name.delete(0, END) # dbsql.writing 실행 후 name 텍스트 필드 내용 삭제
    psw.delete(0, END) # dbsql.writing 실행 후 psw 텍스트 필드 내용 삭제
    wrt.delete("1.0", END) # dbsql.writing 실행 후 wrt 텍스트 필드 내용 삭제
    

def find_written(): # 작성한 글 찾기 함수
    pass # 미작성
########################################################################################


########################################################################################
frame2 = Frame(root)
frame2.pack(side="right", fill="both", expand=True)

# 작성 글 찾기
Button(frame2, text="작성 글\n 찾기", command=show_written).pack(fill="both", expand=True)
# 글 작성
Button(frame2, text="작성", height=20, command=write).pack(fill="both", expand=True)
########################################################################################

root.mainloop()
