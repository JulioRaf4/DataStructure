#include <iostream>
using namespace std;

class Node
{
public:
    int value;
    Node *next;
    Node *previous;
};

void printForward(Node*head) {
    Node* traverse = head;
    while(traverse != nullptr) {
        cout << traverse->value<<endl;
        traverse = traverse->next;
    }
}

void printBackward(Node*tail) {
    Node* traverse = tail;
    while(traverse != nullptr) {
        cout << traverse->value<<endl;
        traverse = traverse->previous;
    }
}

int main() {
    Node *head;
    Node *tail;

    Node *node = new Node();
    node->value = 4;
    node->next = nullptr;
    node->previous = nullptr;
    head = node;
    tail = node;

    node = new Node();
    node->value = 5;
    node->next = nullptr;
    node->previous = tail;
    tail->next = node;
    tail = node;
    
    node = new Node();
    node->value = 6;
    node->next = nullptr;
    node->previous = tail;
    tail->next = node;
    tail = node;
    
    node = new Node();
    node->value = 7;
    node->next = nullptr;
    node->previous = tail;
    tail->next = node;
    tail = node;

    printBackward(tail);

    cin.get();
}