#include<iostream>
using namespace std;

class Node{
    public:
    int value;
    Node* next;
    Node* previous;
};

int main()
{
    Node* node = new Node();    
    cin.get();
    printf("%d", node->value);
}