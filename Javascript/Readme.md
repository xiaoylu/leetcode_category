Javascript Basics
===
Summarized from this [tutorial](https://www.dofactory.com/tutorial/)

Variables
---
Boolean values and numbers are value-based types, whereas strings, objects, arrays, and functions are reference types.

Value types are copied, passed, and compared by value. Reference types, are copied, passed, and compared by reference.

JavaScript strings are immutable. Modifying the string actually generates a new string.

Objects
---

JavaScript objects are mutable. The properties can be other objects. 

```
var rect = {
    width: 20, 
    height: 10,
    color: { red: 0, green: 255, blue: 128 }, // object property
    getArea: function() {                     // method property 
       return this.width * this.height;
    }
};
```

Dot notation is used more often to access properties, while bracket notation allows you to use the property names that are variables.

To get a list of property names from an object use the for-in loop.

```
var car = { make: "Toyota", model: "Camry" };
for (var prop in car) {
   // => make: Toyota, and model: Camry
   alert(prop + ": " + car[prop]);  
}
```

Constructor Function
---
* Constructor functions are capitalized by convention in JavaScript
* Calling a constructor function without new is like calling an ordinary function.
* 

```
function Book(isbn) {
    this.isbn = isbn;
    this.getIsbn = function () {
        return "Isbn is " + this.isbn;
    };
}
var book = new Book("901-3865");
```

The code above creates `getIsbn` function each time when `Book()` is called. We can use a single `getIsbn` function. See below.
```
function Book(isbn) {
    this.isbn = isbn;
}
Book.prototype.getIsbn = function () {
    return "Isbn is " + this.isbn;
};
var book = new Book("901-3865");
```

`this` 
---

JavaScript establishes an execution context for this function call.
Calling `this` finds the local context (or hits the global object, same story for finding the variables declared by the `var` keyword.)

```
var name = 'First';
var student = {
    name: 'Middle',
    detail: {
        name: 'Last',
        getName: function() {
            alert(this.name);
        }
    }
}
var result = student.detail.getName; 
result();                    // => 'First' (global scope)
student.detail.getName();    // => 'Last'  (detail scope) 
```


