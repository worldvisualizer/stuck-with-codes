// Gradle is a Groovy script.

println "Hello World"

// variable declaration 
// initialization later is also possible
// value just is null when not initialized
def x = 1
println x

x = new java.util.Date()

// typical string behavior like python
def str1 = 'char?'
def str2 = "double quote string"

// Array
// typical array behavior
def technologies = []
technologies.add("...")
technologies << "Groovy"
technologies.addAll(["Gradle", "Griffon"])
technologies.remove("Griffon")
technologies = technologies - "Grails"

// it's also a good practice to look at 
// array internal implementation

// closure supported, string interpolation supported
// $it notation is just something groovy does
technologies.each { println "Tech:$it" }
technologies.eachWithIndex {
    it, i -> println "$i, $it"
}

// def notation is not necessary...?
// so it seems like when initialized directly,
// you don't need def notation. Type is inferred
// sorting where it creates new copy
sortedTechnologies = technologies.sort(false)

// Map
// typical map
def devMap = [:]
devMap = ["name": "Roberto", "framework": "Grails"]
devMap.put('lastName', 'Perez')

// same thing with iteration
devMap.each { println "$it.key: $it.value"}
// devMap.each { println "key: $it.key['noop']}
// smartly parses up to it.key. ohh.....

assert devMap.containsKey('name')
assert devMap.containsValue('Roberto')

// ever heard of JavaBeans? yeah.
// There's something called GroovyBeans

// Class
class Foo {
    // this makes it a read-only property
    final String name = "Roberto"
    String language
    // function does not become a property.
    // so function is probably not an object in groovy
    protected void setLanguage(String language) {
        this.language = language
    }
    // this is also a property? wut
    def lastName
}

foo = new Foo()

println foo.name
foo.name = 'Joseph' // ReadOnlyPropertyException
println foo.language
println foo.lastName
println foo.noop // MissingPropertyException
println foo.setLanguage // MissingPropertyException
println foo.setLanguage('some string')
println foo.language

// Functions

// default arguments possible, no return statement
// just like Ruby
def say(msg = "Hello", name = "World") {
    "$msg $name!"
}

// Ternary operator
displayName = user.name ? user.name : 'Anonymous'

// Elvis Operator: returns first operand if 
// operand evaluates to true.
// so shortcut of ternary operator
displayName = user.name ?: 'Anonymous'

//For loop
//Iterate over a range
def x = 0
for (i in 0 .. 30) {
    x += i
}

// Spread Operator
def technologies = ['Groovy','Grails','Gradle']
technologies*.toUpperCase() // = to technologies.collect { it?.toUpperCase() }

// Safe navigation operator:
// used to avoid a NullPointerException.
// Just like Optional in Swift
def user = User.get(1)
def username = user?.username

// Groovy closure is like a code block of a method pointer
def clos = {
    println "hello world"
}

println "executing the closure"
clos() // this is possible, so code block has a name


def sum = { a, b -> println a + b }
sum(2,4) // not very different from function.

// referencing outer scope's variable is fine.
def x = 5
def multiplyBy = { num -> num * x }
println multiplyBy(10)

// omitting the parameter if it's only one is fine
def close = { print it } // it is the automatic name

// Memoization, by Groovy
def c1 = { a, b -> 
    sleep(1000)
    a + b
}
mem = c1.memoize() // this fucking rocks

def callClosure(a, b) {
    def start = System.currentTimeMillis()
    mem(a, b)
    println "Inputs(a = $a, b = $b) - took ${System.currentTimeMillis() - start} msecs."
}

/*
Inputs(a = 1, b = 2) - took 1002 msecs.
Inputs(a = 1, b = 2) - took 0 msecs.
Inputs(a = 2, b = 3) - took 1004 msecs.
Inputs(a = 2, b = 3) - took 0 msecs.
Inputs(a = 3, b = 4) - took 1001 msecs.
Inputs(a = 3, b = 4) - took 1 msecs.
Inputs(a = 1, b = 2) - took 0 msecs.
Inputs(a = 2, b = 3) - took 0 msecs.
Inputs(a = 3, b = 4) - took 0 msecs.
*/

// Special Bean Classes in Groovy
/*
The Expando class is a dynamic bean so we can add properties and we can add
  closures as methods to an instance of this class

  http://mrhaki.blogspot.mx/2009/10/groovy-goodness-expando-as-dynamic-bean.html
*/
def user = new Expando(name:"Roberto")
assert 'Roberto' == user.name

user.lastName = 'Pérez'
assert 'Pérez' == user.lastName

user.showInfo = { out ->
  out << "Name: $name"
  out << ", Last name: $lastName"
}

def sw = new StringWriter()
println user.showInfo(sw)
println user // this gives showInfo as:
// showInfo=ConsoleScript30$_run_closure1@c7767be

// Metaprogramming
//Using ExpandoMetaClass to add behaviour
String.metaClass.testAdd = {
    println "we added this"
}

String x = "test"
x?.testAdd()

//Intercepting method calls
class Test implements GroovyInterceptable {
    def sum(Integer x, Integer y) { x + y }

    // this is a decorator scheme
    // using interface behavior
    def invokeMethod(String name, args) {
        System.out.println "Invoke method $name with args: $args"
    }
}

def test = new Test()
test?.sum(2,3)
test?.multiply(2,3)


/*
  TypeChecked and CompileStatic
  Groovy, by nature, is and will always be a dynamic language but it supports
  typechecked and compilestatic

  More info: http://www.infoq.com/articles/new-groovy-20
*/