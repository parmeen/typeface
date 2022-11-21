str1=input()
str2=input()
s=str2[-1]
count=0
for i in str1:
    if i==s:
        count=count+1
print(count)
