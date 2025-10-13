marks=[]
for i in range(5):
    mark=float(input(f"enter the marks of student{i+1}:"))
    marks.append(mark)
def average(marks):
     average=sum(marks)/5
     print(f"\nAverage marks: {average:}")
average(marks)
