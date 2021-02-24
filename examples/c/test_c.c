#include <stdio.h>

// emcc test_c.c -o test_c.wasm -s EXPORTED_FUNCTIONS='["_even", "_squared", "_inverse"]'
// functions even and squared are exported ------------^^^^^^^^^^^^^^^^^^^^^

int even(int value){
    if (value % 2 == 0) {
        return 1;
    } else {
        return 0;
    }
}

int squared(int value){
    return value * value;
}

float inverse(float number){
	long i;
	float x2, y;
	const float threehalfs = 1.5F;

	x2 = number * 0.5F;
	y  = number;
	i  = * ( long * ) &y;    
	i  = 0x5f3759df - ( i >> 1 );  
	y  = * ( float * ) &i;
	y  = y * ( threehalfs - ( x2 * y * y ) );

	return y;
}

int main() {
    printf("\n");

    float number = inverse(3.5);
    printf("inverse(3.5) %f\n", number);

    int number1 = even(3);
    printf("even(3): %d\n", number1);

    int number2 = squared(3);
    printf("squared(3) %d\n", number2);

    return 0;
}