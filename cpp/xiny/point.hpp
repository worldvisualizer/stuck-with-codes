#include <iostream>
using namespace std;

class Point {

public:
    double x = 0; // these are default values
    double y = 0;

    Point() {};

    // initialization list, proper way to initialize 
    // class member values...?
    Point(double a, double b) : x(a), y(b) {
	   // do nothing except initializing values
    }
    // return type is point, parameter is the right hand side reference
    Point operator+(const Point& rhs) const;

    Point& operator+=(const Point& rhs);
}