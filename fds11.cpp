#include <iostream> 
using namespace std; 
 
class Queue { 
public: 
    const static int size = 10; 
    int rear = -1; 
    int front = -1; 
    int queue[size]; 
 
    // Function to add a job to the queue 
    void enqueue(int x) { 
        if ((rear + 1) % size == front) {  // Check for overflow in circular queue 
            cout << "Overflow!!! Queue is full." << endl; 
        } else { 
            if (front == -1 && rear == -1) {  // Queue is empty 
                front = rear = 0; 
            } else { 
                rear = (rear + 1) % size;  // Move to the next position in a circular manner 
            } 
            queue[rear] = x;  // Add the job 
            cout << "Job " << x << " added to the queue." << endl; 
        } 
    } 
 
    // Function to delete a job from the queue 
    void dequeue() { 
        if (front == -1 && rear == -1) {  // Check for underflow 
            cout << "Underflow!!! Queue is empty." << endl; 
        } else { 
            cout << "The Deleted Job No.: " << queue[front] << endl; 
            if (front == rear) {  // Only one element was present 
                front = rear = -1;  // Reset queue 
            } else { 
                front = (front + 1) % size;  // Move to the next position in a circular manner 
            } 
        } 
    } 
 
    // Function to display the queue 
    void display() { 
        if (front == -1 && rear == -1) {  // Check if queue is empty 
            cout << "Queue is Empty!" << endl; 
        } else { 
            cout << "Queue Contains: "; 
            int i = front; 
            while (true) { 
                cout << queue[i] << " "; 
                if (i == rear) break;  // Stop when reaching the last element 
                i = (i + 1) % size;  // Circular increment 
            } 
            cout << endl; 
        } 
    } 
}; 
 
int main() { 
    Queue job_line; 
    int choice, val; 
 
    do { 
        cout << "Enter the option No. to perform the operations:" << endl; 
        cout << "Note: (Job no. should be in integer type)" << endl; 
        cout << "1. To Add Job" << endl; 
        cout << "2. To Delete Job" << endl; 
        cout << "3. To Display Queue" << endl; 
        cout << "4. Exit" << endl; 
        cin >> choice; 
 
        switch (choice) { 
            case 1: 
                cout << "Enter Job:" << endl; 
                cin >> val; 
                job_line.enqueue(val); 
                break; 
            case 2: 
                job_line.dequeue(); 
                break; 
            case 3: 
                job_line.display(); 
                break; 
            case 4: 
                cout << "Exiting..." << endl; 
                break; 
            default: 
                cout << "Enter valid option:" << endl; 
                break; 
        } 
    } while (choice != 4); 
 
    return 0; 
} 
