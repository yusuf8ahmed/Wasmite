from wasmite import Module, WasmiteCase
from wasmite import Function, Global, Value, main

def sum(x: int, y: int) -> int:
    return x + y

class Test(WasmiteCase):
    module = Module("test_wat.wat")
    module.register("math", {
        "sum": Function(module.store, sum),
        "seven": Global(module.store, Value.i32(7), mutable=True)
    })
    module.start()
    exports = module.exports
    
    def test_add(self):
        add_function = self.exports.add(1,2)
        self.assertEqual(add_function, 3)
        
    def test_sub(self):
        sub_function = self.exports.sub(1,2)
        self.assertEqual(sub_function, -1)
        
    def test_global_read(self):
        # read value of global
        read_seven = self.exports.read_g()
        self.assertEqual(read_seven, 7) 
        
    def test_global_write(self):
        # write value of global
        self.exports.write_g(5)
        read_seven = self.exports.read_g()
        self.assertEqual(read_seven, 5) 

        
if __name__ == "__main__":
    main()