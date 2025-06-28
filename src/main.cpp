#include <iostream>

using namespace std;

struct Node {
    int coordinate;
    Node* left;
    Node* right;
};

Node* createNode(int* data){
    Node* newNode = new Node();
    newNode -> coordinate = *data;
    newNode -> left = nullptr;
    newNode -> right = nullptr;
    return newNode;
}

int main() {
    int data[4] = {4, 6, 2, 5};
    int dataSize = sizeof(data)/sizeof(data[0]);
    Node* Nodes[dataSize];
    Nodes[0] = createNode(&data[dataSize/2]); // create root node

    return 0;
}
