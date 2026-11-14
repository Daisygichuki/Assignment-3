#include <stdio.h>
#define MAX 5

int deque[MAX];
int front = 0, rear = -1, count = 0;

int isFull()  { return count == MAX; }
int isEmpty() { return count == 0; }

/* (a) Front insertion */
void insertFront(int x) {
    if (isFull()) {
        printf("Deque Overflow\n");
        return;
    }
    front = (front - 1 + MAX) % MAX;   /* move front back, wrapping */
    deque[front] = x;
    if (count == 0)
        rear = front;                  /* first element is both ends */
    count++;
}

/* (b) Rear insertion */
void insertRear(int x) {
    if (isFull()) {
        printf("Deque Overflow\n");
        return;
    }
    rear = (rear + 1) % MAX;           /* move rear forward, wrapping */
    deque[rear] = x;
    count++;
}

/* (c) Front deletion */
int deleteFront() {
    if (isEmpty()) {
        printf("Deque Underflow\n");
        return -1;
    }
    int x = deque[front];
    front = (front + 1) % MAX;
    count--;
    return x;
}

/* (d) Rear deletion */
int deleteRear() {
    if (isEmpty()) {
        printf("Deque Underflow\n");
        return -1;
    }
    int x = deque[rear];
    rear = (rear - 1 + MAX) % MAX;
    count--;
    return x;
}

void display() {
    if (isEmpty()) { printf("Deque is empty\n"); return; }
    for (int i = 0, idx = front; i < count; i++, idx = (idx + 1) % MAX)
        printf("%d ", deque[idx]);
    printf("\n");
}

int main() {
    insertRear(10);  insertRear(20);   
    insertFront(5);                    
    insertFront(1);                    
    display();
    printf("Deleted front: %d\n", deleteFront());  /* 1  */
    printf("Deleted rear : %d\n", deleteRear());   /* 20 */
    display();                         /* 5 10           */
    return 0;
}