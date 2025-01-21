/**
* @param {Function} fn
* @param {number} t
* @return {Function}
*/
var timeLimit = function (fn, t) {
    return async function (...args) {
        const timeoutId = new Promise((_, reject) => {
            setTimeout(() => {
                reject("Time Limit Exceeded");
            }, t);
        });

        try {
            const start = Date.now();
            const result = await Promise.race([fn(...args), timeoutId]);
            const end = Date.now();
            return { resolved: result, time: end - start };
        } catch (error) {
            return { rejected: error, time: t };
        }
    };
};

const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms