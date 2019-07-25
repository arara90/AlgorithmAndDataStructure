# 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.
# 1) X가 3으로 나누어 떨어지면, 3으로 나눈다.
# 2) X가 2로 나누어 떨어지면, 2로 나눈다.
# 3) 1을 뺀다.
#
# 문제)
# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다.
# 연산을 사용하는 횟수의 최솟값을 출력하시오.
#
# 입력)
# 첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 정수 N이 주어진다.
#
# 출력)
# 첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.

#####################################
# 1) 3으로 나뉘는지 확인
#     -> 나눈 값 임시 저장
#     -> X-1을 한 숫자의 연산 갯수가 더 적으면 해당 숫자를 이용
#
# 2) 2으로 나뉘는지 확인
#     -> 나눈 값 임시 저장
#     -> X-1을 한 숫자의 연산 갯수가 더 적으면 해당 숫자를 이용
#
# 3) -1 한다

#### 거의 다 왔는데... 시간 초과! (1시간)
####################################
def make1(x):
    print('   x:  ' , x, type(x))

    if x == 1 :
        print('1 : ', x, type(x))
        return 0

    elif dp[x] != 0:
        print('dp[x] != 0:', dp[x])
        return dp[x]

    else :
        # 1) 3으로 나누기
        if x % 3 == 0 :
            print('x/3')
            tmp1 = make1(int(x/3)) + 1
            tmp2 = make1(x-1) + 1
            if tmp1 > tmp2:
                dp[x] = tmp2
            else :
                dp[x] = tmp1

        elif x % 2 == 0:
            print('3 : ',x, type(x))
            tmp1 = make1(int(x/2))
            tmp2 = make1(x-1)

            if tmp1 > tmp2 :
                dp[x] = tmp2 + 1
            else:
                dp[x] = tmp1 + 1

        else :
            dp[x] = make1(x-1) + 1

        return dp[x]

number = int(input())
# 초기화
dp = list( 0 for _ in range(number+1) )
test = list( i for i in range(0,number+1) )
dp[0] = 0
dp[1] = 0

print(dp)
print(make1(number))
print(test)
print(dp)





###################3
# #include<stdio.h>
# #define MAX 987654321
# #define Min(a,b) (a < b ? a : b)
# int DP[1000001];
# int Solve(int x){
#     if(x==1) // x가 1이면 0 리턴
#         return 0;
#     if(DP[x]!=0) 이미 계산 되었다면 바로 리턴
#         return DP[x];
#     int ret = MAX;
#     if(x%3==0){ // 3으로 나누어 떨어지는 경우
#         ret = Min(ret, Solve(x/3) + 1);
#     }
#     if(x%2==0){ // 2로 나누어 떨어지는 경우
#         ret = Min(ret, Solve(x/2) + 1);
#     }
#     ret = Min(ret, Solve(x-1) + 1); // 모든 경우
#     return DP[x] = ret;
# }
# int main(){
#     int n;
#     scanf("%d",&n);
#     printf("%d\n",Solve(n));
# }


