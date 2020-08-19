// and in the cpp file...
Point Point::operator+(const Point& rhs) const {
    return Point(x + rhs.x, y + rhs.y);
}

// good practice to return a reference to the leftmost
// variable of an assignment. (a += b) == c will work this way.
Point& Point::operator+=(const Point& rhs) {
    x += rhs.x;
    y += rhs.y;
    // this is a pointer to the object, on which a method is called
    return *this;
}

int main() {
    Point up (0, 1); // this is the way to initialize cpp object
    Point right (1, 0);
    Point result = up + right;

    return 0;
}