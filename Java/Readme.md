Java Basics
===

Inheritance
---
  * Neither final methods nor private methods can be overridden in the subclass
  * Multiple inheritance is not allowed, subclass inherits at most one parent class
  * Type of inheritance (like protected, public or private in C++) can NOT be specified
  * A class can not access its grandparent's methods (`super()` can be called only once)

super() vs. this():
---
  * call super() and this() only inside constructor 
  * call super() and this() only once
  * super() is called by default in constructor which doest not have this()
    * but parent's parametrized constructor must be called via `super(arg1, arg2)` implicitly 

Access Levels:
---
* use private unless you have a good reason not to
* avoid public fields except for constants
* private methods can not be overridden
* protected methods are accessable by classes in the same package
* see [this table](https://docs.oracle.com/javase/tutorial/java/javaOO/accesscontrol.html)
* all methods are virtual by default

final
---
* variable: const, get assigned only once (not necessarily at the declaration)
* method: can not be overidden
  * useful for [initialization](https://docs.oracle.com/javase/tutorial/java/javaOO/initial.html) method when you don't want subclass override its parent's variable initialization
* class: can not be inherited, all methods declared immediately within a final class behave as if they are final

static:
---
* variable: static variables at class-level only (no static variable in functions)
* method: share across all instances
* class: only applies to static nested classes (access to static members of outter class)
* block: static initialization block, anywhere in class, called by the order they appear

Nested class: 
---
* Motivation 
  * if a class is useful to only one other class, then it is logical to embed it in that class
  * hiding class B within class A, so A's members can be declared private and B can access them
* it has access to the members of enclosing class, including its private members
* since it's a member of outer class, a nested/inner class can be declared private, public, protected, or package private (by default)
* static nested class vs. inner class
```java
 to create an object for the static nested class
terClass.StaticNestedClass nestedObject =
   new OuterClass.StaticNestedClass();

 to create an object for the inner class
terClass outerObject = new OuterClass(); // you must instantiate the OuterClass first
terClass.InnerClass innerObject = outerObject.new InnerClass();
```
* Serialization of inner classes (local and anonymous classes) and lambda expression is strongly discouraged

Abstract
---
* if a class includes abstract methods, the class itself must be declared abstract
* abstract class can not be instantiated
* subclass either implements all the abstract methods or be declared abstract

Interface
---
* cannot instantiate (no constructor)
* all of the methods are abstract. all fields are both static and final
* an interface can extend multiple interfaces
* class must implement all methods in interface 

Abstract classes vs. Interfaces
---
* interfaces
  * all fields are automatically public, static, and final
  * a class can implement multiple interface (can be a lifesaver)
* abstract classes
  * good for extension
  * but restricted by hierarchy
* Abstract class can implements only part of the methods of an Interface (and its subclass implements the rest)

Annotations
---
* @interface <annotation name>
* Annotations which apply to other annotations
  * @Target, @Retention, @Documented, @Repeatable, @Inherited (Read [this](https://docs.oracle.com/javase/tutorial/java/annotations/predefined.html))
* For compilers to warn you: 
  * @Deprecated vs. @SuppressWarnings, @Override 

Lambda expression
---
* A functional interface is any interface that contains only one **abstract** method, ex. Comparator<T>, Predicate<T>
* Use lambda expression to represent the instance of a functional interface
```java
 / * Anonymous class
   * Check Person is a functional interface
   * /
 printPersons(
    roster,
    new CheckPerson() {
        public boolean test(Person p) {
            return p.getGender() == Person.Sex.MALE
                && p.getAge() >= 18
                && p.getAge() <= 25;
        }
    }
);
                                   
/* Lambda Expression */
printPersons(
    roster,
    (Person p) -> p.getGender() == Person.Sex.MALE
        && p.getAge() >= 18
        && p.getAge() <= 25
);
```         
  * Using Generic
```java
import java.util.function.Predicate; 

//interface Predicate<Person> {
//    boolean test(Person t);
//}                          

Predicate<String> p = (s)->s.startsWith("G");

p.test("Facebook")  // returns false
p.test("Google")  // returns true 
```
