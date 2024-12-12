//min stack will search minimum element in O(1)
#include <stdio.h>
#include <limits.h>
#define MAX_SIZE 100

int stack[MAX_SIZE];
int minStack[MAX_SIZE];
int top=-1;

void push(int value)
{
    if(top==MAX_SIZE-1)
    {
        printf("stack overflow!\n");
        return;
    }
    top++;
    stack[top]=value;

    if(top==0 || value<minStack[top-1])
    {
        minStack[top]=value;
    }
    else
    {
        minStack[top]=minStack[top-1];
    }
    printf("%d push to the stack\n",value);
}

int pop()
{
    if(top==-1)
    {
        printf("stack underflow\n");
        return INT_MIN;
    }
    return stack[top--];
}

int peek()
{
    if(top==-1)
    {
        printf("Stack is empty\n");
        return INT_MIN;
    }
    else
    {
        return stack[top];
    }
}

int getMin()
{
    if(top==-1)
    {
        printf("Stack is empty\n");
        return INT_MIN;
    }
    else
    {
        return minStack[top];
    }
}

void display()
{
    if(top==-1)
    {
        printf("Stack is empty\n");
        return;
    }
    for(int i =top;i>=0;i--)
    {
        printf("Stack value :%d \n",stack[i]);
    }
}

int main()
{
    int choice,val;


    while(1)
    {   printf("\nWhat do u want to do:\n");
        printf("1.push\n");
        printf("2.pop\n");
        printf("3.top element\n");
        printf("4.minimum element\n");
        printf("5.Display all element\n");
        printf("6.exit\n");
        printf("\nEnter ur choice:\n");
        scanf("%d",&choice);
        switch(choice)
        {
        case 1:
            printf("Enter the element u want to push:\n");
            scanf("%d",&val);
            push(val);
            break;
        case 2:
            val=pop();
            if(val!=INT_MIN)
            {   printf("Element popped: %d\n",val);
                break;
            }
            printf("no element to pop\n");
            break;
        case 3:
            val=peek();
            if(val!=INT_MIN)
            {
                printf("Top Element : %d\n",val);
            }

            break;
        case 4:
            val=getMin();
            if(val!=INT_MIN)
                printf("Minimum Element : %d\n",val);
            break;
        case 5:
            display();
            break;
        case 6:
            return 0;
        default:
            printf("invalid choice , try again\n");
            break;
        }
    }
    return 0;
}
