# 프로그램 모음

 # 순서 정하기
 # 자리 배치
 # 조 짜기
 # 발표자 뽑기

# 순서 뽑기
import random
o = input("어떤 기능을 고르시겠습니까? : ")

if o == "순서 정하기":
    print()
    t = input("순서 정하기 시작")
    print()
    
    def nmixx():
        i = ["20501 곽시은", "20502 김민채", "20503 김성현", "20504 김수희", "20505 김채원", "20506 박민주", "20507 박신혜",
             "20508 박영서", "20509 박주은", "20510 박지유", "20511 서유민", "20512 손수경", "20513 손지민", "20514 안다경",
             "20515 안혜지", "20516 양다성", "20517 양서현", "20518 이소민", "20519 이예원", "20520 이유민", "20521 이주원",
             "20522 이하은", "20523 장민경", "20524 장소현", "20525 전유진", "20526 정동영", "20527 조수민", "20528 최원영",
             "20529 홍수민"]
        random.shuffle(i)
        nn = 0
        for po in range(1, 30):
            print(po,"번 ",i[nn : nn +1])
            nn = nn + 1
                
    nmixx()

# 조 짜기
if o == "조 짜기":
    p = int(input("몇 명씩 짜실겁니까? : "))
    print()
    t = input("조 만들기 시작")
    print()
    def nctdream():
        if 29 % p != 0:
            w = list(range(1,30))
            random.shuffle(w)
            nn = 0
            q = int((29 // p) + 1)
            for i in range(1, q):
                k = p * i
                print(i,"조 ", w[nn : k])
                nn = k
            print(i + 1,"조 ", w[k : 29])
            print()
            print("남은 인원은 위의 조부터 차례대로 배정하십시오.")
            
    nctdream()

# 자리 배치
if o == "자리 배치":
    print()
    import turtle as t
    import random

    q = input("자리 배치 스따뚜(start)")

    # 교탁 만들기
    t.up()
    t.goto(90, -400)
    t.down()
    t.speed(0)

    for i in range(2):
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(200)

    t.up()
    t.goto(-30,-435)
    t.down()
    t.write("교탁", font = ("", 15))

    # 복도
    t.up()
    t.goto(-560, 0)
    t.write("복도", font = ("", 15))

    # 창가
    t.up()
    t.goto(480, 0)
    t.write("창가", font = ("", 15))

    # 자리 만들기
    t.up()
    t.goto(450,372)
    t.down()
    t.speed(0)

    for i in range(2):
        t.right(90)
        t.forward(744)
        t.right(90)
        t.forward(300)

    for k in range(5):
        n = 372 - 148 * k
        t.up()
        t.goto(450, n)
        t.down()
        t.forward(-300)

    t.up()
    t.goto(130,372)
    t.down()

    for i in range(2):
        t.right(90)
        t.forward(744)
        t.right(90)
        t.forward(300)

    for k in range(5):
        n = 372 - 148 * k
        t.up()
        t.goto(130, n)
        t.down()
        t.forward(-300)
    
    t.up()
    t.goto(-190,372)
    t.down()

    for i in range(2):
        t.right(90)
        t.forward(744)
        t.right(90)
        t.forward(300)

    for k in range(5):
        n = 372 - 148 * k
        t.up()
        t.goto(-190, n)
        t.down()
        t.forward(-300)

    t.up()
    t.goto(300,372)
    t.right(90)
    t.down()
    t.forward(744)
    t.up()
    t.goto(-20, 372)
    t.down()
    t.forward(744)
    t.up()
    t.goto(-335,372)
    t.down()
    t.forward(744)

    # 랜덤 자리 배치
    eban = ["곽시은", "김민채", "김성현", "김수희", "김채원", "박민주", "박신혜", "박영서", "박주은", "박지유", "서유민", "손수경", "손지민", "안다경", "안혜지", "양다성", "양서현", "이소민", "이예원", "이유민", "이주원", "이하은", "장민경", "장소현", "전유진",
       "정동영", "조수민", "최원영", "홍수민"]
    random.shuffle(eban)
    job = ["(3분단 쓸기)", "(칠판 닦기/행주 세탁)", "(2분단 책상 원위치)","(2분단 닦기)", "(아침 쓰레기 줍기)", "(창틀/대리석 닦기)", "(3분단 쓸기)", "(사물함 위쪽 닦기)", "(2분단 책상 원위치)", "(2분단 쓸기)", "(칠판 분필가루 정리)",
       "(1분단 쓸기)", "(3분단 책상 원위치)", "(3분단 닦기)", "(맨앞/맨뒤/구석 쓸기)", "(2분단 쓸기)","(1분단 닦기)","(1분단 쓸기)", "(3분단 책상 원위치)", "(베란다 청소)", "(쓰레기통)", "(쓰레기통)", "(1분단 책상 원워치)", "(1분단 책상 원위치)", "(칠판 지우개 세탁)", "(베란다 청소)","(쓰레기통)",
       "(쓰레기통)", "(특별 : 3층~2층 계단)"]

    for z in range(6):
            q = eban[z : z+1]
            fu = job[z : z+1]
            m = (-502) + 161 * z
            t.up()
            t.goto(m + 30, 248 + 50)
            t.down()
            t.write(q, font = ("", 15))
            t.up()
            n = (-505) + 161 * z
            t.goto(n + 30, 278)
            t.down()
            t.write(fu, font = ("", 8))
        
        
    a = 6
    p = 6
    for z in range (6):
            q = eban[a : a + 1]
            fu = job[p : p + 1]
            m = (-502) + 161 * z
            t.up()
            t.goto(m + 30, 98 + 50)
            t.down()
            t.write(q, font = ("", 15))
            a = a + 1
            t.up()
            n = (-505) + 161 * z
            t.goto(n + 30, 128)
            t.down()
            t.write(fu, font = ("", 8))
            p = p + 1
        
    a = 12
    p = 12
    for z in range (6):
            q = eban[a : a + 1]
            fu = job[p : p + 1]
            m = (-502) + 161 * z
            t.up()
            t.goto(m + 30, -2)
            t.down()
            t.write(q, font = ("", 15))
            a = a + 1
            t.up()
            n = (-505) + 161 * z
            t.goto(n + 30, -22)
            t.down()
            t.write(fu, font = ("", 8))
            p = p + 1
        
    a = 18
    p = 18
    for z in range (6):
            q = eban[a : a + 1]
            fu = job[p : p + 1]
            m = (-502) + 161 * z
            t.up()
            t.goto(m + 30, -152)
            t.down()
            t.write(q, font = ("", 15))
            a = a + 1
            t.up()
            n = (-505) + 161 * z
            t.goto(n + 30, -178)
            t.down()
            t.write(fu, font = ("", 8))
            p = p + 1
        
    a = 24
    p = 24
    for z in range (6):
            q = eban[a : a + 1]
            fu = job[p : p + 1]
            m = (-502) + 161 * z
            t.up()
            t.goto(m + 30, -302)
            t.down()
            t.write(q, font = ("", 15))
            a = a + 1
            t.up()
            n = (-505) + 161 * z
            t.goto(n + 30, -328)
            t.down()
            t.write(fu, font = ("", 8))
            p = p + 1

# 발표자 뽑기
if o == "발표자 뽑기":
    print()
    def txt():
        i = ["20501 곽시은", "20502 김민채", "20503 김성현", "20504 김수희", "20505 김채원", "20506 박민주", "20507 박신혜",
             "20508 박영서", "20509 박주은", "20510 박지유", "20511 서유민", "20512 손수경", "20513 손지민", "20514 안다경",
             "20515 안혜지", "20516 양다성", "20517 양서현", "20518 이소민", "20519 이예원", "20520 이유민", "20521 이주원",
             "20522 이하은", "20523 장민경", "20524 장소현", "20525 전유진", "20526 정동영", "20527 조수민", "20528 최원영",
             "20529 홍수민"]
        random.shuffle(i)
        print(i[0:1])
    txt()
        

            
        
   


    
    

