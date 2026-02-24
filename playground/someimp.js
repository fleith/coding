#!/usr/bin/env node

const total = [0, 1, 2, 3].reduce(function (sum, value) {
    return sum + value;
}, 1);

console.log(total)

// 1) Implement a MAP function

var MyMap = function (func, elements) {
    var result = new Array();
    elements.forEach((item) => {result.push(func(item))});
    return result;
};

const nice = MyMap((item) => {return item * item;}, [1, 2, 5, 6]);
console.log(nice);

// console.log(typeof MyMap);

// 2) Implement debounce function

var dbounce = function (func, wait) {
    let timeout = null;
    return function () {
        clearTimeout(timeout);
        timeout = setTimeout(func, wait);
    }
}

var log = function () {
    console.log("call function");
}

var decorated = dbounce(log, 2000);

decorated();
decorated();
decorated();
