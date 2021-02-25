/**
 * Initialize your data structure here.
 */
var MyHashSet = function() {
    this.myHash = [];
};

/** 
 * @param {number} key
 * @return {void}
 */
MyHashSet.prototype.add = function(key) {
    if(this.myHash.includes(key)){
        return null
    }
    else{
        this.myHash.push(key);
    }    
};

/** 
 * @param {number} key
 * @return {void}
 */
MyHashSet.prototype.remove = function(key) {
    if(this.myHash.length == 0){
        return null
    }
    if(this.myHash.includes(key)){
        for(let i=0;i<this.myHash.length;i++){
            if(this.myHash[i] == key){
                this.myHash.splice(i, 1);
            }
        }
    }
};

/**
 * Returns true if this set contains the specified element 
 * @param {number} key
 * @return {boolean}
 */
MyHashSet.prototype.contains = function(key) {
    if(this.myHash.length == 0){
        return false
    }
     if(this.myHash.includes(key)){
        return true;
    }else{
        return false
    }
};

/** 
 * Your MyHashSet object will be instantiated and called as such:
 * var obj = new MyHashSet()
 * obj.add(key)
 * obj.remove(key)
 * var param_3 = obj.contains(key)
 */


/* ["MyHashSet","add","add","contains","contains","add","contains","remove","contains"]
[[],[1],[2],[1],[3],[2],[2],[2],[2]] */
