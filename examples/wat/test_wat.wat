;; test.wat is the same as test.wasm

(module
  (import "math" "sum" (func $sum (param i32 i32) (result i32)))
  (import "math" "seven" (global $seven (mut i32)))
  (func (export "read_g") (result i32)
    global.get $seven)
  (func (export "write_g") (param $lhs i32)
    get_local $lhs
    global.set $seven)
  (type $t0 (func (param i32 i32) (result i32)))
  (func $add (export "add") (type $t0) (param $lhs i32) (param $rhs i32) (result i32)
    get_local $lhs
    get_local $rhs
    i32.add)
  (func $sub (export "sub") (type $t0) (param $lhs i32) (param $rhs i32) (result i32)
    get_local $lhs
    get_local $rhs
    i32.sub)
  (func $addsum (export "addsum") (param $lhs i32) (param $rhs i32) (result i32)
    get_local $lhs
    get_local $rhs
    call $sum)
)
