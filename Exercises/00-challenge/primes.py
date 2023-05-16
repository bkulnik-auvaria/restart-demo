

def is_prime(n):
    for k in range(2, n):
        if n % k == 0:          # 2, 4, 6, 8, ...
            return False
    return True


# Check all numbers from 1 to 250
primes = []
for i in range(2, 251):              # 2,3,4,5,...,250
    if is_prime(i) == True:
        primes.append(i)


primes_converted_to_string = [f"{p}\n" for p in primes]

with open("primes_data.txt", "w") as f:         # open file in writing mode and create a file stream "f"
    f.writelines(primes_converted_to_string)



