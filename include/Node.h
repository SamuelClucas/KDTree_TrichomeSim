#ifndef KD_TREE_H
#define KD_TREE_H

#include "Node.h"
#include <iostream>
#include <random>
using namespace std;



class KDTree {
private:
    struct Points {
        int x, y, z;
    };
    struct Node {
        Points medianSplit;
        int axis;
        Node *less;
        Node *greater;
    };

public:
    bool compareByX(const Points &a, const Points &b);

    bool compareByY(const Points &a, const Points &b);

    bool compareByZ(const Points &a, const Points &b);

    Node* createNode(Points value, int axis, Node *nodeArray, int *insertionPoint);

    Node* buildTree(Points *p, int start, int end, int axis = 0, Node *nodeArray = nullptr, int *insertionPoint = nullptr);

    int distance3D(Points coordinate, Points query);

    int distance1D(int hyperplane, int query);

    Node* nearest(Node *n, Points query, Node *best);

    Node* makeNodeArray(int num);

    int* makeNodeArrayIndex();
d
    void deleteNodeArray(Node* nodeArray, int* insertionPoint);
};

#endif  // KD_TREE_H
