def solve_curling_game():
    T = int(input())  # Number of test cases
    for t in range(1, T + 1):
        N, G = map(int, input().split())  # Number of stones and the goal position
        stones = []
        for i in range(N):
            E = int(input())  # Energy of the i-th stone
            stones.append((E, i + 1))  # Store energy and 1-based index

        # Sort stones by their initial energies (larger energy stones move first)
        stones.sort(reverse=True)

        final_positions = {}  # Dictionary to store final positions of each stone

        for energy, index in stones:
            pos = energy  # Start by assuming the stone travels to full energy
            while pos in final_positions:
                # If there's a collision, transfer remaining energy to next stone
                remaining_energy = pos - final_positions[pos]
                pos = final_positions[pos] + remaining_energy

            # Store final position of this stone
            final_positions[pos] = index

        # Now, we have all stones' final positions, calculate distance from the goal G
        closest_stone_index = -1
        closest_distance = float('inf')

        for pos, index in final_positions.items():
            distance = abs(pos - G)
            if distance < closest_distance or (distance == closest_distance and index <                           closest_stone_index):
                closest_stone_index = index
                closest_distance = distance

        # Output the result for this test case
        print(f"Case #{t}: {closest_stone_index} {closest_distance}")


# Example usage:
solve_curling_game()
