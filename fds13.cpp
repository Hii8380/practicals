#include <iostream> 
using namespace std; 
 
class Queue { 
public: 
    const static int size = 5;     
    int rear = -1; 
    int front = -1; 
    int queue[size]; 
 
    // Function to place an order 
    void Place_order(int x) { 
        if (front == -1 && rear == -1) { // Queue is empty 
            front = rear = 0; 
            queue[rear] = x; 
        } else if ((rear + 1) % size == front) { // Queue is full 
            cout << "Ooo So Sorry, You Can't order as the orders have reached the maximum." << endl; 
        } else { 
            rear = (rear + 1) % size; // Circular increment 
            queue[rear] = x; 
        } 
    } 
 
    // Function to deliver an order 
    void delivered_order() { 
        if (front == -1 && rear == -1) { // Queue is empty 
            cout << "All the Pizzas are Delivered!!!" << endl; 
        } else { 
            cout << "Delivered Pizza: " << queue[front] << endl; 
            if (front == rear) { // Last element delivered 
                front = rear = -1; // Reset queue 
            } else { 
                front = (front + 1) % size; // Circular increment 
            } 
        } 
    } 
 
    // Function to display all orders 
    void display() { 
        if (front == -1 && rear == -1) { // Queue is empty 
            cout << "No orders placed yet!" << endl; 
            return; 
        } 
 
        cout << "The ordered Pizzas are: "; 
        int i = front; 
        while (true) { 
            cout << queue[i] << " "; 
            if (i == rear) break; // Stop when reaching the last element 
            i = (i + 1) % size; // Circular increment 
        } 
        cout << endl; 
    } 
}; 
 
int main() { 
    Queue q; 
    int choice; 
 
    do { 
        cout << "\n\nWelcome To Pizza Parlor. Enter option number for Order. Enter 0 to exit." << endl; 
        cout << "1. Place an Order" << endl; 
        cout << "2. Display Orders" << endl; 
        cout << "3. Deliver Order" << endl; 
        cout << "0. Exit" << endl; 
         
        cin >> choice; 
 
        switch (choice) { 
            case 0: 
                break; 
            case 1: { 
                int val; 
                cout << "Pizza types: 1. Margherita  2. Paneer  3. Cheese  4. Italian" << endl; 
                cout << "Enter the type of pizza you want to order (1-4): "; 
                cin >> val; 
 
                if (val < 1 || val > 4) { 
                    cout << "Sorry, this pizza type can't be ordered!!" << endl; 
                } else { 
                    cout << "Your ordered pizza " << val << " Placed!!" << endl; 
                    q.Place_order(val); 
                } 
                break; 
            } 
            case 2: 
                q.display(); 
                break; 
            case 3: 
                q.delivered_order(); 
                break; 
            default: 
                cout << "Please enter a valid number!" << endl; 
        } 
    } while (choice != 0); 
 
    return 0; 
} 
