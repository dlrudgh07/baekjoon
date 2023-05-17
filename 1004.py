testcase=int(input())
answerQueue=[]
for i in range(testcase):
    a,b,c,d=map(int,input().split())
    startpoint=[a,b]
    endpoint=[c,d]

    numberOfPlanet=int(input()) 
    circlePoint=[] # 원의 중심
    radius=[] # 반지름
    for j in range(numberOfPlanet):
        x,y,r=map(int,input().split())
        circlePoint.append([x,y])
        radius.append(r)

# ----- 입력값 처리 -----

    count=0 
    # 시작지점,끝지점과 원의중심까지의 거리를 구하여 시작지점이 원 내부에 있는지를 판단합니다.
    for index,p in enumerate(circlePoint):
        case1,case2=False,False    # 같은원인지를 판단하는 변수, 같은원일 경우 count-=2
        if(p[0]-startpoint[0])**2+(p[1]-startpoint[1])**2<radius[index]**2: # 원의 내부에 있음
            count+=1
            case1=True
        if(p[0]-endpoint[0])**2+(p[1]-endpoint[1])**2<radius[index]**2: 
            count+=1
            case2=True
        if case1 and case2: # 같은원일 경우 count-=2
            count-=2
    answerQueue.append(count)

for i in range(testcase):
    print(answerQueue[i])

