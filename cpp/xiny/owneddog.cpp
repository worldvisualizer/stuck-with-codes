// this class inherits everything public and protected 
// from the Dog class as well as the private stuff,
// but cannot access private members/methods
// without accessors

class OwnedDog : public Dog {

public:
    void setOwner(const std::string& dogsOwner);

    // override the behavior of the print function for all ownedDogs.
    // subtype polymorphism:
    // http://en.wikipedia.org/wiki/Polymorphism_(computer_science)#Subtyping
    void print() const override;

private:
    std::string owner;
};
