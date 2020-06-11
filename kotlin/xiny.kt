// single line comment
/*
    multi-line comments
*/
package com.learnxinyminutes.kotlin

fun learnVariables() {
    val fooVal = 10 // cannot reassign
    var fooVar = 10 // can reassign
    fooVar = 20

    // we do have an option to explicitly declare the var type
    val foo: Int = 7
    val fooString = ""
}

fun main(args: Array<String>) {
    learnVariables()
    
}