/** Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]] */

/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function(matrix) {
    transpose(matrix);
    reverse(matrix);
};

function transpose(matrix){
    let n = matrix.length;
    for(let i=0;i<n;i++){
        for(let j=i;j<n;j++){
            let temp = matrix[i][j];
            matrix[i][j] = matrix[j][i];
            matrix[j][i] = temp
        }
    }
    console.log(matrix)
}

function reverse(matrix){
    let n = matrix.length;
     for(let i=0;i<n;i++){
         matrix[i].reverse();
     }
    console.log(matrix);
}
