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
The resolving of virtual function call is done at Run-time. (Runtime polymorphism, or refered as Late Binding or Dynamic Binding by the vptr), instead of an Early binding (Compile time binding))
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
We cannot create objects of abstract classes. But we can pointers to and references of abstract classes, also an abstract class can have constructors. If we do not override the pure virtual function in derived class, then derived class also becomes abstract class.
When all functions are pure virtual, an abstract class is similar to the "interface" in Java.





