#_-_encoding=utf8_-_
#__author__="huiseong.song"
from tkinter import *
import dbsql

root = Tk() # Tkinter 생성
root.title("방명록 시스템") # 타이틀 설정
root.geometry("640x400") # 창 크기 설정
root.resizable(False, False) # 창 크기 변경 가능 여부 설정



########################################################################################
frame1 = Frame(root) # 프레임 생성
frame1.pack(side="left", fill="both", expand=True) # 프레임 표시

# 이름
Label(frame1, text="이름").pack() # "이름" 라벨 생성 후 pack
name = Entry(frame1, width=30) # 텍스트 필드 생성 후 name 에 저장
name.pack() # name pack

# 비밀번호
Label(frame1, text="비밀번호").pack() # "비밀번호" 라벨 생성 pack
pwd = Entry(frame1, width=30) # 텍스트 필드 생성 후 psw 에 저장
pwd.pack() # psw pack

# 내용
Label(frame1, text="내용").pack() # "내용" 라벨 생성 후 pack
wrt = Text(frame1, width=80, height=22) # 텍스트 필드 생성 후 wrt 에 저장
wrt.pack() # wrt pack
########################################################################################


########################################################################################
def write(): # 글 작성 함수
    if not name.get(): # name 엔트리가 공백일 경우 메세지 출력
        print("이름을 입력하세요.")
        
    elif not pwd.get():# password 엔트리가 공백일 경우 메세지 출력
        print("비밀번호를 입력하세요.")
        
    else: # name과 password 엔트리가 공백이 아닐 경우 글 등록 sql 실행
       
        # insert_data에 name 텍스트 필드, psw 텍스트 필드, wrt의 텍스트 필드 값을 리스트로 저장
        insert_data = [name.get(), pwd.get(), wrt.get("1.0", END)] 
        
        dbsql.writing(insert_data) # sql 함수에 insert_data 값을 보내 writing 실행
    
        name.delete(0, END) # dbsql.writing 실행 후 name 텍스트 필드 내용 삭제
        
        pwd.delete(0, END) # dbsql.writing 실행 후 psw 텍스트 필드 내용 삭제
        
        wrt.delete("1.0", END) # dbsql.writing 실행 후 wrt 텍스트 필드 내용 삭제

def find_written(Fname, Fpwd): # 작성한 글 찾기 함수
    
    account = [Fname, Fpwd] # 전달 받은 검색 창의 name과 pwd를 리스트에 삽입
    
    result = dbsql.load(account) # 리스트 값을 검색 데이터로 전달
    
    view_written(result) # 리턴 받은 select문 결과 값을 출력 함수로 전달

def find_written_window():
    # 새로운 창 생성
    global newWindow
    newWindow = Toplevel()
    
    # 라벨, 엔트리 프레임 생성
    FieldFrame = Frame(newWindow)
    FieldFrame.grid(row=0, column=0)
    
    # 라벨 생성과 필드 프레임에 삽입
    Label(FieldFrame, text="이름").grid(row=0, column=0)
    Label(FieldFrame, text="비밀번호").grid(row=1, column=0)
    
    # 엔트리 생성
    Fname = Entry(FieldFrame, width=30)
    Fpwd = Entry(FieldFrame, width=30)
    
    # 필드 프레임에 엔트리 삽입
    Fname.grid(row=0, column=1)
    Fpwd.grid(row=1, column=1)
    
    # 검색 버튼 프레임 생성과 출력
    ButtonFrame = Frame(newWindow)
    ButtonFrame.grid(row=0, column=3)
    
    # 검색 버튼 생성과 프레임 삽입
    Button(ButtonFrame, text="검색", command=lambda : find_written(Fname.get(), Fpwd.get())).grid(row=0, column=0)
    
def view_written(result):
    
    # select 문으로 받아온 글을 출력할 프레임 생성
    writtenFrame = Frame(newWindow)
    writtenFrame.grid(row=0, column=4)
    
    if result: # result의 값이 존재 할 때만 수행
        for i in result: 
            # 반복문을 통해 select문으로 가져온 이름, 암호, 글 내용을 출력함.
            Label(writtenFrame, text=i[0]).pack()
            Label(writtenFrame, text=i[1]).pack()
            Label(writtenFrame, text=i[3]).pack()
        
########################################################################################


########################################################################################
# 글 작성, 글 찾기 버튼 프레임 생성
frame2 = Frame(root)
frame2.pack(side="right", fill="both", expand=True)

# 글 작성
Button(frame2, text="작성", height=20, command=write).pack(fill="both", expand=True)

# 글 검색 윈도우를 여는 버튼
Button(frame2, text="작성 글\n 찾기", command=find_written_window).pack(fill="both", expand=True)
########################################################################################

root.mainloop()
