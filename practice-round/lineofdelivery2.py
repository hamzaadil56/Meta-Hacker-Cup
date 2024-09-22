def solve_curling_game_with_collisions():
  T = int(input())  # Number of test cases
  for t in range(1, T + 1):
      N, G = map(int, input().split())  # Number of stones and the goal position
      energies = [int(input()) for _ in range(N)]  # Energies of the stones

      # Initialize positions array
      final_positions = [-1] * N  # Initially, no stone has moved yet

      # Simulate throwing stones
      for i in range(N):
          energy = energies[i]
          pos = energy  # The initial target position is its energy

          # Check for collision with previous stones
          while pos in final_positions:
              # Find the index of the stone at position pos
              colliding_index = final_positions.index(pos)
              # Transfer remaining energy to the colliding stone
              remaining_energy = pos - final_positions[colliding_index]
              pos = final_positions[colliding_index] + remaining_energy

          # Store the final position of the current stone
          final_positions[i] = pos

      # Now, we have all stones' final positions, calculate distance from the goal G
      closest_stone_index = -1
      closest_distance = float('inf')

      for i in range(N):
          distance = abs(final_positions[i] - G)
          if distance < closest_distance or (distance == closest_distance and i + 1 < closest_stone_index):
              closest_stone_index = i + 1  # Stones are 1-indexed
              closest_distance = distance

      # Output the result for this test case
      print(f"Case #{t}: {closest_stone_index} {closest_distance}")

# Example usage:
solve_curling_game_with_collisions()
