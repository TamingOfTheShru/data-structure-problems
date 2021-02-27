/* Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4 */

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    if(nums.length==1){
        if(target==nums[0]){
            return 0
        }
        else{
            return -1
        }
    }
    let l=0, h=nums.length-1;
    let index = binarySearch(nums, l, h, target);
    return index;
};

function binarySearch(arr, l, h, key){
    if(l>h){
        return -1
    }
    let mid = parseInt((l+h)/2);
    if(key==arr[mid]){
        return mid;
    }
    if(arr[l]<=arr[mid]){
        if(key>=arr[l] && key<=arr[mid]){
            return binarySearch(arr, l, mid-1, key)
        }
        return binarySearch(arr, mid+1, h, key)
   }
    if(key>=arr[mid]&&key<=arr[h]){
        return binarySearch(arr, mid, h, key);
    }
    return binarySearch(arr, l, mid-1, key)
}
