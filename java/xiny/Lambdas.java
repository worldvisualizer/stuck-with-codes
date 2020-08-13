// Lambda Expressions

// methods that can be created without class (in java?)
// being passed around as a function object
// executed on demand

// lambdas must implement a functional interface
// only one single abstract method declared

import java.util.Map;
import java.util.HashMap;
import java.util.function.*;
import java.security.SecureRandom;

public class Lambdas {
	public static void main(String[] args) {
		planets.keySet().forEach((p) -> System.out.println(p));
	}
}