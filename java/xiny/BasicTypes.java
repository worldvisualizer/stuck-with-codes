/**
 * JavaDoc comments look like this. Used to describe the Class or various
 * attributes of a Class.
 * Main attributes:
 *
 * @author         Name (and contact information such as email) of author(s).
 * @version     Current version of the program.
 * @since        When this part of the program was first added.
 * @param         For describing the different parameters for a method.
 * @return        For describing what the method returns.
 * @deprecated  For showing the code is outdated or shouldn't be used.
 * @see         Links to another part of documentation.
*/

// Still easy enough to make use of sublime
// checkstyle for linting
// compilation and running and making jar file using Gradle

import java.util.ArrayList;
import java.util.Scanner;
import java.security.*;

public class LearnJava {
    public static void main(String[] args) {
        // main method as an entry point.
        // java programs starts by running a main method
        // of the class it intends to run.

        // is this possible? does not seem like it
        // import java.util.Scanner;
        Scanner scanner = new Scanner(System.in);

        // Seems like scanner reads string by default
        String name = scanner.next();

        byte numByte = scanner.nextByte();
        int numInt = scanner.nextInt();
        float numFloat = scanner.nextFloat();
        double numDouble = scanner.nextDouble();
        boolean bool = scanner.nextBoolean();

        int fooInt; // declaration without initialization possible

        int fooInt1, fooInt2, fooInt3;

        int barInt = 1;
        int barInt1, barInt2, barInt3;
        barInt1 = barInt2 = barInt3 = 1; // multiple assignment possible

        // 8-bit signed two's complement integer
        byte fooByte = 100;

        // 0xff (8 bit) maybe takes out signedness at the 
        // most significant bit
        /*
            byte b = (byte)0xC8;
            // so things get FF... when casted to integer
            int v1 = b;       // v1 is -56 (0xFFFFFFC8)
            int v2 = b & 0xFF // v2 is 200 (0x000000C8)
        */
        int unsignedIntLessThan256 = 0xff & fooByte;
        int signedInt = (int) fooByte;
        // so this will be a contrasted negative number
        short fooShort = 10000;
        int bazInt = 1; // 32 bit
        long fooLong = 100000L; // 64 bit

        // float - single-precision 32 bit
        float fooFloat = 234.5f;
        // double - 64 bit
        double fooDouble = 123.4;

        // BigInteger - Immutable arbitrary-precision integers
        //
        // BigInteger is a data type that allows programmers to manipulate
        // integers longer than 64-bits. Integers are stored as an array of
        // of bytes and are manipulated using functions built into BigInteger
        //
        // BigInteger can be initialized using an array of bytes or a string.
        BigInteger fooBigInteger = new BigInteger(fooByteArray);

        // BigDecimal - Immutable, arbitrary-precision signed decimal number
        //
        // A BigDecimal takes two parts: an arbitrary precision integer
        // unscaled value and a 32-bit integer scale
        //
        // BigDecimal allows the programmer complete control over decimal
        // rounding. It is recommended to use BigDecimal with currency values
        // and where exact decimal precision is required.
        //
        // BigDecimal can be initialized with an int, long, double or String
        // or by initializing the unscaled value (BigInteger) and scale (int).
        BigDecimal fooBigDecimal = new BigDecimal(fooBigInteger, fooInt);

        // Be wary of the constructor that takes a float or double as
        // the inaccuracy of the float/double will be copied in BigDecimal.
        // Prefer the String constructor when you need an exact value.
        BigDecimal tenCents = new BigDecimal("0.1");

        // for static variables... this is possible
        // Double Brace Initialization
        // The Java Language has no syntax for how to create static Collections
        // in an easy way. Usually you end up in the following way:
        private static final Set<String> COUNTRIES = new HashSet<String>();
        static {
           COUNTRIES.add("DENMARK");
           COUNTRIES.add("SWEDEN");
           COUNTRIES.add("FINLAND");
        }

        // first brace creates Anonymous Inner Class 
        // and second one declares an instance initializer block
        private static final Set<String> COUNTRIES = new HashSet<String>() {{
            add("DENMARK");
            add("SWEDEN");
            add("FINLAND");
        }}
    }
}