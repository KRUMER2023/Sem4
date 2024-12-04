#include<stdio.h>

void main()
{

    int a=24,b=8,n=a;
    while(n%b!=0)
    {
        n=n+a;
    }
    printf("lcm : %d",n);

    /*
    int a=8,b=6,n=1;
    int max;
    if(a<b)
        max=b;
    else
        max=a;
    //printf("%d",max);

    printf("lcm : %d",n);*/

}
