#include <iostream>
using namespace std;

// Funcție care returnează un întreg și face heapify subarborele cu rădăcina la indicele i
int heapify(int arr[], int n, int i) {
    int largest = i;  // Inițial presupunem că rădăcina este cel mai mare
    int left = 2 * i + 1;  // Indicele copilului stâng
    int right = 2 * i + 2; // Indicele copilului drept

    // Verificăm dacă copilul stâng există și este mai mare decât rădăcina
    if (left < n && arr[left] > arr[largest])
        largest = left;

    // Verificăm dacă copilul drept există și este mai mare decât rădăcina (sau copilul stâng)
    if (right < n && arr[right] > arr[largest])
        largest = right;

    // Dacă rădăcina nu este cel mai mare, schimbăm cu cel mai mare dintre copii
    if (largest != i) {
        swap(arr[i], arr[largest]);

        // Aplicați heapify pe subarborele modificat
        return heapify(arr, n, largest);
    }

    return i; // Rădăcina este deja corectă
}

// Funcție care returnează un întreg și sortează array-ul folosind Heap Sort
int* heapSort(int arr[], int n) {
    // Construim heap-ul (să facem heapify de la mijlocul array-ului spre început)
    for (int i = n / 2 - 1; i >= 0; i--) {
        heapify(arr, n, i);
    }

    // Extragem elemente din heap unul câte unul
    for (int i = n - 1; i > 0; i--) {
        // Mutăm elementul curent (cel mai mare) la sfârșitul array-ului
        swap(arr[0], arr[i]);

        // Aplica heapify pe subarborele care nu este sortat
        heapify(arr, i, 0);
    }

    return arr; // Returnăm array-ul sortat
}

// Funcție pentru a imprima array-ul
void pr

