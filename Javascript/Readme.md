Javascript Basics
===
Summarized from this [tutorial](https://www.dofactory.com/tutorial/javascript)

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
* Calling a constructor function without `new` is like calling an ordinary function.
* With `new`, you create an object, so the keyword `this` in the constructor function refers to this newly created object. 

```
function Book(isbn) {
    this.isbn = isbn;
    this.getIsbn = function () {
        return "Isbn is " + this.isbn;
    };
}
var book = new Book("901-3865");
```

The code above creates `getIsbn` function each time when `Book()` is called. 
We can use a single `getIsbn` function to skip the creation of function `getIsbn`. 
See below.
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

Calling `this` would find the local object (go up until it hits the global object, i.e. window, just like finding the variables declared by the `var` keyword.)

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

Prototypal inheritance
---
Properties on prototype objects do not change or override properties in the parent object.

Setting prototypes to an object is done by setting an object's prototype attribute to a prototype object.

A prototype is just a single object and derived object instances hold only references to their prototype.

```
var account = {
    bank: "Bank of America",   // just the default value
    getBank: function() {
        return this.bank;
    }
};
function createObject (p) {
    var F = function () {};    // Create a new and empty function
    F.prototype = p;
    return new F();
}
var savings = createObject(account);
```
