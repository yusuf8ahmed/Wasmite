from wasmite import WasmiteCase, WasmModule
from wasmite import FunctionTypes, Function, Global, Value, main
from wasmite import I32, I64

def sum(x: int, y: int) -> int:
    """ python function to be imported into WASM  """
    return x + y

class Test(WasmiteCase):
    # create a variable the hold all the functions from a specific wasm file.
    module = WasmModule("test_wasm.wasm")
    # import python function into WASM 
    # type annotations on the function is necessary 
    module.register("math", {
        "sum": Function(module.store, sum),
        "seven": Global(module.store, Value.i32(7), mutable=True)
    })
    # start up the module and return the exports (this is mandatory)
    exports = module.get_exports()
    
    def test_add(self):
        # test add function
        result = self.exports.add(1,2)
        self.assertEqual(result, 3) 
        
    def test_sub(self):
        # test the sub function
        result = self.exports.sub(2,2)
        self.assertEqual(result, 0)

    def test_args_add(self):
        # check the types for results and parameter of the function "add"
        # param is I32, I32 and result is I32
        add_function = self.exports.add
        self.assertTypes(add_function, FunctionTypes([I32, I32], [I32])) #
        
    def test_import_sum(self):
        # test the imported python function sum.
        sum_function = self.exports.addsum(5,2)
        self.assertEqual(sum_function, 7)
        
    def test_global_read(self):
        # test reading value of global
        read_seven = self.exports.read_global()
        self.assertEqual(read_seven, 7) 
        
    def test_global_write(self):
        # test writing value of global
        self.exports.write_global(5)
        read_seven = self.exports.read_global()
        self.assertEqual(read_seven, 5) 
        
# Hi don't forget to add me         
if __name__ == "__main__":
    main()