/*Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]*/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function(nums, target) {
    if(nums.length ==0){
        return [-1,-1]
    }
    if(nums.length == 1){
        if(nums[0]==target){
            return [0,0]
        }else{
            return [-1,-1]
        }
    }
    let ans=[];
    for(let i=0;i<=nums.length-1;i++){
        if(target==nums[i]){
            ans.push(i)
        }
    }
    if(ans.length!=0){
        if(ans.length==1){
            ans.push(ans[0])
        }
        if(ans.length>2){
            ans = [ans[0], ans[ans.length-1]];
        }
        return ans;
    }
    else{
        return [-1,-1]
    }  
};
