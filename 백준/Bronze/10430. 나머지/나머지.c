#include <stdio.h>

int main()
{
	int A, B, C;
    int a,b,c,d;

	scanf("%d", &A);
	scanf("%d", &B);
	scanf("%d", &C);

	a = (A+B)%C ;
	b = ((A%C) + (B%C))%C ;
	c = (A*B)%C ;
	d = ((A%C) * (B%C))%C ;

	printf("%d\n", a);
	printf("%d\n", b);
	printf("%d\n", c);
	printf("%d\n", d);

    return 0;
}
