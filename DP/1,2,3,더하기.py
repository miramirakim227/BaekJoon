# 정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.

# 1+1+1+1
# 1+1+2
# 1+2+1
# 2+1+1
# 2+2
# 1+3
# 3+1
# 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

# Sol: 점화식 느낌이면 DP 

total = int(input())

list_ = []
for i in range(total):
    list_.append(int(input()))

max_ = max(list_)
dp = [0] * max_     # 리스트는 빈칸으로 선언할 수 없음 
dp[0] = 1
dp[1] = 2
dp[2] = 4
for i in range(3, max_):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for num in list_:
    print(dp[num-1])
