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
// https://stackoverflow.com/questions/16155592/negative-numbers-to-binary-string-in-javascript
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

function evalprint(expression) {
	console.log(
		"statement:", expression,
		"| result:", eval(expression),
		"| type: ", typeof eval(expression));
}

evalprint("'' + 1 + 0");
evalprint("'' - 1 + 0");
evalprint("true + false");
evalprint("6 / '3'");
evalprint("'2' * '3'");
evalprint("4 + 5 + 'px'");
evalprint("'$' + 4 + 5");
evalprint("'4' - 2");
evalprint("'4px' - 2");
evalprint("7 / 0");
evalprint("'  -9  ' + 5");
evalprint("'  -9  ' - 5"); // fuck yoooooo
evalprint("null + 1");
evalprint("undefined + 1");
// evalprint("' \t \n' - 2");


// Comparisons -------------------

evalprint("2 > 1");
evalprint("'A' < 'Z'");
evalprint("'A' < 'z'");
evalprint("'Glow' > 'Glee'");
evalprint("'Bee' > 'Be'");
evalprint("'2' > 1");
evalprint("'01' == 1");
evalprint("true == 1");
evalprint("false == 0");
evalprint("Boolean(0) == Boolean('0')");
evalprint("null == undefined");
evalprint("null === undefined");
evalprint("null > 0");
evalprint("null == 0");
evalprint("null >= 0"); // true, WTF
