import random
num=random.randint(1,10)
"""
guess1=int(input("请输入第一次猜想的数字"))
if guess1 > num:
    print("大了，再猜一次吧")
elif guess1 < num:
    print("小了，再猜一次吧")
else:
    print("恭喜第一次就猜对了")
    exit()

guess2=int(input("请输入第二次猜想的数字"))
if guess2 > num:
    print("大了，再猜一次吧")
elif guess2 < num:
    print("小了，再猜一次吧")
else:
    print("恭喜第二次就猜对了")
    exit()

guess3 = int(input("请输入第三次猜想的数字"))
if guess3 > num:
    print("大了，我想的是%i"%num)
elif guess3 < num:
    print("小了，我想的是%i"%num)
else:
    print("恭喜第三次就猜对了")
    exit()

guess=int(input("请输入猜想的数字:"))
count=1
while guess!=num:
    if guess > num:
        print("大了，再猜一次吧")
    elif guess < num:
        print("小了，再猜一次吧")
    guess = int(input("请输入猜想的数字"))
    count+=1
print(f"第{count}次猜到了")
"""
#flag思想
count=0
flag=True
if count>5:
    flag=False
while flag:
    guess = int(input("请输入猜想的数字:"))
    count += 1
    if count >= 5:
        flag = False
        print(f"都不对，我想的是{count}")
        break
    if guess == num:
        print("猜对了")
        flag = False
    else:
        if guess < num:
            print("小了，再猜一次吧")
        elif guess > num:
            print("大了，再猜一次吧")
