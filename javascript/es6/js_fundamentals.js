// Javascript Fundamentals

// Type conversions
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

// bitwise operations

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
for (a = 1, b = 3, c = a * b; a < 10; a++) {
  // comma has a very low precedence
}

let a = 2;
let x = 1 + (a *= 2); // rightmost, highest precedence first

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

