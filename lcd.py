valid=['1','2','5','6','8','9','0']
num=int(input())
val=0
lis=[]
for i in range(100):
    for j in str(i):
        if j not in valid:
            break
    else:
        lis.append(i)
        val=val+1
        if val==num+1:
            print(i)
            break

                      
        
