C++
===

The default constructors are called in the order of inheritance, while the default destructors are called in the opposite order.
---
BUT you have to explicitly call the base class’s parameterised constructor in the derived class
```
Child(int j): Parent(j) 
{ 
    // constructor of Child 
} 
```
The parameterised constructor of base class can NOT be called in default constructor of the derived class.

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


Return by reference
---
```
// function to return reference value 
int global_var;

int& ReturnReference() 
{ 
    return global_var; 
}

ptr_to_var = &ReturnReference(); // Note the usage of & symbol

ReturnReference() = 20.23; // we can do this
```

Virtual Function
---
They are always defined in base class and overridden in derived class with the EXACT same prototype, while the 'virtual' keyword is optional in the derived class.

The resolving of virtual function call is done at Run-time. (Runtime polymorphism, or refered as Late Binding or Dynamic Binding by the vptr), instead of an Early binding (Compile time binding) for other overridings)

In case of virtual function in base, the call is forwarded to the **most heavily derived** class.

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

Virtual Destructor
---
If you do a "delete p" where p is a pointer to a base class, then that class needs have a virtual destructor.

[Why?](https://blogs.msdn.microsoft.com/oldnewthing/20040507-00/?p=39443) 
Because your "delete p" might be early binded to the base class's destructor at compile time, so memory leak happens for the derived class.

"There’s rarely a reason NOT to make the destructor virtual if you already have a (public) virtual method in the base class." 
The vptr is already there in the base class anyway.

Pure Virtual Function (Abstract Class)
---
A class is abstract if it has at least one pure virtual function. 
```
virtual void func() = 0; 
```
We cannot create objects of abstract classes. But we can pointers to and references of abstract classes, also an abstract class can have constructors. 

If we do not override the pure virtual function in derived class, then derived class also becomes abstract class.

When all functions are pure virtual, an abstract class is similar to the "interface" in Java.

* = 0 means that a function is pure virtual and you cannot instantiate an object from this class. You need to derive from it and implement this method.
* = delete means that the compiler will not generate those constructors for you. AFAIK this is only allowed on copy constructor and assignment operator.

Friend Class & Functions
---
Friendship is not mutual. If a class A is friend of B, then B doesn’t become friend of A automatically.
Friendship is not inherited.

Static Variable
---
The lifetime of function static variables begins the first time the program flow encounters the declaration and it ends at program termination.






