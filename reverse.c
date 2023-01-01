#include<stdio.h>

int main(){
    
    int a,reverse=0,remainder;

    printf("enter the number");
    scanf("%d",&a);

    while(a>0)
    {
        remainder=a%10;
        reverse=reverse*10+remainder;
        a/=10;
    }

    printf("%d",reverse);
    return 0;
}