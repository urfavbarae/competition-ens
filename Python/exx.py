import math

def calculate_distance(p1, p2):
  return math.sqrt((p1['x'] - p2['x'])**2 + (p1['y'] - p2['y'])**2)

def find_pairs(remaining_players, current_pairs, current_distance_sum, min_distance_sum):
  if not remaining_players:
    min_distance_sum[0] = min(min_distance_sum[0], current_distance_sum)
    return

  player1 = remaining_players[0]
  for i in range(1, len(remaining_players)):
    player2 = remaining_players[i]
    distance = calculate_distance(player1, player2)

    new_remaining_players = remaining_players[1:]
    new_remaining_players.pop(i - 1)

    find_pairs(new_remaining_players, current_pairs + [(player1, player2)], current_distance_sum + distance, min_distance_sum)

def solve():
  t = int(input())
  for _ in range(t):
    n = int(input())
    players = []
    for _ in range(2 * n):
      name, x, y = input().split()
      players.append({'x': int(x), 'y': int(y)})

    min_distance_sum = [float('inf')]
    find_pairs(players, [], 0, min_distance_sum)
    print(f"{min_distance_sum[0]:.2f}")

solve()