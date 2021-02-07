from wasmite import Module, WasmiteCase, main
from wasmite import FuncType, Function, Global, Value
from wasmite import I32, I64

def sum(x: int, y: int) -> int:
    return x + y

# create a Test class the inherits wasmite.TestWasm
class Test(WasmiteCase):
    # create a variable the hold all the functions from a specific wasm file.
    module = Module("test_wasm.wasm")
    # import python function into WebAssembly (not mandatory)
    # type annotations on the function is necessary 
    module.register("math", {
        "sum": Function(module.store, sum),
        "seven": Global(module.store, Value.i32(7), mutable=True)
    })
    # start up the module (this is mandatory)
    module.start()
    # access exports
    exports = module.exports
    # create any amount of function that test you codes functionality
    def test_add(self):
        # test the "add" function in test.wasm
        result = self.exports.add(1,2)
        self.assertEqual(result, 3) 
        
    def test_sub(self):
        # test the "sub" function in test.wasm
        result = self.exports.sub(2,2) # 2-2 => 0 == 0
        self.assertEqual(result, 0)
        
    def test_sub_notequal(self):
        # test the "sub" function in test.wasm
        result = self.exports.sub(5,2) # 5-2 => 3 != -1
        self.assertNotEqual(result, -1)

    def test_args_add(self):
        # check the types for results and parameter of the function "add"
        # param is I32, I32 and result is I32
        add_function = self.exports.add
        self.checkFunctionTypes(add_function, FuncType([I32, I32], [I32])) # result will fail
        
    def test_import_sum(self):
        # test the use of the import function sum.
        sum_function = self.exports.addsum(5,2)
        self.assertEqual(sum_function, 7)
        
    def test_global_read(self):
        # read value of global
        read_seven = self.exports.read_g()
        self.assertEqual(read_seven, 7) 
        
    def test_global_write(self):
        # write value of global
        self.exports.write_g(5)
        read_seven = self.exports.read_g()
        self.assertEqual(read_seven, 5) 
        
# Hi don't forget to add me         
if __name__ == "__main__":
    main()