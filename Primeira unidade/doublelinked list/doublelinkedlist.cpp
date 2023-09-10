#include <iostream>
using namespace std;

class Node
{
public:
    int value;
    Node *next;
    Node *previous;
};

void printForward(Node *head)
{
    Node *traverse = head;
    while (traverse != nullptr)
    {
        cout << traverse->value << endl;
        traverse = traverse->next;
    }
}
 //test
void printBackward(Node *tail)
{
    Node *traverse = tail;
    while (traverse != nullptr)
    {
        cout << traverse->value << endl;
        traverse = traverse->previous;
    }
}

void insertAtBeginning(Node *&head, int value)
{
    Node *newNode = new Node;
    newNode->value = value;
    newNode->next = head;
    newNode->previous = nullptr;
    if (head != nullptr)
    {
        head->previous = newNode;
    }
    head = newNode;
}

void insertAtEnd(Node *&tail, int value)
{
    Node *newNode = new Node;
    newNode->value = value;
    newNode->next = nullptr;
    newNode->previous = tail;
    if (tail != nullptr)
    {
        tail->next = newNode;
    }
    tail = newNode;
}

int main()
{
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

    insertAtBeginning(head, 99);
    insertAtEnd(tail, 55);
    printForward(head);
    cin.get();
}