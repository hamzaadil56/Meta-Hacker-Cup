def can_travelers_cross(N, K, times):
    times.sort()  # Sort travelers by their crossing times
    total_time = 0
    while N > 3:
        # Option 1: Send the two fastest, return the fastest
        option1 = times[1] + times[0] + times[N-1] + times[1]
        # Option 2: Send the two slowest, return the fastest
        option2 = times[N-1] + times[N-2] + 2 * times[0]
        total_time += min(option1, option2)
        N -= 2  # Two travelers successfully crossed

    # Deal with the last 3 or fewer travelers
    if N == 3:
        total_time += times[2] + times[0] + times[1]
    elif N == 2:
        total_time += times[1]
    elif N == 1:
        total_time += times[0]

    return total_time <= K


outputs = []

# Reading input
T = int(input())  # Number of test cases
for t in range(1, T + 1):
    # Number of travelers and maximum allowed time
    N, K = map(int, input().split())
    times = [int(input()) for _ in range(N)]  # Crossing times of travelers
    if can_travelers_cross(N, K, times):
        outputs.append(f"Case #{t}: YES")
    else:
        outputs.append(f"Case #{t}: NO")

for output in outputs:
    print(output)
