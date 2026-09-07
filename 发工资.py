count=10000
for i in range(1, 21):
    import random
    num = random.randint(1, 10)
    if num < 5:
        print(f"员工{i},绩效{num}分，低于五，不发工资下一位")
        continue

    if count >0:
        count -= 1000
        print(f"向员工{i}发放工资1000元，账户余额{count}元")
    else:
        print("工资发完了，下个月领取吧")
        break