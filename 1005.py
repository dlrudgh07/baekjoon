
#================함수정의====================

testcase=int(input())
answer=[]
for _ in range(testcase):
    N,K=map(int,input().split()) # 건물의 개수, 건설규칙의 총 개수
    D=list(map(int,input().split())) # 건물당 건설에 걸리는 시간
    
    #이차원배열만들기
    building=[[] for i in range(N+1)]
    for _ in range(K):
        X,Y=map(int,input().split()) # 건물 X를 지은다음에 건물 Y를 지을 수 있다.
        building[Y-1].append[X-1] # 그러므로 후속건물인 Y에 선행건물 목록 X를 저장한다.

    W=int(input()) # 건설해야할 건물의 번호
    #================입력값처리====================
    answer.append(search(W)) 

for i in answer:
    print(i)

    

def search(building_number):
    if building[building_number]!=[]: # 선행조건이 있다면
        maxTime=max([search(i) for i in building[building_number]]) # 선행건물중 가장 오래걸리는 시간을 찾는다.
        return maxTime+D[building_number]
    else: # 선행조건이 없다면
        return D[building_number] # 건설시간을 반환한다.



