import math

def largest_prime_factor(n):
    # ابتدا همه عوامل 2 را حذف کن
    while n % 2 == 0:
        max_prime = 2
        n //= 2

    # بررسی اعداد فرد از 3 تا ریشه دوم n
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            max_prime = i
            n //= i  # حذف عامل i از n

    # اگر بعد از تقسیم‌ها n هنوز عددی بزرگ‌تر از 2 باشد، آن خودش یک عدد اول است.
    if n > 2:
        max_prime = n

    return max_prime

x = 600851475143
print("Largest prime factor:", largest_prime_factor(x))
    