#include <iostream>

Dog::Dog() {
    // class member functions are implemented in .cpp files.
}

void Dog::setName(const std::string& dogsName) {
    name = dogsName;
}

void Dog::setWeight(int dogsWeight) {
    weight = dogsWeight;
}

// virtual is only needed in the declaration, not the definition
void Dog::print() const {
    std::cout << "Dog is " << name << " and weighs " //...
}

Dog::~Dog() {
    // again, destructor
}

int main() {
    Dog myDog;
    myDog.setName("Barkley");
    myDog.setWeight(10);
    myDog.print();
    return 0; // returning runs destructor for the myDog object
}