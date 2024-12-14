#include <iostream>
using namespace std;

#define MAX_SIZE 5  // Maximum size of the deque

class Deque {
private:
    int arr[MAX_SIZE];  // Array to store elements of the deque
    int front;          // Pointer to the front of the deque
    int rear;           // Pointer to the rear of the deque
    int size;           // Current size of the deque

public:
    // Constructor to initialize the deque
    Deque() {
        front = -1;
        rear = -1;
        size = 0;
    }

    // Function to check if the deque is full
    bool isFull() {
        return size == MAX_SIZE;
    }

    // Function to check if the deque is empty
    bool isEmpty() {
        return size == 0;
    }

    // Function to add an element to the front
    void addFront(int element) {
        if (isFull()) {
            cout << "Deque is full. Cannot add element at the front." << endl;
            return;
        }
        if (front == -1) {  // Deque is empty
            front = rear = 0;
        } else {
            front = (front - 1 + MAX_SIZE) % MAX_SIZE;  // Circular move
        }
        arr[front] = element;
        size++;
        cout << "Added " << element << " to the front." << endl;
    }

    // Function to add an element to the rear
    void addRear(int element) {
        if (isFull()) {
            cout << "Deque is full. Cannot add element at the rear." << endl;
            return;
        }
        if (rear == -1) {  // Deque is empty
            front = rear = 0;
        } else {
            rear = (rear + 1) % MAX_SIZE;  // Circular move
        }
        arr[rear] = element;
        size++;
        cout << "Added " << element << " to the rear." << endl;
    }

    // Function to delete an element from the front
    void deleteFront() {
        if (isEmpty()) {
            cout << "Deque is empty. Cannot delete element from the front." << endl;
            return;
        }
        cout << "Deleted " << arr[front] << " from the front." << endl;
        if (front == rear) {  // Only one element in the deque
            front = rear = -1;
        } else {
            front = (front + 1) % MAX_SIZE;  // Circular move
        }
        size--;
    }

    // Function to delete an element from the rear
    void deleteRear() {
        if (isEmpty()) {
            cout << "Deque is empty. Cannot delete element from the rear." << endl;
            return;
        }
        cout << "Deleted " << arr[rear] << " from the rear." << endl;
        if (front == rear) {  // Only one element in the deque
            front = rear = -1;
        } else {
            rear = (rear - 1 + MAX_SIZE) % MAX_SIZE;  // Circular move
        }
        size--;
    }

    // Function to display all elements of the deque
    void display() {
        if (isEmpty()) {
            cout << "Deque is empty." << endl;
            return;
        }
        cout << "Deque elements: ";
        int i = front;
        while (i != rear) {
            cout << arr[i] << " ";
            i = (i + 1) % MAX_SIZE;
        }
        cout << arr[rear] << endl;  // Display the last element
    }
};

int main() {
    Deque dq;

    // Operations on the deque
    dq.addRear(10);    // Add to rear: 10
    dq.addRear(20);    // Add to rear: 20
    dq.addFront(5);    // Add to front: 5
    dq.addRear(30);    // Add to rear: 30
    dq.addFront(2);    // Add to front: 2
    dq.display();      // Display: 2 5 10 20 30

    dq.deleteFront();  // Delete from front: 2
    dq.deleteRear();   // Delete from rear: 30
    dq.display();      // Display: 5 10 20

    dq.addFront(15);   // Add to front: 15
    dq.addRear(25);    // Add to rear: 25
    dq.display();      // Display: 15 5 10 20 25

    dq.deleteFront();  // Delete from front: 15
    dq.deleteRear();   // Delete from rear: 25
    dq.display();      // Display: 5 10 20

    return 0;
}

