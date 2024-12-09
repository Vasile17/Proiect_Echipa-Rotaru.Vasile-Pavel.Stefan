 #include <iostream>
using namespace std;

// Definirea structurii unui nod de arbore binar
struct Node {
    int data;       // Valoarea stocată în nod
    Node* left;     // Pointer către subarborele stâng
    Node* right;    // Pointer către subarborele drept

    // Constructor pentru a inițializa un nod
    Node(int val) {
        data = val;
        left = right = nullptr;
    }
};

// Funcție pentru a insera un element într-un arbore binar de căutare
Node* insert(Node* root, int val) {
    // Dacă arborele este gol, creăm un nou nod
    if (root == nullptr) {
        return new Node(val);
    }

    // Dacă valoarea este mai mică decât valoarea curentă a nodului,
    // mergem în subarborele stâng
    if (val < root->data) {
        root->left = insert(root->left, val);
    }
    // Dacă valoarea este mai mare sau egală, mergem în subarborele drept
    else {
        root->right = insert(root->right, val);
    }

    return root;
}

// Funcție pentru a efectua o traversare în ordine (in-order traversal)
// Aceasta va returna elementele în ordine crescătoare
void inOrderTraversal(Node* root) {
    if (root != nullptr) {
        // Traversăm subarborele stâng
        inOrderTraversal(root->left);

        // Afișăm valoarea curentă
        cout << root->data << " ";

        // Traversăm subarborele drept
        inOrderTraversal(root->right);
    }
}

// Funcție pentru a sorta un vector folosind BTS
void BTSort(int arr[], int n) {
    // Creăm un arbore binar de căutare gol
    Node* root = nullptr;

    // Inserăm toate elementele în arbore
    for (int i = 0; i < n; i++) {
        root = insert(root, arr[i]);
    }

    // Realizăm o traversare in-order a arborelui pentru a obține elementele sortate
    cout << "Vectorul sortat folosind BTS: ";
    inOrderTraversal(root);
    cout << endl;
}

int main() {
    // Exemplu de vector de numere
    int arr[] = { 7, 3, 5, 2, 8, 4, 6, 1 };
    int n = sizeof(arr) / sizeof(arr[0]);

    // Apelăm funcția BTSort pentru a sorta vectorul
    BTSort(arr, n);

    return 0;
}
