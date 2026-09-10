name=input("请输入姓名:")
money=5000
def seek(headShow):
    if headShow:
        print(f"--------------------查询余额--------------------")
    print(f"{name},您好，您的余额剩余：{money}元")
def cun(y):
    print(f"--------------------存款--------------------")
    seek(False)
def qu(z):
    print(f"--------------------取款--------------------")
    seek(False)

while True:
    x = int(input(f"--------------------主菜单--------------------\n{name},您好，欢迎来到肯斯任ATM,请选择操作"
                  "\n查询余额\t【请输入1】\n"
                  "存款\t\t【请输入2】\n取款\t\t【请输入3】\n退出\t\t【请输入4】"
                  "\n请输入您的选择:"))
    if x==1:
        seek(True)
    elif x==2:
        Cun=int(input("存入:"))
        money+=Cun
        cun(money)
    elif x==3:
        Qu = int(input("取出："))
        money -= Qu
        qu(money)
    elif x==4:
        print("退出成功")
        break
    else:
        print("无此操作")
        break
