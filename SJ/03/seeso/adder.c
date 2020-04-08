#include <stdio.h>

int main(void)
{
    int x;
    int y;
    printf("Give me an integer: \n");
    scanf("%d", &x);
    getchar();
    printf("Give me another integer: ");
    scanf("%d",&y);
    getchar();
    printf("The sum of %d and %d is %d\n", x,y,x+y);
}