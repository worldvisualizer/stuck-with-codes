import UIKit
import Foundation

// Swift is pretty cool. Everything is controlled by Apple,
// they know what to incorporate, recommend.
var str = "Hello, playground"
print(str) // running a program is very intuitive

let theAnswer = 42 // this is constant
var theQuestion = "What's the answer" // this is a variable
theQuestion = "reassignment"

func foo() -> Int {
    // for some reason top of the line declaration is problematic
    let someConstant: Int
    var someVariable: String
    // both vars and constants can be declared with a type
    // must be initialized before used
    
    someConstant = 0
    someVariable = "0"
    return someConstant
}
print(foo())

// Variable declaration and initialization
let aString: String = "A String"
let aDouble: Double = 0

// Casting - values are never implicitly converted to another type
let stringWithDouble = aString + String(aDouble)
let intFromDouble = Int(aDouble)

print(stringWithDouble)

// String interpolation
let description = "The Value of aDouble = \(aDouble)"
let multilineString = """
And just like python!
    Any indentation beyond the closing quotation marks is kept,
rest is discareded.
    delimiter is three "s.
"""
print(multilineString)

// Arrays
// let is pretty strong: doesn't care if arrays are declared, it's still immutable
let shoppingList = ["catfish", "water", "tulips"]
let secondElement = shoppingList[1]
print(shoppingList)
print(secondElement)

// so this is mutable.
var mutableShoppingList = shoppingList
mutableShoppingList[2] = "mango"
print(shoppingList)
print(mutableShoppingList)

// == is equality
print(shoppingList == mutableShoppingList) // this is false

// Dictionaries
// again, mutable.
var occupations = [
    "Malcolm": "Captain",
    "Kaylee": "Mechanic"
]
occupations["Jayne"] = "Public Relations"

// Dictionaries are also structs, so this also creates a copy
let immutableOccupations = occupations
immutableOccupations == occupations // true

mutableShoppingList.append("blue paint")
occupations["Tim"] = "CEO"

mutableShoppingList = []
occupations = [:]

let emptyArray = [String]()
let emptyArray2 = Array<String>()
let emptyArray3: [String] = []
let emptyArray4: Array<String> = []

// [Key: Value] is shorthand for Dictionary<Key, Value>
let emptyDictionary = [String: Double]()
let emptyDictionary2 = Dictionary<String, Double>() // same as above
var emptyMutableDictionary: [String: Double] = [:]
var explicitEmptyMutableDictionary: Dictionary<String, Double> = [:]
// same as above

/*
 Optionals: Swift feature: contains value or nil.
 */
var someOptionalString: String? = "optional"
let someOptionalString2: Optional<String> = nil
let someOptionalString3 = String?.some("optional")
let someOptionalString4 = String?.none

print(someOptionalString)
print(someOptionalString2)
print(someOptionalString3)
print(someOptionalString4)

if someOptionalString != nil {
    // I am not nil
    // to access the value of an optional that has a value,
    // use postfix operator !, which force-unwraps it.
    if someOptionalString!.hasPrefix("opt") {
        print("has the prefix")
    }
}

// Optional Chaining: result of some function of optional type -> optional.
let empty = someOptionalString?.isEmpty // Bool?

//if-var is allowed too!
if var someNonOptionalString = someOptionalString {
    someNonOptionalString = "Non optional AND mutable"
    print(someNonOptionalString)
}

// You can bind multiple optional values in one if-let statement.
// If any of the bound values are nil, the if statement does not execute.
if let first = someOptionalString, let second = someOptionalString2,
    let third = someOptionalString3, let fourth = someOptionalString4 {
    print("\(first), \(second), \(third), and \(fourth) are all not nil")
}

// if-let supports "," (comma) clauses, which can be used to
// enforce conditions on newly-bound optional values.
// Both the assignment and the "," clause must pass.
let someNumber: Int? = 7
// this means num is not nil.
if let num = someNumber, num > 3 {
    print("num is not nil and is greater than 3")
}

// So Unwrapped Optional is another type.
// Implicitly unwrapped optional — An optional value that doesn't need to be unwrapped
let unwrappedString: String! = "Value is expected."

// Here's the difference:
let forcedString = someOptionalString! // requires an exclamation mark
let implicitString = unwrappedString // doesn't require an exclamation mark


// Control Statements

// Switch: must be exhaustive, does not implicitly fall through like JS
let vegetable = "red pepper"
let vegetableComment: String
switch vegetable {
case "celery":
    vegetableComment = "Add some raisins and make ants on a log."
case "cucumber", "watercress": // match multiple values
    vegetableComment = "That would make a good tea sandwich."
case let localScopeValue where localScopeValue.hasSuffix("pepper"):
    vegetableComment = "Is it a spicy \(localScopeValue)?"
default: // required (in order to cover all possible input)
    vegetableComment = "Everything tastes good in soup."
}
print(vegetableComment)

