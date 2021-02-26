/* Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

 

Example 1:

Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.*/

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var checkPossibility = function(nums) {
    let flag = false;
    for(let i=1;i<nums.length;i++){
        if(nums[i]<nums[i-1]){
            if(flag){
                return false
            }
            if(i>=2 && nums[i]<nums[i-2]){
                nums[i] = nums[i-1]
            }
            flag = true
        }
    }
    return true
};
