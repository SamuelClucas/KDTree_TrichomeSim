//
// Created by Sam Clucas on 17/07/2023.
//

#include "Node.h"
#include <iostream>
#include <random>
using namespace std;

static bool Node::compareByX(const Points& a, const Points& b){
    return a.x < b.x;
}
static bool Node::compareByY(const Points& a, const Points& b){
    return a.y < b.y;
}
static bool Node::compareByZ(const Points& a, const Points& b){
    return a.z < b.z;
}

Node* Node::createNode(Points value, int axis, Node* nodeArray, int* insertionPoint){
    nodeArray[*insertionPoint].medianSplit = value;
    nodeArray[*insertionPoint].axis = axis;
    nodeArray[*insertionPoint].less = nullptr;
    nodeArray[*insertionPoint].greater = nullptr;
    return nodeArray + *insertionPoint;
}

Node* Node::buildTree( Points* p, int start, int end, int axis = 0, Node* nodeArray = nullptr, int* insertionPoint = nullptr){
    //base case
    if (start > end){
        return nullptr;
    }

    switch (axis){  // sort on axis
        case 0:
            sort(p + start, p + end, compareByX);
            break;
        case 1:
            sort(p + start, p + end, compareByY);
            break;
        case 2:
            sort(p + start, p + end, compareByZ);
            break;
    }

    int medianIndex =  (start + end)/2;
    Points medianPoint = p[medianIndex];

    Node* root = createNode(medianPoint, axis, nodeArray, insertionPoint);
    (*insertionPoint)++;
    root -> less = buildTree(p, start, medianIndex - 1, (axis + 1) % 3, nodeArray, insertionPoint); // recursively build left and right subtrees where parent node less and greater pointers act as the tree "root"
    (*insertionPoint)++;
    root -> greater = buildTree(p, medianIndex + 1, end, (axis + 1) % 3, nodeArray, insertionPoint);
    (*insertionPoint)++;
    return root;
}

static int Node::distance3D(Points coordinate, Points query){
    int SED = pow(Coordinate.x - query.x, 2) + pow(Coordinate.y - query.y, 2) + pow(Coordinate.z - query.z, 2);
    return SED;
}

static int Node::distance1D(int hyperplane, int query){
    int SED = pow(hyperplane - query, 2);
    return SED;
}

Node* Node::nearest(Node* n, Points query, Node* best) {
    if (n == nullptr) {
        return best;
    }
    if (distance3D(query, n->medianSplit) <= distance3D(query, best->medianSplit)) {
        best = n;
    }

    switch (n->axis) {
        case 0: // x axis
            if (query.x < n->medianSplit.x) {
                Node* favourableSide = n->less;
                Node* unlikelySide = n->greater;
                best = nearest(favourableSide, query, best);
                if (distance1D(query.x, n -> medianSplit.x) <= distance3D(query,best -> medianSplit)){
                    best = nearest(unlikelySide, query, best);
                }
            }
            else {
                Node* favourableSide = n->greater;
                Node* unlikelySide = n->less;
                best = nearest(favourableSide, query, best);
                if (distance1D(query.x, n -> medianSplit.x) <= distance3D(query, best -> medianSplit)){
                    best = nearest(unlikelySide, query, best);
                }
            }
            break;
        case 1: // y axis
            if (query.y < n->medianSplit.y) {
                Node* favourableSide = n->less;
                Node* unlikelySide = n->greater;
                best = nearest(favourableSide, query, best);
                if (distance1D(query.y, n -> medianSplit.y) <= distance3D(query, best -> medianSplit)){
                    best = nearest(unlikelySide, query, best);
                }

            }
            else {
                Node* favourableSide = n->greater;
                Node* unlikelySide = n->less;
                best = nearest(favourableSide, query, best);
                if (distance1D(query.y, n -> medianSplit.y) <= distance3D(query, best -> medianSplit)){
                    best = nearest(unlikelySide, query, best);
                }
            }
            break;
        case 2: // z axis
            if (query.z < n->medianSplit.z) {
                Node* favourableSide = n->less;
                Node* unlikelySide = n->greater;
                best = nearest(favourableSide, query, best);
                if (distance1D(query.z, n -> medianSplit.z) <= distance3D(query, best -> medianSplit)){
                    best = nearest(unlikelySide, query, best);
                }

            }
            else {
                Node* favourableSide = n->greater;
                Node* unlikelySide = n->less;
                best = nearest(favourableSide, query, best);
                if (distance1D(query.z, n -> medianSplit.z) <= distance3D(query, best -> medianSplit)){
                    best = nearest(unlikelySide, query, best);
                }
            }
            break;
    }

    return best;
}

Node* Node::makeNodeArray(int numpoints){
    Node* nodeArray = new Node[numpoints];
}

static int* Node::makeNodeArrayIndex(){
    int* insertionPoint = new int(0);
    return insertionPoint;
}

void Node::deleteNodeArray(Node* nodeArray, int* insertionPoint){
    delete[] nodeArray;
    delete insertionPoint;
}