Java Basics
===

Inheritance
---
* A subclass inherits all the public and protected members (fields, methods, and nested classes) from superclass
  * Superclass's private members are only accessible from the superclass
  * a private function of same signature in subclass:
    * it's not overriding!
    * it's a just new member in the subclass
```java
class Base { 
  private void fun() { 
     System.out.println("Base fun");      
  } 
} 
    
class Derived extends Base { 
  private void fun() { 
     System.out.println("Derived fun");   
  } 
  public static void main(String[] args) { 
      Base obj = new Derived(); 
      obj.fun(); // compiler error, because fun() is not overridden in Derived.
                 // and it's illegal to access fun() in Base
                 // Polymorphism only works when the instance methods are overridden
  }
}
```
* Constructors are inherited because they are not members
  * superclass's constructor can be invoked by `super()`
  * A class can not access its grandparent's methods
  * `super()` can be called only once
* Neither final methods nor private methods can be overridden in the subclass
* multiple inheritance of state (NO) vs. multiple inheritance of type (YES)
  * A subclass inherits at most one superclass which avoids the diamond problem
  * A class implements more than one interface:   
    * `(MyInterface) myVariable` can reference any object of any class that implements the `MyInterface`
* Type of inheritance (like protected, public or private in C++) can NOT be specified
* hiding vs. overriding (same signature in superclass and subclass)
  * static method: hiding, invoked by the type
  * instance method: overriding, invoked by the specific object (Polymorphism, virtual method invocation)
```java
public class Animal {
    public static void testClassMethod() {
        System.out.println("The static method in Animal");
    }
    public void testInstanceMethod() {
        System.out.println("The instance method in Animal");
    }
}

public class Cat extends Animal {
    public static void testClassMethod() {
        System.out.println("The static method in Cat");
    }
    public void testInstanceMethod() {
        System.out.println("The instance method in Cat");
    }

    public static void main(String[] args) {
        Cat myCat = new Cat();
        Animal myAnimal = myCat;
        Animal.testClassMethod(); // hiding, print "The static method in Animal"
        myAnimal.testInstanceMethod(); // overriding, print "The instance method in Cat"
    }
}
```

* [Access Levels](https://docs.oracle.com/javase/tutorial/java/javaOO/accesscontrol.html):
  * use private unless you have a good reason not to
  * avoid public fields except for constants
  * private methods can not be overridden
    * private method are **private**
  * protected methods are accessable by classes in the same package
  * all methods are virtual by default
  * The access specifier for overriding method can allow more than the overridden method
    * a protected instance method in the superclass can be made public in subclass

super() vs. this():
---
  * call super() and this() only inside constructor 
  * call super() and this() only once
  * super() is called by default in constructor which doest not have this()
    * but parent's **parametrized constructor** must be called **implicitly** via `super(arguments)`  
  * constructor chaining
    * because every subclass constructor invokes a constructor of its superclass, either explicitly or implicitly

final
---
* variable: const, get assigned only once (not necessarily at the declaration)
* method: can not be overidden
  * useful for [initialization](https://docs.oracle.com/javase/tutorial/java/javaOO/initial.html) method when you don't want subclass override its parent's variable initialization
  * Methods called from constructors should generally be declared final
    * because a subclass's constructor may call a non-final method overridden in the subclass
* class: can not be inherited, all methods declared immediately within a final class behave as if they are final
  * ex. immutable class like the String

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
// static nested class
OuterClass.StaticNestedClass nestedObject = new OuterClass.StaticNestedClass();

// an inner class must be associated with the specific instance
OuterClass outerObject = new OuterClass(); // you must instantiate the OuterClass first
OuterClass.InnerClass innerObject = outerObject.new InnerClass();
```
* Serialization of inner classes (local and anonymous classes) and lambda expression is strongly discouraged

Abstract
---
* if a class includes abstract methods, the class itself must be declared abstract
* abstract class can not be instantiated
* subclass either implements all the abstract methods or be declared abstract

Interface
---
* does not have fields, so it cannot be instantiated (i.e. no constructor)
* all of the methods are `public abstract` by default
  * except the `public default` methods and `public static` methods which are implemented explicitly
    * default method
      * impacts all class implementing this interface
      * enable you to add new functionality to existing interfaces
      * ensure binary compatibility with code written for older versions of those interfaces
    * static method
      * every instance of the class implementing an interface shares its static methods
      * suitable for helper methods
```java
public interface CustomInterface {
     
    public abstract void method1();
     
    public default void method2() {
        System.out.println("default method");
    }
     
    public static void method3() {
        System.out.println("static method");
    }
}
 
public class CustomClass implements CustomInterface {
 
    @Override
    public void method1() {
        System.out.println("abstract method");
    }
     
    public static void main(String[] args){
        CustomInterface instance = new CustomClass();
        instance.method1(); // print "abstract method"
        instance.method2(); // print "default method"
        CustomInterface.method3(); // print "static method"
    }
}
```

* access level
  * all fields are both static and final by default
  * all constant values defined in an interface are implicitly public, static, and final
  * all of the methods are public and abstract by default
* an interface can extend multiple interfaces
* a class must implement all methods in interface 
* a class can implement more than one interface
* A functional interface (annotated by @FunctionalInterface) is any interface that contains only one **abstract** method
* Interface is a reference data type
  * An interface name can be used anywhere a type can be used.

Case Study of Interfaces `Comparator<T>`
```java

@FunctionalInterface
public interface Comparator<T> {
    int compare(T o1, T o2);
    
    default Comparator<T> reversed() {
        return Collections.reverseOrder(this);
    }
    
    public static <T, U extends Comparable<? super U>> Comparator<T> comparing(
            Function<? super T, ? extends U> keyExtractor)
    {
        Objects.requireNonNull(keyExtractor);
        return (Comparator<T> & Serializable)
            (c1, c2) -> keyExtractor.apply(c1).compareTo(keyExtractor.apply(c2));
    }
    
    ...
}

//Card::getRank and Card::getSuit are the getter functions of the class Card
myDeck.sort(
    Comparator.comparing(Card::getRank)
        .reversed()
        .thenComparing(Comparator.comparing(Card::getSuit)));
``` 

Abstract classes vs. Interfaces
---
* interfaces
  * all fields are automatically public, static, and final
  * a class can implement multiple interface (can be a lifesaver)
* abstract classes
  * good for extension
  * but restricted by hierarchy structure
* if all the subclasses will share the same **state**, abstract class is a better choice
  * such **state** includes non-static or non-final fields
* Abstract class can implements only part of the methods of an Interface (and its subclass implements the rest)
```java
abstract class X implements Y {
  // implements all but one method of Y
}

class XX extends X {
  // implements the remaining method in Y
}
```

Annotations
---
* @interface <annotation name>
* Annotations which apply to other annotations
  * @Target, @Retention, @Documented, @Repeatable, @Inherited (Read [this](https://docs.oracle.com/javase/tutorial/java/annotations/predefined.html))
* For compilers to warn you: 
  * @Deprecated vs. @SuppressWarnings, @Override 

Lambda expression
---
* A functional interface (annotated by @FunctionalInterface) is any interface that contains only one **abstract** method, ex. Comparator<T>, Predicate<T>, Function<T, R>
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
