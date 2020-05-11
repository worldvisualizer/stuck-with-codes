// Functional Programming with JS, Luis Atencio

// Chapter 1: Becoming Functional

// Properties of Functional Programming
/*
    1) Declarative Programming
    2) Pure Functions
    3) Referential Transparency
    4) Immutability of Input 
*/

// Declarative Programming:
// Separates program description from evaluation

[1,2,3].map((num) => {
	return Math.pow(num, 2);
}); // don't have to care about loop counter

// Pure Functions
// Depends only on the input provided and not on any hidden or external state
// Does not inflict changes beyond its scope, such as modifying parameter by ref.