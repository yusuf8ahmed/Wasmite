#include <stdio.h>

// emcc test_c.c -o test_c.wasm -s EXPORTED_FUNCTIONS='["_even", "_squared"]'
// functions even and squared are exported ------------^^^^^^^^^^^^^^^^^^^^^

int even(int value){

    if (value % 2 == 0) {
        return 1; // true: 1
    } else {
        return 0; // false: 0
    }
}

int squared(int value){
    return value * value;
}

int main() {
    int number = even(3);
    printf("even(3): %d\n", number);

    int number2 = squared(3);
    printf("squared(3) %d\n", number2);

    return 0;
}