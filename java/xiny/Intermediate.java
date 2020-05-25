
public class FooObject {
    public FooObject() {
        // pass
    }
}


class IntermediateJava {
    public static void learnCopy() {
        FooObject x = new FooObject(1);
        FooObject y = new FooObject(2);
        x = y; // shallow --
        // just make x point to 2nd Foo,
        // Garbage Collector gets the 1st Foo
        bar(x);
    }

    public static void main(String[] args) {

    }
}