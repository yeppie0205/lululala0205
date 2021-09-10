import turtle as t
import random

ro = input("자리 배치 스따뜨")

# 교탁 만들기
t.up()
t.goto(100, -400)
t.down()
t.speed(0)

for i in range(2):
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(200)

t.up()
t.goto(-10,-435)
t.down()
t.write("교탁")

# 복도
t.up()
t.goto(-490, 0)
t.write("복도")

# 창가
t.up()
t.goto(480, 0)
t.write("창가")

    
# 자리 만들기
t.up()
t.goto(450, 372)
t.down()
t.speed(0)

for i in range(2):
    t.right(90)
    t.forward(744)
    t.right(90)
    t.forward(900)

for i in range(5):
    n = (-450) + 180*i
    t.up()
    t.goto(n, 370)
    t.down()
    t.setheading(270)
    t.forward(740)

for i in range(6):
    n = (-372) + 124*i
    t.up()
    t.goto(-450, n)
    t.down()
    t.setheading(0)
    t.forward(900)

# 랜덤 자리 배치
eban = ["1번 강혜영", "2번 공민서", "3번 곽나윤", "4번 김보미", "5번 김성현", "6번 김수희", "7번 김채원", "8번 김호정", "9번 목수연", "10번 박지유", "11번 박지성", "12번 박지원", "13번 서정원", "15번 신예원", "16번 양다성", "17번 양채린", "18번 유영서", "19번 이서인", "20번 이소민", "21번 이소은", "22번 이예원", "23번 이유민", "24번 이윤영", "25번 이주원",
       "26번 장민경", "27번 정동영", "28번 좌서연", "29번 최원영", "30번 홍수민", "31번 황이빈"]
random.shuffle(eban)

for z in range(5):
        q = eban[z : z+1]
        m = (-450) + 180 * z
        t.up()
        t.goto(m + 30, 248 + 50)
        t.down()
        t.write(q)
        
a = 5
for z in range (5):
        q = eban[a : a + 1]
        m = (-450) + 180 * z
        t.up()
        t.goto(m + 30, 124 + 50)
        t.down()
        t.write(q)
        a = a + 1
a = 10
for z in range (5):
        q = eban[a : a + 1]
        m = (-450) + 180 * z
        t.up()
        t.goto(m + 30, 0 + 50)
        t.down()
        t.write(q)
        a = a + 1
a = 15
for z in range (5):
        q = eban[a : a + 1]
        m = (-450) + 180 * z
        t.up()
        t.goto(m + 30, -74)
        t.down()
        t.write(q)
        a = a + 1
a = 20
for z in range (5):
        q = eban[a : a + 1]
        m = (-450) + 180 * z
        t.up()
        t.goto(m + 30, -198)
        t.down()
        t.write(q)
        a = a + 1
a = 25
for z in range (5):
        q = eban[a : a + 1]
        m = (-450) + 180 * z
        t.up()
        t.goto(m + 30, -322)
        t.down()
        t.write(q)
        a = a + 1
