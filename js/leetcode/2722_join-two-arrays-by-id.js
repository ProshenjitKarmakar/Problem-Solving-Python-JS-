/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
// var join = function (arr1, arr2) {
//     let joinedArray = [];

//     arr1.map((item) => {
//         joinedArray.push(item)
//     })

//     arr2.map((item) => {
//         let isExists = joinedArray.find((s) => s.id === item.id);

//         if (isExists) {
//             console.log("===isExists===", isExists);
//             joinedArray = joinedArray.filter((f) => f.id !== item.id)
//         }
//         joinedArray.push(item)
//     })

//     joinedArray = joinedArray.sort((a, b) => a.id - b.id)

//     console.log("=======joinedArray======", joinedArray)

//     return joinedArray;
// };



var join = function (arr1, arr2) {
    const map = new Map();

    for (const item of arr1) {
        map.set(item.id, { ...item });
    }

    for (const item of arr2) {
        if (map.has(item.id)) {
            map.set(item.id, { ...map.get(item.id), ...item });
        } else {
            map.set(item.id, { ...item });
        }
    }

    const joinedArray = Array.from(map.values()).sort((a, b) => a.id - b.id);

    return joinedArray;
};


const arr1 = [
    { "id": 1, "x": 2, "y": 3 },
    { "id": 2, "x": 3, "y": 6, "z": 8 },
    { "id": 5, "x": 3, "y": 6 }
]
const arr2 = [
    { "id": 2, "x": 10, "y": 20 },
    { "id": 4, "x": 0, "y": 0 },
    { "id": 3, "x": 0, "y": 0 }
]

join(arr1, arr2)