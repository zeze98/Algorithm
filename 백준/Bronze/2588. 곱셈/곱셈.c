#include <stdio.h>

int main()
{
    int A, B;
    int a, b, c;

    scanf("%d",&A);
    scanf("%d",&B);

    a = B % 10;
    c = B / 100;
    b = (B - (c * 100) - a)/10;

    printf("%d\n", A * a);
    printf("%d\n", A * b);
    printf("%d\n", A * c);
    printf("%d\n", A * B);
    return 0;
}
