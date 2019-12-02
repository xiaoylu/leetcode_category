Java Basics
===

Inheritance
---
* A subclass inherits all the public and protected members (fields, methods, and nested classes) from superclass
  * Superclass's private members are only accessible from the superclass
  * a private function using same signature in subclass:
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
                 // and it's illegal to access the private fun() in Base
                 // Polymorphism only works when the instance methods are overridden
  }
}
```
* Constructors are not inherited because they are not members
  * superclass's constructor can be invoked by `super()`
  * `super()` is called only once, implicitly or explicitly
* A class can not access its grandparent's methods
* Neither final methods nor private methods can be overridden in the subclass
* Java support multiple inheritance of type but NOT multiple inheritance of state
  * A class can implement multiple interfaces but extend at most one superclass
  * Thus, it avoids the [diamond problem](https://en.wikipedia.org/wiki/Multiple_inheritance#The_diamond_problem) in which superclasses share the fields using the same name
  * `(MyInterface) myVariable` can reference any object which instantiates a class that implements the `MyInterface`
* Type of inheritance (like protected, public or private in C++) can NOT be specified
* hiding vs. overriding (methods with same signatures in superclass and subclass)
  * static method: hiding, invoked by the class name
  * instance method: overriding, invoked by the specific object (called Polymorphism, or virtual method invocation)
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
  * protected methods are accessable by classes in the same package
  * all methods are virtual by default
  * The access specifier for overriding method can allow more than the overridden method
    * ex. a protected instance method in the superclass can be made public in subclass

super() vs. this():
---
  * Motivation: constructor does not have a name
  * call super() and this() only inside constructor 
  * call super() and this() only once
  * super() is called by default in constructor which doest not have this()
    * but parent's **parametrized constructor** must be called **implicitly** via `super(arguments)`  
  * constructor chaining
    * because every subclass constructor must invoke a constructor of its superclass, either explicitly or implicitly

final
---
* variable: 
  * the **reference** gets assigned only once (not necessarily at the declaration)
  * but you can mutate the state of the object it refers to
* method: can not be overidden (final == private, but Java does not complain redundancy)
  * useful for variable [initialization](https://docs.oracle.com/javase/tutorial/java/javaOO/initial.html) method when you don't want subclass override its parent's variable initialization
  * Methods called from constructors should generally be declared final
    * because a subclass's constructor may call a non-final method overridden in the subclass
* class: can not be inherited, all methods declared immediately within a final class behave as if they are final
  * ex. immutable class like the String

static:
---
* variable: static variables at class-level only (no static variable in functions)
* method: share across all instances
* class: only applies to static nested classes (to grant it access to static members of the outter class)
  * public static nested class can be understood as a "top-level" class declared within another class. It can be instantiated.
* block: static initialization block, could be anywhere in a class declaration, called by the order they appear

enum
---
* An enum is a kind of class and an annotation is a kind of interface. (cited from [Class.java](http://hg.openjdk.java.net/jdk8/jdk8/jdk/file/687fd7c7986d/src/share/classes/java/lang/Class.java#l76))
* `for (val : MyEnumClass.values())` return all values present inside enum.
* find the constant index: `val.ordinal()`
* `MyEnum.valueOf("abcd")` method returns the enum constant of the specified string value, if exists.
* Internally `enum` is a final class which you can neither extend nor instantiate from outside
```java
enum Color 
{ 
    RED, GREEN, BLUE; 
} 

/* internally above enum Color is converted to
final class Color
{
     public static final Color RED = new Color();
     public static final Color BLUE = new Color();
     public static final Color GREEN = new Color();
     
     private Color() {};
}*/
```
* Java requires that the constants be defined first, prior to any fields or methods
* write a rich enum
  * declare instance fields and write a constructor that takes the data and stores it in the fields
  * use abstract method and define them in each enum
```java
enum Color
{
  RED(1, 'red'){public String example() { return "Apple"; }};
  GREEEN(2, 'green'){public String example() { return "Grass"; }};
  public final int id;  // all fields must be final in enum
  public final String tag;
  Color(int id, String tag) {
    this.id = id;
    this.tag = tag;
  }
  public int id() { return id; }
  public String tag() { return tag; }
  public abstract String example();
}
```

Nested class: 
---
* Motivation 
  * if a class is useful to only one other class, then it is logical to embed it in that class
  * hiding class B within class A, so A's members can be declared private and B can access them
* it has access to the members of enclosing class, including its private members
* since it's a member of outer class, a nested/inner class can be declared private, public, protected, or package private (by default)
* static nested class vs. inner class
  * static nested class is basically a top-level class definition embedded in another top-level definition
    * [Builder pattern](https://github.com/xiaoylu/DesignPattern/tree/master/builder) defines a "Builder" as the static nested class.
  * inner class is bascially a member of its outter class
    * instance of inner class lives within the instance of outter class (like your liver vs. your body)
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
  * all fields are public, static and final by default
  * all methods are public and abstract by default
* an interface can extend multiple interfaces
* a class must implement all methods in interface
* interface is also a reference data type
  * therefore, an interface name can be used anywhere a type is used.
* A **functional interface** (annotated by @FunctionalInterface) is any interface that contains only one **abstract** method

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
* abstract classes
  * good for extension
  * but restricted by hierarchy structure
* interfaces
  * all fields are automatically static, and final
  * No **state** is involved
* if all the subclasses will share the same **state**, abstract class is a better choice
  * **state** refers to non-static or non-final fields
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
* An enum is a kind of class and an annotation is a kind of interface.
* Declared by `@interface MyAnnotations { String spec(); }`
* Annotations can apply to other annotations
  * @Target, @Retention, @Documented, @Repeatable, @Inherited (Read [this](https://docs.oracle.com/javase/tutorial/java/annotations/predefined.html))
* The annotations can let compilers to warn you (or not to warn you): 
  * @Deprecated vs. @SuppressWarnings, @Override 

Lambda expression
---
* A functional interface (annotated by @FunctionalInterface) is any interface that contains only one **abstract** method, ex. Comparator<T>, Predicate<T>, Function<T, R>

* Use lambda expression to represent the instance of a functional interface

```java
 /* Anonymous class implementation*/
 printPersons(
    roster,
    new CheckPerson() {    // CheckPerson is a functional interface 
        public boolean test(Person p) {
            return p.getGender() == Person.Sex.MALE
                && p.getAge() >= 18
                && p.getAge() <= 25;
        }
    }
);
                                   
/* Lambda expression implementation */
printPersons(
    roster,
    (Person p) -> p.getGender() == Person.Sex.MALE
        && p.getAge() >= 18
        && p.getAge() <= 25
);
```         
  * Lambda expression + Generic
```java
import java.util.function.Predicate; 

//interface Predicate<Person> {
//    boolean test(Person t);
//}                          

Predicate<String> p = (s)->s.startsWith("G");

p.test("Facebook")  // returns false
p.test("Google")  // returns true 
```

Generic
---

* In theory, we can use `Object myStuff` everywhere to achieve Polymorphism
  * because the Object class is the topmost class of java.
  * but it provides no type checks at compile time -- if we pass the wrong type, only runtime error is shown
  * we need to manually do cast `(SubClass) myStuff` everywhere
* Generic methods
  * Class: `class Foo<T> { T data; ...} `
```java
public class Util {
  public static <K, V> boolean compare(Pair<K, V> p1, Pair<K, V> p2) {
      return p1.getKey().equals(p2.getKey()) &&
             p1.getValue().equals(p2.getValue());
  }
}g
// we can skip the type parameter section if compiler knows these types
// otherwise, the type parameter section must appear before the method's return type
boolean same = Util.<Integer, String>compare(p1, p2);
```

* `List<Integer>` is NOT a subtype of `List<Number>`!!
  * How to define a subtype of `List<Number>`?
  * Upper Bounded Wildcard matches the type Foo and any subtype of Foo
   `public static void process(List<? extends Foo> list) { /* ... */ }`
    * `extends` here mean either "extends" (as in classes) or "implements" (as in interfaces)
    * mutiple interfaces: `class D <T extends A & B & C> { /* ... */ }`
  * Unbounded wildcard matches any type 
  `public static void printList(List<?> list) { ... }`
  * lower bounded wildcard `List<? super Integer>`

* type erasure:
  * the `<?>` is replaced by `<Object>` at **compile-time (instead of at runtime)**
  * the `<? extends Foo>` is replaced by `<Foo>` etc...
  
* JVM actually does **NOT** check which type is used at runtime!!
  * Bridge method:
    * After type erasure `T => Object`, the `setData(Integer data)` of `SubFoo` does not override `setData(Object data)` of the `Foo<Object>` anymore. So compiler creates a bridge method.

```java
public class Foo<T> {
    public T data;
    public void setData(T data) {
        this.data = data;
    }
}

public class SubFoo extends Foo<Integer> {
    public void setData(Integer data) {
        super.setData(data);
    }
    
    // Bridge method generated by the compiler
    // because setData(Integer ..) does not override setData(T ..)
    //public void setData(Object data) {
    //    setData((Integer) data);
    //}
}
```

* Restriction (remember that **the runtime does not check which generic type is actually used**):
  * `Foo<int>` is illegal because `int` is a primitive type
  * `class Foo<T> { void func() { new T(); } }` is illegal because `T`'s constructor is unknonw at compile time
  * `class Foo<T> { static T data; }` is illegal because all `Foo<Integer>`, `Foo<Double>` share the same static member `data` but what is the type of `data` then?
  * `List<Integer>[] arrayOfLists = new List<Integer>[2];` is illegal because you cannot create arrays of parameterized types
  * illegal because methods that have the same name and the same arguments – stripped of generics, have the same signature.
```java
public class Example {
    public void print(Set<String> strSet) { }
    public void print(Set<Integer> intSet) { }
}
```

Object & Class
---
* The Object class is the topmost class in Java. All classes inherits Object directly or indirectly.
* The Class class provides metadata about the current object's class
  * `public final Class getClass()` declared in the "Object" class	returns an object of the "Class" class.
  * If `A a = new B();`, then `a.getClass()` returns `B` which is the runtime type of `a`
* Use `<MyClass>.class` if you know `<MyClass>`.
```java
  // print all the public methods of 'MyClass'
  Method[] methods = MyClass.class.getDeclaredMethods();
  for (int i = 0; i < methods.length; i++) {
    System.out.println(methods[i]);
  }
```

Concurrent Programming
---

[Advanced Topics in Programming Languages: The Java Memory Model By Jeremy Manson](https://www.youtube.com/watch?v=WTVooKLLVT8) and his [blogs](http://jeremymanson.blogspot.com/2008/12/benign-data-races-in-java.html)

* Java language provides atomic access to variables (except long/double) but it's NOT enough
  * compiler may reorder independent statements within one thread
  * the memory model may delay the write to global memory
  * so, in addition to atomic access:
    * one must acquire/release the lock to create a happens-before relationship between threads!
    
* try to avoid concurrent design, when you have to, prefer `volatile` and `synchronized`
  * volatile variables are atomic (long/double becomes atomic)
  * **volatile read/write becomes lock acquire/release pairs**
    * visibility: write on volatile variabless goes directly into global memory
    * ordering: it creates a happens-before edge from write to read, which ensures ordering of two atomic blocks

* `synchronized` keyword has two purposes:
  * mutual exclusion ("all or nothing" guarantee)
  * ordering/communication (which is often forgotten)
    * use `synchronized` to ensure the visibility (aka the happens-before relationship)
    * both write and read should be `synchronized` (imagine read in the middle of write...)

* `volatile` ensure ordering of **single** write and read of a variable
  * it will be used alone with `synchronized` for the mutual exclusion across code blocks ("all or nothing" guarantee)
    
> For example:

> Class: init volatile bool `flag = false`

> Thread1: synchronized block one { write data; assign `flag = true`; }

> Thread2: synchronized block two { check if `flag==true`, if yes, read data, otherwise, wait indefinitely }

In this way, Thread2 will only obtain the data **after** Thread1 writes it.

  

    








