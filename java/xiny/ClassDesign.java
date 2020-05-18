// Class Declaration Syntax:
// <public/private/protected> class <class name> {
//    // data fields, constructors, functions all inside.
//    // functions are called as methods in Java.
// }

// You can include other, non-public outer-level classes in a .java file,
// but it is not good practice. Instead split classes into separate files.

class Bicycle {
    public int cadence; // anywhere
    private int speed; // only accessible from within the class
    protected int gear; // accessible from class, subclass
    static String className; // class variable

    // Static block
    // Java has no implementation of static constructors, but
    // has a static block that can be used to initialize class variables
    // (static variables).
    // This block will be called when the class is loaded.
    static {
        className = "Bicycle";
    }

    public Bicycle() {
        gear = 1; // java considers context about what this var is.
    }

    // you know the drill.
    public Bicycle(int startCadence) {

    }

    @Override // Inherited from the Object class.
    public String toString() {
        return "gear: " + gear + " cadence: " + cadence + " speed: " + speed +
            " name: " + name;
    }
}

// Object casting and interfaces

// Interfaces
// Interface declaration syntax
// <access-level> interface <interface-name> extends <super-interfaces> {
//     // Constants
//     // Method declarations
// }
public interface Edible { // naming goes as ...able.
    public void eat(); // don't need to implement. 
}


// Interface variables are static and final by default.
// because they cannot be instantiated by themselves.
public interface Digestible {
    public void digest();

    // Java 8 feature: default method
    // https://www.geeksforgeeks.org/default-methods-java/
    // allow the interfaces to have methods with implementation
    // without affecting the classes that implement the interface.
    public default void defaultMethod() {
        System.out.println('ss...');
    }
}

// In Java, you can extend only one class, but you can implement many
// interfaces. For example:
public class ExampleClass extends ExampleClassParent implements InterfaceOne,
    InterfaceTwo {
    @Override
    public void InterfaceOneMethod() {
    }

    @Override
    public void InterfaceTwoMethod() {
    }
}

/*
Abstract class vs Interface

Type of methods: 
- Interface can have only abstract methods.
- Abstract class can have abstract and non-abstract methods.
  From Java 8, it can have default and static methods also.

Final Variables:
- Variables declared in a Java interface are by default final
- An abstract class may contain non-final variables.

Type of variables:
- Abstract class can have final, non-final, static and non-static variables.
- Interface has only static and final variables.

Implementation:
- Abstract class can provide the implementation of interface.
- Interface can’t provide the implementation of abstract class.

Multiple implementation:
- An interface can extend another Java interface only,
- an abstract class can extend another Java class and
- implement multiple Java interfaces.

Accessibility of Data Members:
- Members of a Java interface are public by default.
- A Java abstract class can have class members like private,
  protected, etc.
*/

// So Java Abstract Classes are for more concrete situations
// where behaviors could be much more different
// while still following the contract specified by the interface

public abstract class Animal {
    private int age;
    public abstract void makeSound();
    public void eat() {
        // ...
        age = 30;
    }

    public void printAge() {
        // can access private variable here.
        System.out.println(age);
    }

    // Final Method Syntax:
    // <access modifier> final <return type> <function name>(<args>)

    // Final methods, like, final classes cannot be overridden by a child
    // class, and are therefore the final implementation of the method.
    public final boolean isWarmBlooded()
    {
        return true;
    }

    // abstract classes can have main method.
    public static void main(String[] args) {
        System.out.println("abstract class");
    }
}

class Dog extends Animal {
    // still need to override abstract methods.
    // boo.
    @Override
    public void makeSound() {
        // age = 30; => Error, age is private to Animal.
        // even the subclasses cannot touch private instance var.
    }

    // NOTE: You will get an error if you used the
    // @Override annotation here, since java doesn't allow
    // overriding of static methods.
    // What is happening here is called METHOD HIDING.
    // Check out this SO post: http://stackoverflow.com/questions/16313649/
    public static void main(String[] args) {
        Dog pluto = new Dog();
        pluto.makeSound();
        pluto.eat();
        pluto.printAge();
    }
}

// Enum Type
//
// An enum type is a special data type that enables for a variable to be a set
// of predefined constants. The variable must be equal to one of the values
// that have been predefined for it. Because they are constants, the names of
// an enum type's fields are in uppercase letters. In the Java programming
// language, you define an enum type by using the enum keyword. For example,
// you would specify a days-of-the-week enum type as:
public enum Day {
    SUNDAY, MONDAY, TUESDAY, WEDNESDAY,
    THURSDAY, FRIDAY, SATURDAY
}
public class EnumTest {
    // Variable Enum is now a valid type. Just like namedtuple.
    Day day;

    public EnumTest(Day day) {
        this.day = day;
    }
}
// Enum types are much more powerful than we show above.
// The enum body can include methods and other fields.
// You can see more at https://docs.oracle.com/javase/tutorial/java/javaOO/enum.html

// Lambda Expressions
Supplier<String> numPlanets = () -> Integer.toString(planets.size());

// The actual lambda expression is the parameter passed to forEach.
planets.keySet().forEach((p) -> System.out.format("%s\n", p));

// If you are only passing a single argument, then the above can also be
// written as (note absent parentheses around p):
planets.keySet().forEach(p -> System.out.format("%s\n", p));