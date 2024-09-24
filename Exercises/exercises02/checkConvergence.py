sum = 0
i = 0
n = 10000

while i <= n:
    sum += 1/2**i
    i += 1
print(f"1 + 1/2 + ... + 1/2**n converges to {sum}")

sum = 0
i = 0

while i <= n:
    sum += (-1)**i/(2*i+1)
    i += 1
print(f"1 - 1/3 + 1/5 + ... (-1)**n / (2*n+1) converges to {round(sum, 3)}")

# don't know how to format it with like latex, or if this is sufficient.