Go
===

Type
---
* golang is very serious about variable types
  * `var x int = 1`
  * `y := x` the compiler infers **new** variable y's type 
    * which is the same as `x`'s
  * all cast must be explicit (unlike C++)
* constant `const x = 1.1`
* define your own `type` 
```
type MyFloat float64
type Person struct {
	name string
	age int
}
```

Function 
---
  * `func needInt(x int) int { return x*10 + 1 }`
  * `func needInt(x int) (int, int) { return 1, 2 }`
  * bind the return variable  
```go
  func needInt(x int) (x, y int) {
    x++
    y += x
    return
  }
```
  * closure `adder` is bound to its own variable `sum`
```go
func adder() func(int) int {
	sum := 0
	return func(x int) int {
		sum += x
		return sum
	}
}
x = adder() // sum == 0 now
x(1) // sum == 1 now
x(2) // sum == 3 now 
```

Method
---
* no class in Go ! 
* a method is a function with a receiver
```go
// Abs() has v as its receiver
func (v Vertex) Abs() float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
} 
```
* Use **pointer receiver** to support modification
  * motivation? this is a way for access level (like private/public in C++)
```go
func (v *Vertex) Scale(f float64) {
	v.X = v.X * f
	v.Y = v.Y * f
}
```

Interface
---
* interface is a set of methods 
* a type implements an interface whose method uses it as the receiver   
```go
type I interface {
	M()
}

// interface I holds the concrete type string 
func (s string) M() { /* whatever */ }

// create interface value which holds type string 
var i I = string("hello") 
i.M()
```
* `var i I interface{} = "hello"`
  * creates an interface value `i`
  * and `i` holds the concrete type string
* `t, ok := i.(T)` checks if interface value `i` holds a `T`
  * `ok == true` if yes; otherwise, `ok == false` 
  * `t` becomes the underlying value if yes
* Polymorphism for an interface value `i`
```go
switch v := i.(type) {
  case T: ...
  case S: ... 
```
  * for example, every type can have its own way to print if
    * interface `Stringer`'s method `String() string` holds this type
    * `func (t SomeType) String() string { return <string of t> }`

Logic
---
* one extra statement before the if condition
```go
if v := math.Pow(x, n); v < lim {
  return v
}
// v is only in the scope of the if condition
```
* for loop can ignore end condition `for { /* forever */ }`
* `switch` automatically add `break` for every `case` (unlike C++)

`defer`
---
* function executes after the current function returns 
* `defer` functions are pushed to a stack
  * their executions order is the opposite

Pointer
---
* no pointer ops
* 
``` 
type Vertex struct {
  X, Y int
}
p := &Vertex{1, 2} // p is a pointer 
p.X = 100 
```

Array
---
* `var a [2]string`
* `primes := [6]int{2, 3, 5, 7, 11, 13}`
* `var s []int = primes[1:4]`
* slices are like Python, `a := names[0:2]`  
  * `a` is a **reference** of the array
  * `len(a)` is length of slice
  * `cap(a)` is the allocated memory starting from `a[0]` 
* slice `x == nil` if `len(x) == 0`  
* create slice `a := make([]int, 5)`  
* slice of slices
```
	board := [][]string{
		[]string{"_", "_", "_"},
		[]string{"_", "_", "_"},
		[]string{"_", "_", "_"},
	}
``` 
* `range` iterates through (index, value) pairs, like Python's `enumerate()` 
  * `for i := range pow { /* index i*/ } ` 
  * `for i, val := range pow { /* index i*/ } ` 
  
Map
---
* `var m map[<key type>]<value type>`
* Insert by `m[key] = value` 
* Obtain value by `value = m[key]`
  * Check exist by `val, exit = m[key]`
  * `exit == false` if `key` is not in `m` 
* Remove by `delete(m, key)`
