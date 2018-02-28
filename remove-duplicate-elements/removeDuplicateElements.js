/**
 * Given a sorted array, remove the duplicates in-place such that each element appear
 * only once and return the new length.
 */

"use strict"
var nums = [1, 1, 2, 2, 3];

function removeDuplicates(nums) {
	if (nums === null || nums.length === 0) return 0;
	if (nums.length == 1) return 1;
	var count = 0,
		newNums = [];
	for (var i = 0; i < nums.length; i++) {
		if (nums[i] != nums[i + 1]) {
			count++;
			newNums.push(nums[i]);
		}
	}
	console.log("new array: ", newNums)
	return newNums;
};

removeDuplicates(nums);