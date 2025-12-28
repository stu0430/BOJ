n = int(input())
original = n

bit_count = 0
temp = n
while temp:
    temp //= 2
    bit_count += 1

complement = (1 << 32) - original

result = 0
for i in range(32):
    bit_original = bool(original & (1 << i))
    bit_complement = bool(complement & (1 << i))
    result += bit_original ^ bit_complement

print(result)