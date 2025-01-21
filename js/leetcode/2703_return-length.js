/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function (...args) {
    const arguments = [...args]
    return arguments?.length
};

const res = argumentsLength(3, ['wef', 'efew'], null, 'wxxx', {}); // 3

console.log("======res======", res);
