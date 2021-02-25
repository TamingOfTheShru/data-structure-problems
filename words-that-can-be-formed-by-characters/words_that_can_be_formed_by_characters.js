/**
 * @param {string[]} words
 * @param {string} chars
 * @return {number}
 */
var countCharacters = function(words, chars) {
    let len = 0;
    for(let i=0; i< words.length; i++){
        if (words[i].length > chars.length){
            continue;
        }
        let flag = words[i].split('').every(function(character) {
            return chars.includes(character);
        });
        console.log(flag)
        if(flag == true){
            len+=words[i].length
        }
    }
    return len;
};
