import sys

input = sys.stdin.readline

def calculate_score(pieces):
    scores = {'k': 0, 'p': 1, 'n': 3, 'b': 3, 'r': 5, 'q': 9}
    score = sum(scores[piece.lower()] for piece in pieces)
    
    return score

board = [list(input().rstrip()) for _ in range(8)]

white = [piece for line in board for piece in line if piece.isupper()]
black = [piece for line in board for piece in line if piece.islower()]

w_score = calculate_score(white)
b_score = calculate_score(black)

print(w_score - b_score)