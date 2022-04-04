#!/usr/bin/node
const process = require('process');

const args = process.argv;

if (args.length === 2) {
  console.log('0');
} else if (args.length === 3) {
  console.log('0');
} else {
  const numbs = args.map(function (x) {
    return parseInt(x, 10);
  });
  numbs.sort().reverse();
  console.log(numbs[3]);
}
