
const debounce = (fn, t) => {
    let timerId;

    return function (...args) {
        clearTimeout(timerId);
        timerId = setTimeout(() => {
            fn(...args)
        }, t)
    }
}

const log = debounce(console.log, 100);
log('Hello');
log('Hello');
log('Hello'); 