#include <iostream>
using namespace std;

struct Bstnode {
    int data;
    Bstnode* left;
    Bstnode* right;

    Bstnode(int value) : data(value), left(NULL), right(NULL) {}
};

class Btree {
public:
    Bstnode* root;

    Btree() {
        root = NULL;
    }

    ~Btree() {
        destroyTree(root);
    }

    void destroyTree(Bstnode* temp) {
        if (temp == NULL) return;
        destroyTree(temp->left);
        destroyTree(temp->right);
        delete temp;
    }

    // Insert a node into the tree (no duplicates)
    Bstnode* insert(Bstnode* temp, int in_data) {
        if (temp == NULL) {
            return new Bstnode(in_data);
        }
        if (in_data < temp->data) {
            temp->left = insert(temp->left, in_data);
        } else if (in_data > temp->data) {
            temp->right = insert(temp->right, in_data);
        } else {
            cout << "Duplicate value " << in_data << " not inserted!" << endl;
        }
        return temp;
    }

    void addNode() {
        int value;
        cout << "Enter value to insert into the tree: ";
        cin >> value;
        root = insert(root, value);
        cout << "Node " << value << " inserted successfully!" << endl;
    }

    // Find depth of the tree
    int findDepth(Bstnode* temp) {
        if (temp == NULL) return 0;
        return max(findDepth(temp->left), findDepth(temp->right)) + 1;
    }

    // Find the minimum value in the tree
    int findMinValue(Bstnode* temp) {
        if (temp == NULL) return -1;
        while (temp->left != NULL) {
            temp = temp->left;
        }
        return temp->data;
    }

    void findMin() {
        if (root == NULL) {
            cout << "The tree is empty!" << endl;
        } else {
            cout << "Minimum value in the tree: " << findMinValue(root) << endl;
        }
    }

    // Mirror the tree
    void mirrorTree(Bstnode* temp) {
        if (temp == NULL) return;
        swap(temp->left, temp->right);
        mirrorTree(temp->left);
        mirrorTree(temp->right);
    }

    void mirror() {
        if (root == NULL) {
            cout << "The tree is empty!" << endl;
        } else {
            mirrorTree(root);
            cout << "Tree mirrored successfully!" << endl;
        }
    }

    // Search for a value in the tree
    bool search(Bstnode* temp, int in_data) {
        if (temp == NULL) return false;
        if (temp->data == in_data) return true;
        return search((in_data < temp->data) ? temp->left : temp->right, in_data);
    }

    void searchValue() {
        int value;
        cout << "Enter value to search: ";
        cin >> value;
        if (search(root, value)) {
            cout << "Value " << value << " found in the tree." << endl;
        } else {
            cout << "Value " << value << " not found in the tree." << endl;
        }
    }

    // Inorder traversal
    void inorder(Bstnode* temp) {
        if (temp == NULL) return;
        inorder(temp->left);
        cout << temp->data << " ";
        inorder(temp->right);
    }

    void display() {
        if (root == NULL) {
            cout << "The tree is empty!" << endl;
        } else {
            cout << "Inorder traversal of the tree: ";
            inorder(root);
            cout << endl;
        }
    }
};

int main() {
    Btree tree;
    int choice;

    while (true) {
        cout << "\nMenu:\n"
             << "1. Insert new node\n"
             << "2. Find number of nodes in the longest path (depth)\n"
             << "3. Find minimum data value in the tree\n"
             << "4. Mirror the tree\n"
             << "5. Search for a value\n"
             << "6. Display tree\n"
             << "7. Exit\n"
             << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                tree.addNode();
                break;
            case 2:
                cout << "Tree depth: " << tree.findDepth(tree.root) << endl;
                break;
            case 3:
                tree.findMin();
                break;
            case 4:
                tree.mirror();
                break;
            case 5:
                tree.searchValue();
                break;
            case 6:
                tree.display();
                break;
            case 7:
                cout << "Exiting program!" << endl;
                return 0;
            default:
                cout << "Invalid choice. Please try again!" << endl;
        }
    }
    return 0;
}
