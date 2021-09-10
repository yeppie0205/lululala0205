# 비교 우위 계산기
import fractions
import turtle 

m = input("기준이 무엇인가요? (생산비, 생산량 중 택 1) : ")
q = input("1 국가 이름을 입력하세요. : ")
w = input("2 국가 이름을 입력하세요. : ")
e = input("1 재화 이름을 입력하세요. : ")
r = input("2 재화 이름을 입력하세요. : ")

if m == "생산비":
    t = int(input(f"{q}의 {e}의 생산비를 입력하세요. : "))
    y = int(input(f"{q}의 {r}의 생산비를 입력하세요. : "))
    u = int(input(f"{w}의 {e}의 생산비를 입력하세요. : "))
    i = int(input(f"{w}의 {r}의 생산비를 입력하세요. : "))

    print()

    Irr = fractions.Fraction(t, y)
    t = Irr.numerator
    y = Irr.denominator

    print(f"{q} : {e} 1 = {r} {Irr}")

    Irra = fractions.Fraction(y, t)
    y = Irra.numerator
    t = Irra.denominator

    print(f"{q} : {r} 1 = {e} {Irra}")

    Irrb = fractions.Fraction(u, i)
    u = Irrb.numerator
    i = Irrb.denominator

    print(f"{w} : {e} 1 = {r} {Irrb}")

    Irrc = fractions.Fraction(i, u)
    i = Irrc.numerator
    u = Irrc.denominator

    print(f"{w} : {r} 1 = {e} {Irrc}")

    print()

    if Irr > Irrb:
        print(f"{e}의 비교 우위에 있는 곳은 {w}입니다.")
        if Irra > Irrc:
            print(f"{r}의 비교 우위에 있는 곳은 {w}입니다.")
            print()
            j = input("무역의 비율이 가능한지 보시겠습니까?(예 / 아니오 중 택 1) : ")
            if j == "예":
                z = int(input(f"무역의 비율을 입력하십시오. ({e}: {r} 중 {e}) : "))
                x = int(input(f"무역의 비율을 입력하십시오. ({e}: {r} 중 {r}) : "))

                Irrd = fractions.Fraction(x, z)
                x = Irrd.numerator
                z = Irrd.denominator

                print()
            
                if Irrb <= Irrd <= Irr:
                    print("무역 가능")
                else:
                    print("무역 불가능")
            else:
                print()
                print(">>>기능을 멈추겠습니다.<<<")
        else:
            print(f"{r}의 비교 우위에 있는 곳은 {q}입니다.")
            print()
            j = input("무역의 비율이 가능한지 보시겠습니까?(예 / 아니오 중 택 1) : ")
            if j == "예":
                z = int(input(f"무역의 비율을 입력하십시오. ({e}: {r} 중 {e}) : "))
                x = int(input(f"무역의 비율을 입력하십시오. ({e}: {r} 중 {r}) : "))

                Irrd = fractions.Fraction(x, z)
                x = Irrd.numerator
                z = Irrd.denominator
                
                print()
            
                if Irrb <= Irrd <= Irr:
                    print("무역 가능")
                else:
                    print("무역 불가능")
            else:
                print()
                print(">>>기능을 멈추겠습니다.<<<")
                
        
    else:
        print(f"{e}의 비교 우위에 있는 곳은 {q}입니다.")
        if Irra > Irrc:
            print(f"{r}의 비교 우위에 있는 곳은 {w}입니다.")
            print()
            j = input("무역의 비율이 가능한지 보시겠습니까?(예 / 아니오 중 택 1) : ")
            if j == "예":
                z = int(input(f"무역의 비율을 입력하십시오. ({e}: {r} 중 {e}) : "))
                x = int(input(f"무역의 비율을 입력하십시오. ({e}: {r} 중 {r}) : "))

                Irrd = fractions.Fraction(x, z)
                x = Irrd.numerator
                z = Irrd.denominator

                print()
            
                if Irr <= Irrd <= Irrb:
                    print("무역 가능")
                else:
                    print("무역 불가능")
            else:
                print()
                print(">>>기능을 멈추겠습니다.<<<")

        else:
            print(f"{r}의 비교 우위에 있는 곳은 {q}입니다.")
            print()
            j = input("무역의 비율이 가능한지 보시겠습니까?(예 / 아니오 중 택 1) : ")
            if j == "예":
                z = int(input(f"무역의 비율을 입력하십시오. ({e}: {r} 중 {e}) : "))
                x = int(input(f"무역의 비율을 입력하십시오. ({e}: {r} 중 {r}) : "))

                Irrd = fractions.Fraction(x, z)
                x = Irrd.numerator
                z = Irrd.denominator

                print()
            
                if Irr <= Irrd <= Irrb:
                    print("무역 가능")
                else:
                    print("무역 불가능")
            else:
                print()
                print(">>>기능을 멈추겠습니다.<<<")

if m == "생산량":
    t = int(input(f"{q}의 {e}의 생산량을 입력하세요. : "))
    y = int(input(f"{q}의 {r}의 생산량을 입력하세요. : "))
    u = int(input(f"{w}의 {e}의 생산량을 입력하세요. : "))
    i = int(input(f"{w}의 {r}의 생산량을 입력하세요. : "))

    tt = t
    yy = y
    uu = u
    ii = i

    print()

    Irr = fractions.Fraction(y, t)
    y = Irr.numerator
    t = Irr.denominator

    print(f"{q} : {e} 1 = {r} {Irr}")

    Irra = fractions.Fraction(t, y)
    t = Irra.numerator
    y = Irra.denominator

    print(f"{q} : {r} 1 = {e} {Irra}")

    Irrb = fractions.Fraction(i, u)
    i = Irrb.numerator
    u = Irrb.denominator

    print(f"{w} : {e} 1 = {r} {Irrb}")

    Irrc = fractions.Fraction(u, i)
    u = Irrc.numerator
    i = Irrc.denominator

    print(f"{w} : {r} 1 = {e} {Irrc}")

    print()

    if Irr > Irrb:
        print(f"{e}의 비교 우위에 있는 곳은 {w}입니다.")
        if Irra > Irrc:
            print(f"{r}의 비교 우위에 있는 곳은 {w}입니다.")
            print()
            j = input("무역의 비율이 가능한지 보시겠습니까?(예 / 아니오 중 택 1) : ")
            if j == "예":
                z = int(input(f"무역의 비율을 입력하십시오. ({e}: {r} 중 {e}) : "))
                x = int(input(f"무역의 비율을 입력하십시오. ({e}: {r} 중 {r}) : "))

                Irrd = fractions.Fraction(x, z)
                x = Irrd.numerator
                z = Irrd.denominator

                print()
            
                if Irrb <= Irrd <= Irr:
                    print("무역 가능")
                else:
                    print("무역 불가능")
            else:
                print()
                print(">>>기능을 멈추겠습니다.<<<")
        else:
            print(f"{r}의 비교 우위에 있는 곳은 {q}입니다.")
            print()
            j = input("무역의 비율이 가능한지 보시겠습니까?(예 / 아니오 중 택 1) : ")
            if j == "예":
                z = int(input(f"무역의 비율을 입력하십시오. ({e}: {r} 중 {e}) : "))
                x = int(input(f"무역의 비율을 입력하십시오. ({e}: {r} 중 {r}) : "))

                Irrd = fractions.Fraction(x, z)
                x = Irrd.numerator
                z = Irrd.denominator
                
                print()
            
                if Irrb <= Irrd <= Irr:
                    print("무역 가능")
                else:
                    print("무역 불가능")
            else:
                print()
                print(">>>기능을 멈추겠습니다.<<<")
        
    else:
        print(f"{e}의 비교 우위에 있는 곳은 {q}입니다.")
        if Irra > Irrc:
            print(f"{r}의 비교 우위에 있는 곳은 {w}입니다.")
            print()
            j = input("무역의 비율이 가능한지 보시겠습니까?(예 / 아니오 중 택 1) : ")
            if j == "예":
                z = int(input(f"무역의 비율을 입력하십시오. ({e}: {r} 중 {e}) : "))
                x = int(input(f"무역의 비율을 입력하십시오. ({e}: {r} 중 {r}) : "))

                Irrd = fractions.Fraction(x, z)
                x = Irrd.numerator
                z = Irrd.denominator

                print()
            
                if Irr <= Irrd <= Irrb:
                    print("무역 가능")
                else:
                    print("무역 불가능")
            else:
                   print()
                   print(">>>기능을 멈추겠습니다.<<<")

        else:
            print(f"{r}의 비교 우위에 있는 곳은 {q}입니다.")
            print()
            j = input("무역의 비율이 가능한지 보시겠습니까?(예 / 아니오 중 택 1) : ")
            if j == "예":
                z = int(input(f"무역의 비율을 입력하십시오. ({e}: {r} 중 {e}) : "))
                x = int(input(f"무역의 비율을 입력하십시오. ({e}: {r} 중 {r}) : "))

                Irrd = fractions.Fraction(x, z)
                x = Irrd.numerator
                z = Irrd.denominator

                print()
            
                if Irr <= Irrd <= Irrb:
                    print("무역 가능")
                else:
                    print("무역 불가능")
            else:
                print()
                print(">>>기능을 멈추겠습니다.<<<")

    print()
    l = input("생산 가능 곡선을 그리시겠습니까?(예 / 아니오 중 택 1) : ")
    if l == "예":
        # 좌표축 그리기
        turtle.title("생산 가능 곡선")
        turtle.bgcolor("black")
        turtle.color("white")
        turtle.speed(0)
        turtle.up()
        turtle.goto(-380, -380)
        turtle.down()
        turtle.forward(760)
        turtle.write(f"{e}", font = ("", 15))
        turtle.forward(-760)
        turtle.setheading(90)
        turtle.forward(760)
        turtle.write(f"{r}", font = ("", 15))
        turtle.forward(-760)

        # 생산 가능 곡선 그리기
        turtle.goto(tt, -380)
        turtle.write(f"{tt}", font = ("", 15))
        turtle.goto(-380, yy) 
        turtle.write(f"{yy}", font = ("", 15))

        f = 380 + tt
        g = 380 + yy
        
        turtle.up()
        turtle.goto((-380) + f * uu / tt, -380)
        turtle.down()
        turtle.write(f"{uu}", font = ("", 15))
        turtle.goto(-380, (-380) + g * ii / yy) 
        turtle.write(f"{ii}", font = ("", 15))
    else:
        print(">>>기능을 멈추겠습니다.<<<")
        



    

            


        

    

    
    


    
    


    


    
    
