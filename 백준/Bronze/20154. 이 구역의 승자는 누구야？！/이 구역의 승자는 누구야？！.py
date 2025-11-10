score = [3, 2, 1, 2, 3, 3, 3, 3, 1, 1, 3, 1, 3, 3, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1]

s = input()
result = sum(score[ord(char) - ord('A')] for char in s)

print("I'm a winner!" if result % 2 else "You're the winner?")
