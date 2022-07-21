import sys
input = sys.stdin.readline
n, m = map(int, input().split())

cards = list(map(int, input().split()))
for _ in range(m):
  cards.sort()
  sum_cards = cards[0] + cards[1]
  cards[0], cards[1] = sum_cards, sum_cards

print(sum(cards))
  