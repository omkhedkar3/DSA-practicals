#include <iostream>
#include <string>
using namespace std;

struct Node {
    string label;
    int ch_count;
    Node* child[10];
};

class GT {
private:
    Node* root;

public:
    GT() {
        root = nullptr;
    }

    void create() {
        root = new Node;
        cout << "Name of the book: ";
        cin >> root->label;

        cout << "Number of chapters: ";
        cin >> root->ch_count;

        for (int i = 0; i < root->ch_count; i++) {
            root->child[i] = new Node;
            cout << "Name of chapter " << i + 1 << ": ";
            cin >> root->child[i]->label;

            cout << "Number of sections: ";
            cin >> root->child[i]->ch_count;

            for (int j = 0; j < root->child[i]->ch_count; j++) {
                root->child[i]->child[j] = new Node;
                cout << "Name of section " << i + 1 << " - " << j + 1 << ": ";
                cin >> root->child[i]->child[j]->label;

                cout << "Number of sub-sections: ";
                cin >> root->child[i]->child[j]->ch_count;

                for (int k = 0; k < root->child[i]->child[j]->ch_count; k++) {
                    root->child[i]->child[j]->child[k] = new Node;
                    cout << "Name of sub-section " << i + 1 << " - " << j + 1 << " - " << k + 1 << ": ";
                    cin >> root->child[i]->child[j]->child[k]->label;
                }
            }
        }
    }

    void display(Node* r) {
        if (r == nullptr) {
            cout << "No book information available.\n";
            return;
        }

        cout << "\nName of Book: " << r->label << endl;
        cout << "Number of Chapters: " << r->ch_count << endl;

        for (int i = 0; i < r->ch_count; i++) {
            cout << "Chapter " << i + 1 << ": " << r->child[i]->label << endl;
            cout << "Number of Sections: " << r->child[i]->ch_count << endl;

            for (int j = 0; j < r->child[i]->ch_count; j++) {
                cout << "  Section " << i + 1 << "-" << j + 1 << ": " << r->child[i]->child[j]->label << endl;
                cout << "  Number of Sub-sections: " << r->child[i]->child[j]->ch_count << endl;

                for (int k = 0; k < r->child[i]->child[j]->ch_count; k++) {
                    cout << "    Sub-section " << i + 1 << "-" << j + 1 << "-" << k + 1
                         << ": " << r->child[i]->child[j]->child[k]->label << endl;
                }
            }
        }
    }

    // Getter function for root
    Node* getRoot() {
        return root;
    }

    ~GT() {
        delete root;
    }
};

int main() {
    GT g;
    int choice;

    while (true) {
        cout << "\n--- MAIN MENU ---" << endl;
        cout << "1 -> Add book info" << endl;
        cout << "2 -> Display info" << endl;
        cout << "3 -> Exit" << endl;
        cout << "Choose an option (1-3): ";
        cin >> choice;

        switch (choice) {
            case 1:
                g.create();
                break;
            case 2:
                g.display(g.getRoot()); // Using getter function
                break;
            case 3:
                cout << "\n// END OF CODE\n";
                exit(0);
                break;
            default:
                cout << "Please choose a valid option (1-3).\n";
                break;
        }
    }

    return 0;
}
