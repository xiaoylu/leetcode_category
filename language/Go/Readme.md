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
* there is no class in Go
* a method is a function with a receiver
```go
// Abs() has v as its receiver
func (v Vertex) Abs() float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
} 
```

* Use **pointer receiver** to allow modification
```go
func (v *Vertex) Scale(f float64) {
	v.X = v.X * f
	v.Y = v.Y * f
}
```

Interface
---
* interface is **a set of methods**
* interface value == interface + value
* when a type implements an interface 
  * this interface value holds a value of this **type**
  * `var i I interface{} = "hello"`

```go
type I interface {
	M()
}

// we can say: interface `I` holds the concrete type string 
// or: M() has a receiver of type string 
func (s string) M() { /* whatever */ }

// create an interface value
var i I = string("hello") 
// we will be able to call the method
i.M()
```
* `var i I interface{} = "hello"`
  * it creates an interface value `i`
  * and this `i` holds the concrete type string "hello"
* an interface can hold many different types
* `t, ok := i.(T)` checks if interface value `i` holds a type `T`
  * `ok == true` if yes; otherwise, `ok == false` 
  * `t` will be the underlying value if yes
* an interface value `i` provides Polymorphism 
  * an interface value can be associated with different types
  * each type can implement the interface in different ways

```go
func do(i interface{}) {
  switch v := i.(type) {
    case T: ...
    case S: ... 
    default: ...
  }
}
```
* for example, every type can have its own way to print if
  * interface `Stringer`'s method `String() string` holds this type
  * you implement `func (t SomeType) String() string { return <string of t> }`
  * depending on the type it holds, an interface value prints differently
* for example, every type can have its own way to `fmt.Printf()` if
  * interface `Stringer`'s method `String() string` holds this type
  * `func (t SomeType) String() string { return <string of t to display> }`

Error
---
* built-in interface
```go
type error interface {
  Error() string
}
```
* the customized Error type implements an `error` interface
  * `func (e MyError) Error() string { /* handle error */ }`

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
  * their executions order is the reversed push order

Pointer
---
* no pointer ops
* 
``` 
type Vertex struct {
  X, Y int
}
p := &Vertex{1, 2} // p is a pointer which allows modification of the struct 
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

Closure
---
How to implement a local `static` variable inside a function? Use Closure

```go
func main() {
  counter := newCounter()
  counter()  // return 1
  counter()  // return 2
}

// Here newCounter() returns an anonymous function
// which has access to n even after it exists
func newCounter() func() int {
  n := 0
  return func() int {
    n += 1
    return n
  }
}
```
[Common ways to use closure](https://www.calhoun.io/5-useful-ways-to-use-closures-in-go/)

Test
---
Run `go test -v` at
```
func TestSum(t *testing.T) {
  t.Run("[1,2,3,4,5]", testSumFunc([]int{1, 2, 3, 4, 5}, 15))
  t.Run("[1,2,3,4,-5]", testSumFunc([]int{1, 2, 3, 4, -5}, 5))
}

func testSumFunc(numbers []int, expected int) func(*testing.T) {
  return func(t *testing.T) {
    actual := Sum(numbers)
    if actual != expected {
      t.Error(fmt.Sprintf("Expected the sum of %v to be %d but instead got %d!", numbers, expected, actual))
    }
  }
}
```
