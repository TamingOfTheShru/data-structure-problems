/* Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121] */

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function(nums) {
    let start = 0, end = n = nums.length-1, sortedSquares=[];
    while(n >= 0){
        if (nums[start]*nums[start] < nums[end]*nums[end]){
            sortedSquares[n] = nums[end]*nums[end];
            end -=1;
        }
        else{
            sortedSquares[n] = nums[start]*nums[start];
            start +=1;  
        }
        n--;
    }
    return sortedSquares;  
};

