n=int(input("enter the no.of numbers:"))
numbers=[]
count=0
count1=0
for i in range(n):
    num=int(input(f"enter number{i+1}:"))
    numbers.append(num)
    if num%2==0:
          count+=1
    else:
          count1+=1
print('even-',count)
print('odd-',count1)
