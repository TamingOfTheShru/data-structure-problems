/*You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true*/

/**
 * @param {number[]} flowerbed
 * @param {number} n
 * @return {boolean}
 */
var canPlaceFlowers = function(flowerbed, n) {
    let bed = flowerbed
    bed.unshift(0);
    bed.push(0);
    for(let i=1;i<bed.length;i++){
        
        if(bed[i]==0 && bed[i-1]==0 && bed[i+1]==0){
            bed[i]=1;
            n-=1;
        }
    }
    if(n<=0){
        return true;
    }
    else{
        return false;
    }
};
