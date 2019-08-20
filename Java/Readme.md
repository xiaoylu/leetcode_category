Java Basics
===

* Inheritance
  * Neither final methods nor private methods can be overridden in the subclass
  * Multiple inheritance is not allowed 
  * Type of inheritance (like protected, public or private in C++) can NOT be specified
  * A class can not access its grandparent's methods (`super()` can be called only once)
* super() vs. this():
  * call super() and this() only inside constructor 
  * call super() and this() only once
  * super() is called by default in constructor without either this() or super()
    * but parametrized constructor must be called via `super(arg1, arg2)` implicitly 
* Access Levels:
  * use private unless you have a good reason not to
  * avoid public fields except for constants
  * private methods can not be overridden
  * protected methods are accessable by classes in the same package
  * see [this table](https://docs.oracle.com/javase/tutorial/java/javaOO/accesscontrol.html)
  * all methods are virtual by default
* final:
  * variable: const
  * method: can not be overidden
  * class: can not be inherited, all methods declared immediately within a final class (§8.1.1.2) behave as if they are final
* static:
  * variable: static variables at class-level only (no static variable in functions)
  * method: share across all instances
  * class: only applies to static nested classes
  * block: execute only
* Nested class: 
  * it has access to the members of enclosing class, including its private members
  * since it's a member of , a nested class can be declared private, public, protected, or package private(default)
  * static nested class vs. inner class  
* Interfaces
  * 
  *
* Abstract class
