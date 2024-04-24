num=-2
if num>=0:
    print('Число больше либо равно 0')
else:
    print('Число отризательное')


def yes_no(str_1,str_2):
    if str_1 in str_2:
        print ('ДА')
    else:
        print('НЕТ')
        yes_no(str_1='test',str_2='test1')


str_1="testing"
str_2="home"
if str_2 in str_1:
    print('ДА')
else:
    print('НЕТ')

num_float=-5
if num_float >0:
    print('положительное число')
elif num_float ==0:
    print('ноль')
else:
    print('отрицательное')
permit = True
if num >0 and permit:
    print('num-положительное число')
elif not permit:
    print('печать запрещена')

def year (a):
    if a >=1 and a<=4:
        print('бакалавр')
    elif a>=5 and a<=6:
        print('магистр')
    elif a>=7 and a<=9:
        print('аспирант')
    else:
        print('введите корректный год обучения')
year(a=0)

b=200
if b>100 or b<-100:
    print('-')
else:
    print('+')
