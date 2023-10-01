#include <iostream>

bool isPrime(int n) {
    if (n <= 1) {
        return false; 
    }
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true; 
}

void primeNumbers(int n) {
    for (int i = 2; i <= n; i++) {
        if (isPrime(i)) {
            std::cout << i << " ";
        }
    }
}

int main() {
    int n;
    std::cout << "Enter the No upto which to print Prime Number:";
    std::cin >> n;
    primeNumbers(n);
    return 0;
}

