/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function (promise1, promise2) {
    const res = promise1.then((res1) => promise2.then((res2) => {
        return new Promise((resolve, reject) => {
            resolve(res1 + res2);
        })
    }))

    return res
};


const result = addTwoPromises(Promise.resolve(2), Promise.resolve(2)); // 4

result.then((res) => console.log(res))
