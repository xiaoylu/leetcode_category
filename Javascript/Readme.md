Javascript Basics
===
AirBnB [Javascript Style Guide](https://github.com/airbnb/javascript)

Google [Javascript Style Guide](https://google.github.io/styleguide/jsguide.html)

and this [tutorial](https://www.dofactory.com/tutorial/javascript)

Variables
---
Boolean values and numbers are value-based types, whereas strings, objects, arrays, and functions are reference types.

Value types are copied, passed, and compared by value. Reference types, are copied, passed, and compared by reference.

JavaScript strings are immutable. Modifying the string actually generates a new string.

Google+AirBnB Javascript style guide actually forbids the usage of `var`.

> Declare all local variables with either const or let. Use const by default, unless a variable needs to be reassigned. The var keyword must not be used.

Both `let` and `const` are block-scoped. The difference is `const` does not allow re-assignment and re-declaration. The `const` variable is a constant pointer and it can be optimized by browser. `const` is always preferred when appropriate.

```
// Wrong: `i` is redefined (not reassigned) on each loop step.
for (let i in [1, 2, 3]) {
    console.log(i);
}

// Correct: `i` gets a new binding each iteration
for (const i in [1, 2, 3]) {
  console.log(i);
}
```

Array
---

Destructuring

```
let [, b,, d] = someArray;
function optionalDestructuring([a = 4, b = 2] = []) { … };

const [a, b, c, ...rest] = generateResults();

// Spread operator to flatten elements out of one or more other iterables
[...foo]   // preferred over Array.prototype.slice.call(foo)
[...foo, ...bar]   // preferred over foo.concat(bar)
```

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

Methods
---

Shorthands

```
// class example
class {
  getObjectLiteral() {
    this.stuff = 'fruit';
    return {
      stuff: 'candy',
      method: () => this.stuff,  // Returns 'fruit'
    };
  }
}

// obj example
const foo = 1;
const bar = 2;
const obj = {
  foo,
  bar,
  method() { return this.foo + this.bar; },
};
```

Constructor Function
---
* Constructor functions are capitalized by convention
* Calling a constructor function without `new` is like calling an ordinary function. Doing this pollutes the global namespace!! 
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

Calling `this` would find the local object (go up until it hits the global object, i.e. the "window" object, which is just like finding the variables declared by the `var` keyword.)

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

Class
---
[Understanding Classes in JavaScript By Tania Rascia](https://www.digitalocean.com/community/tutorials/understanding-classes-in-javascript)

Extending a class: subclass constructors must call super() before setting any fields or otherwise accessing `this`.

```
// Initializing a class
class Hero {
    constructor(name, level) {
        this.name = name;
        this.level = level;
    }

    // Adding a method to the constructor
    greet() {
        return `${this.name} says hello.`;
    }
}

// Creating a new class from the parent
class Mage extends Hero {
    constructor(name, level, spell) {
        // Chain constructor with super
        super(name, level);

        // Add a new property
        this.spell = spell;
    }
}
```

The class keyword allows clearer and more readable class definitions than defining `prototype` properties.

Prototypal inheritance
---
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
    F.prototype = p;           // The function has a prototype property
    return new F();            // new instantiate this object
}
var savings = createObject(account);

alert(savings.getBank());                   // => Bank of America
savings.bank = "JP Morgan Chase";
alert(savings.getBank());                   // => JP Morgan Chase
```

Anonymous Immediate Function
---
The anonymous immediate function is the function wrapped in parentheses 
```
var module = (function() { 
      … 
      … 
}())
```

* it has no function name
* it gets executed immediately when JavaScript encounters it
* Withint such function, variables declared with `var` are private

Private member shared by prototype
---
```
function Book(author) {
   var author = author;          // private instance variable 
   this.getAuthor = function () {
      return author;             // privileged instance method
   };
}
Book.prototype = (function () {
   var label = "Author: ";       // private prototype variable
   return {
       getLabel: function () {   // privileged prototype method
           return label;
       }
     };
}());
var book1 = new Book('James Joyce');
alert(book1.getLabel() + book1.getAuthor()); // => Author: James Joyce
var book2 = new Book('Virginia Woolf');
alert(book2.getLabel() + book2.getAuthor()); // => Author: Virginia Woolf
```

Here both `book1` and `book2` adopts a prototype which has the same private variable `label`.

nested function closures
---

**All JavaScript functions are objects!!**

When you hold a reference to a function with a variable by
```
function counter() {
    var index = 0;
    function increment() {
       return ++index;
    }
    return increment;
}
var userIncrement = counter();    // a reference to inner increment()
var adminIncrement = counter();   // a reference to inner increment()
userIncrement();                  // => 1
userIncrement();                  // => 2
adminIncrement();                 // => 1
adminIncrement();                 // => 2
adminIncrement();                 // => 3
```
In such cases, Javascript will maintain a second, but hidden, reference to its closure which will NOT be destroyed after this function returns. (But every execution like will create its own copy of the closure, for example, `counter()` executes twice here.).

Even after the function returns, these local `var` like `index` in the closure will NOT be destroyed.

Because functions are objects, they are copied by reference.
















