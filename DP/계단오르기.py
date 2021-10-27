# 계단 오르기 게임은 계단 아래 시작점부터 계단 꼭대기에 위치한 도착점까지 가는 게임이다. <그림 1>과 같이 각각의 계단에는 일정한 점수가 쓰여 있는데 계단을 밟으면 그 계단에 쓰여 있는 점수를 얻게 된다.
# 계단 오르는 데는 다음과 같은 규칙이 있다.

# 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
# 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
# 마지막 도착 계단은 반드시 밟아야 한다.
# 따라서 첫 번째 계단을 밟고 이어 두 번째 계단이나, 세 번째 계단으로 오를 수 있다. 하지만, 첫 번째 계단을 밟고 이어 네 번째 계단으로 올라가거나, 첫 번째, 두 번째, 세 번째 계단을 연속해서 모두 밟을 수는 없다.

# 각 계단에 쓰여 있는 점수가 주어질 때 이 게임에서 얻을 수 있는 총 점수의 최댓값을 구하는 프로그램을 작성하시오.

num_stairs = int(input())
dp = [0] * (num_stairs+1)

score_stairs = []
for i in range(num_stairs):
    score_stairs.append(int(input()))

if num_stairs >= 1:
    dp[1] = score_stairs[0]
if num_stairs >= 2:
    dp[2] = score_stairs[0] + score_stairs[1]
if num_stairs >= 3:
    dp[3] = max(score_stairs[0], score_stairs[1]) + score_stairs[2]
if num_stairs >= 4:
    dp[4] = score_stairs[0] + max(score_stairs[1], score_stairs[2]) + score_stairs[3]

if len(dp) >= 5:
    for i in range(5, len(dp)):
        dp[i] = score_stairs[i-1] + max(score_stairs[i-2] + dp[i-3], score_stairs[i-3]+max(score_stairs[i-4] + dp[i-5], dp[i-4]))
print(dp[num_stairs])


