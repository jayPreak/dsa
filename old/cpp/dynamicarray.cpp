#include <iostream>
using namespace std;

int main() {
    int x, n;

    cout << "Enter number of item: \n";
    cin >> n;

    int *arr = new int(n);

    cout << "Enter " << n << " elements " << endl;

    for (x=0; x<n; x++) {
        cin >> arr[x];
    }

    cout << "you entered: \n";

    for (x=0; x<n; x++) {
        cout << arr[x] << " ";
    }

    return 0;
}