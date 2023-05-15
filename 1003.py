'''
1부터 n까지의 결과를 구한다.(피보나치식으로 말고 단순 1부터 n까지)
결과를 뽑아서 쓴다.
Dynamic Programing 의 Memorization 방법
'''
testcase=int(input())

queue=[]
for i in range(testcase):
    queue.append(int(input()))

## 입력값 처리
def fibonacci(n):
    for i in range(2,n+1):
        countList.append([countList[i-1][0]+countList[i-2][0],countList[i-1][1]+countList[i-2][1]])
for n in queue:
    countList=[]
    countList.append([1,0])
    countList.append([0,1])
    fibonacci(n)
    print(countList[n][0],countList[n][1])
