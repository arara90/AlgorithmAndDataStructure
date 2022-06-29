// xor(^): 다르면 참
// 두장의 이미지가 겹친 부분만 처리할 때

#include <stdio.h>
int main() 
{
    int a, b;
    scanf("%d %d", &a, &b);
    printf("%d", a ^ b);
    return 0;
}