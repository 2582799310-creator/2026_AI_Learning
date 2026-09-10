def count_letters(text):
    res={}
    for i in text:
        if i!=" ":
            if i in res:
                res[i]+=1
            else:
                res[i]=1
        else:
            continue
    print(res)

count_letters("hello world")