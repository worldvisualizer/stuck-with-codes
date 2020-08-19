// classes and oop

#include <iostream>

class Dog {
    std::string name;
    int weight;

public:
    // default constructor
    Dog();

    void setName(const std::string& dogsName);
    void setWeight(int dogsWeight);

    // functions that do not modify the state of the object
    // should be marked as const. virtual is like an abstract method
    virtual void print() const;

    void bark() const { // functions can be defined inside class body
        std::cout << name << "barks!\n";
    }

    virtual ~Dog(); // destructor
    // if this class is going to be inherited,
    // then virtual destructor is necessary for a case 
    // where child class object is destroyed through a base-class reference

}; // semicolon after class definition.