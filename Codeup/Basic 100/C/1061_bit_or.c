// 둘 중 하나라도 1이면 1
#include <stdio.h>
int main() 
{
    int a, b;
    scanf("%d %d", &a, &b);
    printf("%d", a | b);
    return 0;
}