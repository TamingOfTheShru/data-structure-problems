/**
 *  Write a program to tell if a full deck of cards shuffledDeck 
 *  is a single riffle of two other halves half1 and half2.
 */

function isSingleRiffle(half1, half2, shuffledDeck) {
	var half1Index = 0,
		half2Index = 0,
		half1MaxIndex = half1.length - 1,
		half2MaxIndex = half2.length - 1;

	for (var i = 0; i < shuffledDeck.length - 1; i++) {
		var currentCard = shuffledDeck[i];
		if (half1Index <= half1MaxIndex && currentCard === half1[half1Index]) {
			half1Index++;
		} else if (half2Index <= half2MaxIndex && currentCard === half2[half2Index]) {
			half2Index++;
		} else {
			return false;
		}
	}
	return true;
}


var shuffledDeck = [
	1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
	14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
	27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
	40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52
];
var half1 = [
	26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
	40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52
];
var half2 = [
	1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
	14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25
];

var shuffleFlag = isSingleRiffle(half1, half2, shuffledDeck);
console.log(shuffleFlag)