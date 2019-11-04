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

Private copy constructor makes objects non-copyable. 

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
        // we don't want.
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

Virtual Constructor for Factory Pattern
---
Dynamic creation of derived classes at Runtime 
```
//// LIBRARY START 
class Base 
{ 
public: 
  
    // The "Virtual Constructor" 
    static Base *Create(int id); 
  
    Base() { } 
  
    virtual // Ensures to invoke actual object destructor 
    ~Base() { } 
  
    // An interface 
    virtual void DisplayAction() = 0; 
}; 

// We can also declare "Create" outside Base. 
// But is more relevant to limit it's scope to Base 
Base *Base::Create(int id) 
{ 
    // Just expand the if-else ladder, if new Derived class is created 
    // User need not be recompiled to create newly added class objects 
  
    if( id == 1 ) 
    { 
        return new Derived1; 
    } 
    else if( id == 2 ) 
    { 
        return new Derived2; 
    } 
    else
    { 
        return new Derived3; 
    } 
} 
//// LIBRARY END 
```
Note that the function Create used to return different types of Base class objects at runtime. It acts like virtual constructor, also referred as Factory Method in pattern terminology.

Return by reference
---
```
// function to return reference value 
int global_var;

int& ReturnReference() 
{ 
    return global_var; 
}

int *ptr_to_var = &ReturnReference(); // Note the usage of & symbol

ReturnReference() = 20.23; // we can do this
```

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
* begins the first time the program touches the declaration 
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

The Diamond Problem
---
The diamond problem occurs when two superclasses of a class have a common base class. So the derived-class at very bottom gets two copies of all attributes of superclass at the very top. So the virtual mode is needed here.

Smart Pointer
---
The idea is to make a class with a pointer, destructor and overloaded operators like * and ->. Since destructor is automatically called when an object goes out of scope, the dynamically allocated memory would automatically deleted (or reference count can be decremented).

```
#include<iostream> 
using namespace std; 
  
// A generic smart pointer class 
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
A more advanced implementation: assignment to a smart pointers would triger the destruction of its previous value. This type of smart pointer is called `Holder`. One of the such smart-pointer type is `std::auto_ptr` (chapter 20.4.5 of C++ standard), which allows to deallocate memory automatically when it out of scope and which is more robust than simple pointer usage when exceptions are thrown, although less flexible. Another convenient type is `boost::shared_ptr` which implements reference counting and automatically deallocates memory when no references to object remains. This helps avoiding memory leaks and is easy to use to implement RAII.

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

When do we use Initializer List in C++?
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

rvalue and move semantics
---
The lvalue has a memory allocated so you can assign to lvalues.
The rvalues, such as temporary values, can not be assigned to.

When pass by value, C++ copies the object's memory to pass to the function invocation.
But if a rvalue is passed as argument to a function, instead of copy and release the rvalue,
we can directly transfer the ownership of this rvalue to this function.

Note that, after the transition is done, the caller should not do anything with the rvalue.

C++11 supports rvalue reference `T&& t`, allowing separate overloads for rvalues and lvalues.

```
// Move constructor
Foo(Foo&& original) {
//
}

// Move assignment
Foo& operator=(Foo&& other)  
{
//
}
```

For a lvalue `b`, `Foo a = std::move(b)` would cast `b` to rvalue first.
If `Foo` has a move constructor, then the ownership of `b` is transfered to `a`;
Otherwise, `b` would still be copied and the copy is passed to `a`'s constructor.

unique_ptr
---
* sole owner of whatever it points to

https://en.cppreference.com/w/cpp/memory/unique_ptr

Styles
---
Namespace are all lower cases
* include both declaration (.h file) and definition (.cc file) in the same namespace 
* be explicit: don't `using namespace std`; don't use inline namespace

Further Reading
---
Test yourself: https://www.geeksforgeeks.org/c-plus-plus-gq/

STL: https://www.geeksforgeeks.org/the-c-standard-template-library-stl/

Google C++ style guide: https://google.github.io/styleguide/cppguide.html#Namespaces







