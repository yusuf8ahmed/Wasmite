from wasmite import WasmiteCase, WatModule
from wasmite import Function, Global, Value, main

def sum(x: int, y: int) -> int:
    return x + y

class Test(WasmiteCase):
    module = WatModule("test_wat.wat")
    module.register("math", {
        "sum": Function(module.store, sum),
        "seven": Global(module.store, Value.i32(7), mutable=True)
    })
    exports = module.get_exports()
    
    def test_add(self):
        # test add function
        add_function = self.exports.add(1,2)
        self.assertEqual(add_function, 3)
        
    def test_sub(self):
        # test sub function
        sub_function = self.exports.sub(1,2)
        self.assertEqual(sub_function, -1)
        
    def test_global_read(self):
        # test reading value of global
        read_seven = self.exports.read_global()
        self.assertEqual(read_seven, 7) 
        
    def test_global_write(self):
        # text writing value of global
        self.exports.write_global(5)
        read_global = self.exports.read_global()
        self.assertEqual(read_global, 5) 

if __name__ == "__main__":
    main()