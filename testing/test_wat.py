import wasmite

class Test(wasmite.TestWat):
    exports = wasmite.wat_module("test.wat")
    
    def test_add(self):
        result = self.exports.add(1,2)
        self.assertEqual(result, 3)
        
    def test_sub(self):
        result = self.exports.sub(1,2)
        self.assertEqual(result, -1)
        
if __name__ == "__main__":
    wasmite.main()