// test_cpp.wasm
#include <stdio.h>
#include <iostream>
#include <sstream>
#include <emscripten.h>

using namespace std;

// em++ test_cpp.cpp -o test_cpp.wasm -s EXPORTED_FUNCTIONS='["_addone", "_cubed"]'
// functions addone and cubed are exported ------------------^^^^^^^^^^^^^^^^^^^^^                    

extern "C" {

  int addone(int value){
    return value + 1;
  }

  int cubed(int value){
    return value * value * value;
  }

  int main() {
    printf("\n");

    int number = addone(3);
    printf("addone(3): %d\n", number);

    int number2 = cubed(3);
    printf("cubed(3) %d\n", number2);

    return 0;
  }
}

