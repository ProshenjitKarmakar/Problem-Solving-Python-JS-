/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
var isEmpty = function (obj) {
    if (typeof obj === 'string' || Array.isArray(obj)) {
        return obj.length === 0;
    } else if (typeof obj === 'object' && obj !== null) {
        return Object.keys(obj).length === 0;
    } else {
        return true;
    }
};


const result = isEmpty([1]);


console.log("======result=======", result);
