/* Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2] */

/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    // let numsSorted = nums.sort();
    // console.log(numsSorted);
    if(nums.length==0 || nums.length<2){
        return;
    }
    if(nums.length==2){
        if(nums[0]==nums[1]){
            return;
        }
        else if(nums[0]>nums[1]){
            let t=nums[0];
            nums[0]=nums[1]
            nums[1]=t
            return nums;
        }
        else{
            return;
        }
    }
    let numsDict={}, j=0,k=0;
    for(let i=0;i<nums.length;i++){
        if(numsDict[nums[i]]){
            numsDict[nums[i]]++;
        }
        else{
            numsDict[nums[i]]=1
        }
    }
    let keysLen=Object.keys(numsDict);
    while(j<=2){
        if(numsDict[j] && numsDict[j]!=0){
            nums[k++]=j;
            numsDict[j] = numsDict[j]-1;
            console.log(nums, numsDict)
        }else{
            j++;
        }
    }
};
