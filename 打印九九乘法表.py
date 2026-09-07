"""
num2=1
while num2<=9:
    num1 = 1
    while num1 <= num2:
        print(f"\t{num1}*{num2}={num1 * num2}",end='\t')
        num1 += 1
    print()
    num2 += 1
"""

for num2 in range(1,10):
    num1=1
    for num1 in range(1,num2+1):
        print(f"\t{num1}*{num2}={num1 * num2}", end='\t')
    print()




