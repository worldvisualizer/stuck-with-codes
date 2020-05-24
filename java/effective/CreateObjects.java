// Effective Java, Creating Destroying Objects


// Item 1: Consider static factory rather than constructors
class CreateObjects {
    /*
        static factory:
        1) constructor with certain names
        2) not required to create an object every time invoked
        3) can return an object of any subtype
        4) reduce the verbosity of creating param type instances
        - called type inference.

        e.g. java.util.EnumSet
        https://docs.oracle.com/javase/7/docs/api/java/util/EnumSet.html

        commonly used in service provider framework:
        in Jtem 1-1

        disadvantage:
        1) class without public or protected constructor cannot be subclassed
        2) not very distinguisiable from other static methods.

    */
    public static Boolean valueOf(boolean b) {
        return b ? Boolean.TRUE : Boolean.FALSE;
    }

    public static <K, V> MyHashMap<K, V> newInstance() {
        return new MyHashMap<K, V>();
    }

    Map<String, List<String>> m = MyHashMap.newInstance();
}

// Jtem 1-1: Consider using service provider framework
// commonly used in JDBC. It just needs to know that
// there's some service that follows interface Service.
// three components of SPF:

// 1) service interface
public interface Service {
    // service specific methods
}

public interface Provider {
    Service newService();
}

// this is provider
public class Services {
    private Services() {} // prevents instantiation
    private static final Map<String, Provider> providers;
    public static final String DEFAULT_PROVIDER_NAME = "<def>";

    // 2) service provider registration API
    public static void registerDefaultProvider(Provider p) {
        registerProvider(DEFAULT_PROVIDER_NAME, p);
    }

    public static void registerProvider(String name, Provider p) {
        providers.put(name, p);
    }

    // 3) service access API
    public static Service newInstance() {
        return newInstance(DEFAULT_PROVIDER_NAME);
    }

    public static Service newInstance(String name) {
        Provider p = providers.get(name);
        if(p == null) {
            throw new IllegalArgumentException(
                "No provider registered with name: " + name);
        }
        return p.newService();
    }
}




// service factory:
/*
    the factory method will return an instance of some class 
    (which name is stored in the system property
    "MyServiceImplementation"),
    but it has absolutely no idea what class it is.
*/
public interface MyService {
  void doSomething();
}

public class MyServiceFactory {
  public static MyService getService() {
    try {
      (MyService) Class.forName(System.getProperty("MyServiceImplemetation")).newInstance();
    } catch (Throwable t) {
      throw new Error(t);
    }
  }
}