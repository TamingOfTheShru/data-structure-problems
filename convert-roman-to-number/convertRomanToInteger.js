/* Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
  For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. */

/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
	var values = {
		"I": 1,
		"V": 5,
		"X": 10,
		"L": 50,
		"C": 100,
		"D": 500,
		"M": 1000
	}
    var strArr = s.split('')
    if(s == null) return -1;
    var num = values[strArr[0]]; //10
    var pre, curr;
    for(var i = 1; i < strArr.length; i++){
        curr = values[strArr[i]]; //100
        pre = values[strArr[i-1]]; //10
        console.log(curr, pre)
        if (curr <= pre){
            num += curr; 
        } else {
            num = num - pre*2 + curr; 
        }
    }
    return num;
}
	 
