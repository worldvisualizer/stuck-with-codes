"use strict";

// Javascript Fundamentals - All the Primitives

// Type conversions ------------
let value = true;
console.log(value = String(value));

value = '123';
console.log(value = Number(value));

console.log(Boolean("hello")); // true
console.log(Boolean("")); // false


class Foo {

}
// in order to override toString in custom object,
Foo.prototype.toString = function() {
	return `[object Foo: instance vars: ${this.var}]`;
}

// Bitwise operations -------------

function dec2bin(dec) {
    console.log((dec >>> 0).toString(2));
}

// negative numbers are in signed representation
const integerNumber = 64 + 32 + 16;
dec2bin(integerNumber & 1);
dec2bin(integerNumber | 1);
dec2bin(integerNumber ^ 1);
dec2bin(~integerNumber);
dec2bin(integerNumber << 1);
dec2bin(integerNumber >> 1);
dec2bin(integerNumber >>> 1); // zerofill right shift
// this also converts integer to unsigned form.

// modifying in place

// three operations in one line
for (let a = 1, b = 3, c = a * b; a < 10; a++) {
  // comma has a very low precedence
}

let z = 2;
let x = 1 + (z *= 2); // rightmost, highest precedence first
console.log(x);


console.log("" + 1 + 0);
console.log("" - 1 + 0);
console.log(true + false);
console.log(6 / "3");
console.log("2" * "3");
console.log(4 + 5 + "px");
console.log("$" + 4 + 5);
console.log("4" - 2);
console.log("4px" - 2);
console.log(7 / 0);
console.log("  -9  " + 5);
console.log("  -9  " - 5);
console.log(null + 1);
console.log(undefined + 1);
console.log(" \t \n" - 2);


// Comparisons -------------------

console.log("2 > 1", 2 > 1);
console.log("'A' < 'Z'", 'A' < 'Z');
console.log("'A' < 'z'", 'A' < 'z');
console.log("'Glow' > 'Glee'", 'Glow' > 'Glee');
console.log("'Bee' > 'Be'", 'Bee' > 'Be');
console.log("'2' > 1", '2' > 1);
console.log("'01' == 1", '01' == 1);
console.log("true == 1", true == 1);
console.log("false == 0", false == 0);
console.log("Boolean(0) == Boolean('0')", 
	Boolean(0) == Boolean("0"));
console.log();
console.log();
console.log();
console.log();
console.log();
console.log();
console.log();
console.log();
console.log();
console.log();
console.log();
console.log();
console.log();
console.log();