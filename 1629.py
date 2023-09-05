#mod 성질 : (a*b)%c = ((a%c)*(b%c))%c
# ==> (a*a)%c = (a%c)*(a%c)%c 

a,b,c=map(int,input().split())

AmodC=a%c
answer=a%c
stack=[]

while(b): # log b 번 반복
    stack.append(b)
    b=b//2

for i in stack[::-1]:
    if i==1:
        continue
    
    if(i%2==0):
        answer=(answer%c)*(answer%c)%c # C^n= C^n/2 * C^n/2
    else:   
        answer=((answer%c)*(answer%c)%c)*(AmodC%c)%c
        # C^n= C^(n-1)/2 * C^(n-1)/2 * C


print(answer)
        


    


    