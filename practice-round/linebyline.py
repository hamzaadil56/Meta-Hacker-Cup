def calculate_P_to_be_increased(N, P):
    P_1 = 100 * ((P / 100)**((N - 1) / N))
    return P_1 - P


outputs = []

T = int(input())
for t in range(1, T + 1):
    N, P = map(int, input().split())
    p_to_be_increase = calculate_P_to_be_increased(N, P)
    outputs.append(f"Case #{t}: {p_to_be_increase} ")

for output in outputs:
    print(output)
