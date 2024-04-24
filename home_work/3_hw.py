def hw_1 (a,b):
    if a>b:
        print(a)
    else:
        print(b)
hw_1(a=-5,b=-1)

def hw_2 (c,d):
    if (c-d) == 135:
        print('yes')
    elif (d-c) == 135:
        print('yes')
    else:
        print('no')
hw_2(c=65,d=200)

def hw_3 (season):
    if season in range(3,6):
        print('весна')
    elif season in range(6,9):
        print('лето')
    elif season in range(9,12):
        print('осень')
    elif season in range(1,3) or season==12:
        print('зима')
    else:
        print('введите корректное число месяца')
hw_3 (season=12)

def hw_4 (a,b,c):
    if a>10 and b>10 and c>10:
        print('yes')
    else:
        print('no')
hw_4 (a=14,b=-4,c=17)

def hw_6 (year,month):
    a=year*12*29
    b=month*29
    print(a+b,'дней')
hw_6(year=33,month=8)

def hw_5 (x):
    a=sum(1 for b in x if b>=0)
    print (a)
hw_5(x=[-1,8,-6,10,0])


