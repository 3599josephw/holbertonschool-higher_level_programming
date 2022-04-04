#!/usr/bin/node
const process = require('process');

const args = process.argv;

const a = parseInt(args[2]); const b = parseInt(args[3]);
const sum = add(a, b);
console.log(sum);

function add (a, b) {
  return a + b;
}
