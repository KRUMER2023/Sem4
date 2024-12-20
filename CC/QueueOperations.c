#include <stdio.h>
#define MAX 50

int queue_array[MAX];
int rear = -1;
int front = -1;

void enqueue(int add_item)
{
    if (rear == MAX - 1)
    {
        printf("Queue Overflow\n");
    }
    else
    {
        if (front == -1)
        {
            front = 0;
        }
        rear = rear + 1;
        queue_array[rear] = add_item;
    }
}

void dequeue()
{
    if (front == -1 || front > rear)
    {
        printf("Queue Underflow\n");
        return;
    }
    else
    {
        printf("Element deleted from queue is: %d\n", queue_array[front]);
        front = front + 1;
    }
}
void display()
{
    int i;
    if (front == -1)
    {
        printf("Queue is empty\n");
    }
    else
    {
        printf("Queue is: \n");
        for (i = front; i <= rear; i++)
        {
            printf("%d ", queue_array[i]);
        }
        printf("\n");
    }
}



int main()
{
    enqueue(10);
    enqueue(20);
    enqueue(30);
    enqueue(40);
    display();

    dequeue();
    dequeue();
    display();
}
