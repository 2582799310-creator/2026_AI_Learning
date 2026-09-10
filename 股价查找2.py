gu1={"AAPL":175.0,"GOOGL":135.5,"TSLA":250.0}
def find_max():
    Max1=max(gu1,key=gu1.get)
    print(Max1)
find_max()