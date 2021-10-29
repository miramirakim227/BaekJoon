# RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.

# 집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

# 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
# N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
# i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.

dpr = [0] * 10000
dpg = [0] * 10000
dpb = [0] * 10000

num_house = int(input())

for i in range(num_house):
    price_rgb = list(map(int, input().split(' ')))
    if i == 0:
        dpr[0], dpg[0], dpb[0] = price_rgb[0], price_rgb[1], price_rgb[2]
    else:
        dpr[i] = price_rgb[0] + min(dpg[i-1], dpb[i-1])
        dpg[i] = price_rgb[1] + min(dpr[i-1], dpb[i-1])
        dpb[i] = price_rgb[2] + min(dpr[i-1], dpg[i-1])

print(min(dpr[num_house-1], dpg[num_house-1], dpb[num_house-1]))


# 다음에 풀 때: -1의 정보만 사용한다면, 맨 마지막 값만 알면 되면 -> scalar값으로 저장해버리기! 
