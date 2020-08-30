a, b = map(int, input().strip().split(' '))
print(a + b)

#나의 답
print(a//b, a%b)

# divmod와 unpacking
print(*divmod(a, b))
#divmod는 작은 숫자를 다룰 때는 a//b, a%b 보다 느립니다. 대신, 큰 숫자를 다룰 때는 전자가 후자보다 더 빠르지요.

print(divmod(a, b), type divmod(a, b)) #(1, 2) <class 'tuple'>