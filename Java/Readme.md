Java Basics
===

* Inheritance
  * Neither final methods nor private methods can be overridden in the subclass
  * Multiple inheritance is not allowed, subclass inherits at most one parent class
  * Type of inheritance (like protected, public or private in C++) can NOT be specified
  * A class can not access its grandparent's methods (`super()` can be called only once)
* super() vs. this():
  * call super() and this() only inside constructor 
  * call super() and this() only once
  * super() is called by default in constructor which has neither this() or super()
    * but parent's parametrized constructor must be called via `super(arg1, arg2)` implicitly 
* Access Levels:
  * use private unless you have a good reason not to
  * avoid public fields except for constants
  * private methods can not be overridden
  * protected methods are accessable by classes in the same package
  * see [this table](https://docs.oracle.com/javase/tutorial/java/javaOO/accesscontrol.html)
  * all methods are virtual by default
* final:
  * variable: const, get assigned only once (not necessarily at the declaration)
  * method: can not be overidden
  * class: can not be inherited, all methods declared immediately within a final class behave as if they are final
* static:
  * variable: static variables at class-level only (no static variable in functions)
  * method: share across all instances
  * class: only applies to static nested classes (access to static members of outter class)
  * block: execute only
* Nested class: 
  * it has access to the members of enclosing class, including its private members
  * since it's a member of outer class, a nested/inner class can be declared private, public, protected, or package private (by default)
  * static nested class vs. inner class
* Abstract
  * if a class includes abstract methods, the class itself must be declared abstract
  * abstract class can not be instantiated
  * subclass either implements all the abstract methods or be declared abstract
* Interface
  * cannot instantiate (no constructor)
  * all of the methods are abstract. all fields are both static and final
  * an interface can extend multiple interfaces
  * class must implement all methods in interface 
* Abstract classes vs. Interfaces
  * interfaces
    * all fields are automatically public, static, and final
    * a class can implement multiple interface (can be a lifesaver)
  * abstract classes
    * good for extension
    * but restricted by hierarchy
  * Abstract class can implements part of the methods of an Interface
