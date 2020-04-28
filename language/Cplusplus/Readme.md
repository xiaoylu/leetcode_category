C++
===

Order of Construction and Destruction
---
* the default constructors are called in the order of inheritance (base first and derived next)
* the default destructors are called in the opposite order.
BUT you can only explicitly call the base class’s parameterised constructor in the derived class
```
Child(int j): Parent(j) 
{ 
    // constructor of Child 
} 
```
The parameterised constructor of base class can NOT be called in default constructor of the derived class.
The following code gets "compiler error"
```
class Base
{
public :
    int x, y;
public:
    Base(int i, int j){ x = i; y = j; }
};
 
class Derived : public Base
{
public:
    Derived(int i, int j):x(i), y(j) {}  // Error: the base class members cannot be directly assigned
    void print() {cout << x <<" "<< y; }
};
```

And objects are always destroyed in reverse order of their creation.

We can not make constructor virtual, but we can make destructor virtual. In this way, the call of derived's destructor will be called first, and then the bases's destructor. Otherwise, without virtual keyword, only Derived's destructor gets called.

```
#include<iostream>
using namespace std;
class Base  {
public:
    Base()    { cout<<"Constructor: Base"<<endl; }
    virtual ~Base()   { cout<<"Destructor : Base"<<endl; }
};
class Derived: public Base {
public:
    Derived()   { cout<<"Constructor: Derived"<<endl; }
    ~Derived()  { cout<<"Destructor : Derived"<<endl; }
};
int main()  {
    Base *Var = new Derived();    // Note: if you declare "Derived Var;", then both destructors always get called, w/o virtual keyword.
    delete Var;
    return 0;
}
```
Output
```
Constructor: Base
Constructor: Derived
Destructor : Derived
Destructor : Base
```

Copy constructor
---
In C++, a Copy Constructor may be called:
1. When an object of the class is returned or passed by value.
2. When an object is constructed based on another object of the same class. 
> Note `MyClass a = b;` is equal to `MyClass a(b);` but `MyClass a, b; a = b;` calls the assignment function instead.
3. When the compiler generates a temporary object. (depending on the compiler's optimization)

Private copy constructor makes objects non-copyable. (Or simply mark it by `=delete`.)

For singleton pattern, we intend to make it non-copyable. See below.
```
class S
{
    public:
        static S& getInstance()
        {
            static S    instance; // Guaranteed to be destroyed.
                                  // Instantiated on first use.
            return instance;
        }
    private:
        S() {}                    // Constructor? (the {} brackets) are needed here.

        // C++ 03
        // ========
        // Don't forget to declare these two. You want to make sure they
        // are unacceptable otherwise you may accidentally get copies of
        // your singleton appearing.
        S(S const&);              // Don't Implement
        void operator=(S const&); // Don't implement

        // C++ 11
        // =======
        // We can use the better technique of deleting the methods
        // that we don't want.
    public:
        S(S const&)               = delete;
        void operator=(S const&)  = delete;

        // Note: Scott Meyers mentions in his Effective Modern
        //       C++ book, that deleted functions should generally
        //       be public as it results in better error messages
        //       due to the compilers behavior to check accessibility
        //       before deleted status
};
```
Special member functions
---
They will be defined by the compiler even if not defined by the user:
* Default constructor
* Copy constructor
* Move constructor (since C++11)
* Copy assignment operator
* Move assignment operator (since C++11)
* Destructor

Mark them `delete` (or sometimes `explicit`) to avoid, `default` to enforce.

Rule of Three
---
If a class defines one of the following it should probably explicitly define all three:
* Destructor
* Copy constructor 
> `Point(const Point &p) { x = p.x;}`
* Copy assignment operator
> `Point& operator=(const Point& p) { x = p.x; }`

[Violation Example](https://lokiastari.com/blog/2014/12/30/c-plus-plus-by-example-smart-pointer/)
If destructor is defined but copy constructor is missing,
the default copy constructor may conduct a 'shallow' copy which make the new object points to the same memory
of the original object. So, the same destructor gets called twice.
```cpp
template<typename T>
class UP
{
    private:
        T*   data;
    public:
        UP(T* data) : data(data) {}
        ~UP() { delete data; }
};
int main() {
    UP obj1<int>(new int(5));
    UP obj2<int>(obj1);  
            // the default copy constructor will assign
            // the data member of obj1 to
            // the data member of obj2, so the destructor
            // will be called twice
    return 0;
}
```
It is a often a good practice to declare constructor `explicit` to avoid the default type conversion.
(Otherwise, the compiler may use the constructor for conversions.)
Also C++11 allows `= delete` to get rid of certain functions.

Clockwise/Spiral Rule
---
http://c-faq.com/decl/spiral.anderson.html

* int* - pointer to int
* int const * - pointer to const int
* int * const - const pointer to int
* int const * const - const pointer to const int

Inheritance
---
* try to use `public` inheritance; do not use `private` inheritance, in this case, use composition instead
  * inject an object of the base class into the new class
* for base class:
  * mark functions `virtual`
  * mark API functions abstract to enforce subclass's implementation
* for subclass:
  * don't use `virtual`, mark `override` instead

Virtual Function
---
Member functions that are not declared as virtual are resolved at compile time, not run time.

The 'virtual' keywords are 
* always defined in base class
* but optional in the derived class

The resolving of virtual function call is done at run-time. 
> Runtime polymorphism, or refered as Late Binding or Dynamic Binding by the vptr, instead of an Early binding (Compile time binding)

In case of calling the virtual function in base, the call is **forwarded** to the **most heavily derived** class.
```
    base *p; 
    derived d; 
    p = &d; 
       
    // virtual function, binded at runtime (Runtime polymorphism) 
    // so we call derived's function
    p->virtual_function();  
       
    // Non-virtual function, binded at compile time 
    // so we call base's function
    p->non_virtual_function();  
```

A base class pointer can point to a derived class object. But we can **only** access 
* base class member 
* virtual functions in base class
using the base class pointer

Pure virtual function (abstruct function) is a virtual function without implementation.
A class with at least one pure virtual function is called abstract class.
An abstract class cannot be instantiated.

VTable & Vpointer
---
In the heap, at the top of an object's memory, a virtual pointer points to the code stack of a class. Every class has a vtable. **The vtable maps the child's overrided function to its own implementation, instead of its derived class's virtual function.** However, if a class does not provide customized implementation, the vtable still maps this function to its derived class's virtual function. 

![Imgur](https://i.imgur.com/VdeRgz2.png)

[简书](https://www.jianshu.com/p/91227e99dfd7)

Virtual Destructor
---
If you do a "delete p" where p is a pointer to a base class, then that class must have a virtual destructor.

[Why?](https://blogs.msdn.microsoft.com/oldnewthing/20040507-00/?p=39443) 
Because your "delete p" might be early binded to the base class's destructor at compile time, so memory leak happens for the derived class.

> "There’s rarely a reason NOT to make the destructor virtual if you already have a (public) virtual method in the base class." 
The vptr is already there in the base class anyway.

Pure virtual destructor is used when you want to make a class abstract but no other functions should be pure virtual.

Pure Virtual Function (Abstract Class)
---
A class is abstract if it has at least one pure virtual function. 
```
virtual void func() = 0; 
```
We cannot instantiate abstract class. But we can **pointers to** and **references of** abstract classes, also an abstract class can have **constructors**.

If we do not override the pure virtual function in derived class, then derived class also becomes abstract class.

When all functions are pure virtual, an abstract class becomes an "interface" in Java.

* `= 0` means that a function is pure virtual and you cannot instantiate an object from this class. You need to derive from it and implement this method
* `= delete` means the compiler will not generate those constructors for you (so we can hide copy constructor and assignment operator)

Friend Class & Functions
---
Friendship is not mutual. If a class A is friend of B, then B doesn’t become friend of A automatically.
Friendship is not inherited.

Lifetime of a data member (object)
---
* Association: Foo has a **pointer** to Bar object as a data member, without managing the Bar object => **Foo knows about Bar**
* Composition: Foo has a Bar object as data member => **Foo contains a Bar. It can't exist without it.**
 * **Composition over Inheritance**
* Aggregation: Foo has a pointer to Bar object and manages the lifetime of that object => **Foo contains a Bar, but can also exist without it.**

Static Variable
---
The lifetime of function static variables 
* begins the first time the execution flow "touches" the declaration 
* ends at program termination. 

So, you must "define" it after the class declaration.
```
class B 
{ 
    static A a; 
public: 
    B() { cout << "B's constructor called " << endl; } 
    static A getA() { return a; } 
}; 
  
A B::a;  // definition of a, it is when `a` gets created
         // without this line, your program will have "Compiler Error: undefined reference to `B::a'" 

int main() 
{ 
    B b;
    A a = b.getA(); 
  
    return 0; 
} 
```

Modes of Inheritance
---
* Public mode: If we derive a sub class from a public base class. Then the public member of the base class will become public in the derived class and protected members of the base class will become protected in derived class.
* Protected mode: If we derive a sub class from a Protected base class. Then both public member and protected members of the base class will become protected in derived class.
* Private mode: If we derive a sub class from a Private base class. Then both public member and protected members of the base class will become Private in derived class.
* Virtual Mode: get only one copy of the grand-parent (superclasses)'s attributes. 
    * `class A`
    * `class B: virtual public A`, `class C: virtual public A`
    * `class C: public B, public C`

![Modes](https://www.geeksforgeeks.org/wp-content/uploads/table-class.png)

When a class inherits another one, the members of the derived class can access the **protected** members inherited from the base class, **but not its PRIVATE members**. So, regardless of the inhertitance mode, private members are not accessable outside a base class, even for derived class, except declaring `friend` methods/class.

Restrict yourself to "is-a-type-of" inheritance. Don' use private mode, inject the base class as an instance into the "derived" class.

The Diamond Problem
---
The diamond problem occurs when two superclasses of a class have a common base class. So the derived-class at very bottom gets two copies of all attributes of superclass at the very top. So the virtual mode is needed here.

Smart/Unique Pointer 
---
Make a class with a pointer member, overload its operators like * and ->, and `delete` the pointer in destructor.

When this object goes out of scope, the dynamically allocated memory would automatically be deleted.
```
#include<iostream> 
using namespace std; 
  
// A generic smart pointer class 
// (WARN: it has potential errors, use std::auto_ptr in practice)
template <class T> 
class SmartPtr 
{ 
   T *ptr;  // Actual pointer 
public: 
   // Constructor 
   explicit SmartPtr(T *p = NULL) { ptr = p; } 
  
   // Destructor 
   ~SmartPtr() { delete(ptr); } 
  
   // Overloading dereferncing operator 
   T & operator * () {  return *ptr; } 
  
   // Overloding arrow operator so that members of T can be accessed 
   // like a pointer (useful if T represents a class or struct or  
   // union type) 
   T * operator -> () { return ptr; } 
}; 
  
int main() 
{ 
    SmartPtr<int> ptr(new int()); 
    *ptr = 20; 
    cout << *ptr; 
    return 0; 
} 
```

C++11 allows `unique_ptr` which is the sole owner of whatever it points to. 
The object is disposed when either of the following happens:
* the managing unique_ptr object is destroyed
* the managing unique_ptr object is assigned another pointer via operator= or reset().

Create a `unique_ptr` by `std::make_unique` or ` absl::make_unique`.

Move a `unique_ptr` by `std::move` (so you can move resource more safely across API boundaries.)

sizeof()
---
```
int array[5];
int* ptr = array;

std::cout << "array size " << sizeof(array) << std::endl;
std::cout << "ptr size " << sizeof(ptr) << str::endl;
```
array size will be 5 \* sizeof(int) = 20 

ptr size will be sizeof(int \*) which will be either 4 or 8 bytes.

Exception Handling
---
* If both base and derived classes are caught as exceptions then **catch block of derived class must appear before the base class**. If we put base class first then the derived class catch block will never be reached.
* The catch(...) must be the last catch block.
* Re-throw: `throw` in the catch section - a catch block **cleans up resources** of its function, and then rethrows the **same** exception **with same parameters**  for handling elsewhere. **The destructors are called in reverse order of constructors.**


Polymorphism
---
* Compile time polymorphism : template, overload
* Run time polymorphism: virtual function (late/dynamic binding)

Template
---
* **Compiler** creates a **new instance** of a template function for **every data type**.
    * so every instance has its own copy of static variable.
* Non-type parameters like `N` in `template <class T, int N> ...` must be const, so compiler can fill in the number at compile time
* template specialization: 
```
template <>
int max <int> (int &a, int &b)
{
    cout << "Called ";
    return (a > b)? a : b;
}
```

lambda expressions
---
Functor is a class/struct that defines the `operator()`. It can be called like a function (with access its internal variables).

Lambda expression is the anonymous functors.

> `[capture_variables] (function_arguments) -> return_type { function_logic }`

The capture variable can be passed either by value or by reference (with a prefix &).
 
Lambda only exists in the source code, it's compiled into statement in C++; closures are to lambdas as objects are to classes.
 
Initializer List
---
* The data members must be initialized at creation time
    * data member is const
    * data member does not have default constructor (if you implemented its parameterized constructor)
    * data member is a reference (sth. like `int &x`);
* **Parameterized constructor** of base class, because the base class must be instantied before calling the derived class's constructor. If we want to call default constructor of base class, we do not need initialier list.

```
// Class B is derived from A 
class B: A { 
public: 
    //Initializer list must be used 
    B(int x): A(x) { cout << "B's Constructor called"; }; 
}; 
```

rvalue and lvalue
---
https://www.artima.com/cppsource/rvalue.html
https://stackoverflow.com/questions/5481539/what-does-t-double-ampersand-mean-in-c11

The lvalue has a memory allocated so you can assign to lvalues.
The rvalue does NOT persist beyond one single expression; you can neither reference or assign to rvalues.

For example, &++x is valid because ++x increments x by 1 and then returns itself as a lvalue. But &x++ is invalid because x++ returns a copy of x (before increment x itself by 1).
```
A&  a_ref3 = A();  // Error!
A&& a_ref4 = A();  // Ok
```

C++11 supports rvalue reference `T&& t`, allowing separate overloads for rvalues and lvalues.

`std::move(b)` does nothing but cast lvalue `b` to rvalue type.
So calling `Foo a = std::move(b)` would call move constructor if exist; otherwise, the call would be degraded to normal constructor.

Again, the rvalue does NOT persist beyond one single expression, so after `std::move`, the caller can no longer access the object which gets casted to rvalue. move is a potentially destructive read. 在這一行死亡，然後在新的scope重生!

Move semantics
---
A move constructor and move assignment operator can eliminate extraneous copies.
```cpp
Foo(const Foo& original) {
   // copy the resources held by 'original' here
}

// Move constructor
Foo(Foo&& original) {
   // "steal" the resources held by 'original' here, rather than make copies of them
   // (e.g. pointers to dynamically-allocated objects, file descriptors, TCP sockets, I/O streams, running threads, etc.)     
   // we know for sure that 'original' will no longer be used in other places
}
```
The code which calls the constructor does not need to change. 
We just need to implement overload the constructor (i.e. add the move constructor):

Styles
---
Namespace are all lower cases
* include both declaration (.h file) and definition (.cc file) in the same namespace 
* be explicit: don't `using namespace std`; don't use inline namespace

(To be developed)

Further Reading
---
Test yourself: https://www.geeksforgeeks.org/c-plus-plus-gq/

STL: https://www.geeksforgeeks.org/the-c-standard-template-library-stl/

Google C++ style guide: https://google.github.io/styleguide/cppguide.html#Namespaces







