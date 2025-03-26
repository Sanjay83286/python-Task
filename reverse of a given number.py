# Reverse of a given number
a=1234
result=0
num=0
sum=0
count=0
while a>0:
    result=a%10
    num=num*10+result
    sum=sum+result
    count+=1
    if result%3==0:
        print("number divisible by 3 are =",result)
    a=a//10
print("reverse of a given number=",num,"sum is =",sum,"count =",count)