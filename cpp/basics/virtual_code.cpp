#include <iostream>

class Base {
    public:
        Base() { std::cout << "base class" << std::endl; }

        virtual void what() { std::cout << "base class what() " << std::endl; }
};

class Derived : public Base {
    public:
        Derived() : Base() { std::cout << "derived" << std::endl; }
        void what() { std::cout << "derived class what() " << std::endl; }
};

int main() {
    Base p;
    Derived c;

    Base* p_c = &c;
    Base* p_p = &p;

    p_p->what();
    p_c->what();
    return 0;
}
