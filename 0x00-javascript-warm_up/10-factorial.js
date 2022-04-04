#!/usr/bin/node
const process = require('process');

const args = process.argv;

const num = parseInt(args[2]);

if (num) {
  const result = factorial(num);
  console.log(result);
} else {
  console.log('1');
}

function factorial (num) {
  if (num < 0) {
    return -1;
  } else if (num === 0) {
    return 1;
  } else {
    return (num * factorial(num - 1));
  }
}
