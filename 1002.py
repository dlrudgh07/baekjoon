import math
testcase=int(input())
result=[]
for T in range(testcase):
    x1,y1,r1,x2,y2,r2=map(float,input().split())
    
    

    D=math.sqrt((x1-x2)**2+(y1-y2)**2)

    if(D==0 and r1==r2 ): #두점이 같은점이고 반지름도 같을떄
        result.append(-1)
        continue
    if(D==0 and r1!=r2): 
        result.append(0)
        continue #반지름은 다를때

    if(D>r1+r2):
        result.append(0)
        continue
    if(D==r1+r2):
        result.append(1)
        continue

    if(D==abs(r1-r2)):
        result.append(1)
        continue
    if(D<abs(r1-r2)):
        result.append(0)
        continue
    if(abs(r1-r2)<D<(r1+r2)):
        result.append(2)
        continue
for i in range(testcase):
    print(result[i])
#-----------------------
'''



    t1
            

                 적

            
        t2

r1=t1~적 까지의 길이
r2=t2~적 까지의 길이

점2개(t1,t2)와 적까지의 거리(r1,r2)가 주어졌으므로

t1이 중심인 반지름이 r1인 원
t2가 중심인 반지름이 r2인 원 이 그려진다.

서로의 점까지의 길이를 D라고 하자

일반적으로 2개의 원이 겹치면 교점이 2개생긴다
또는 만나지않거나
접하는 경우가 있다.

https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=junhyuk7272&logNo=221139170814




--------------------------'''
