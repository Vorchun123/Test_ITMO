def task_1 ()->bool:
    a=5
    print(a, "относиться к типу", type(a))
    b=15.5
    print(b, "относиться к типу", type(b))
    c='слово'
    print(c, "относиться к типу", type(c))
    d=[2,4,6,8,10]
    print(d, "относиться к типу", type(d))
    e=True
    print(e, "относиться к типу", type(e))
    return (e)
print (task_1())
def task_2()->list:
    a=[1,2,3,5,8,13,21]
    return (a[0:3])
print (task_2())
def task_3(x:int)->int:
    return x**2
print (task_3(5))


