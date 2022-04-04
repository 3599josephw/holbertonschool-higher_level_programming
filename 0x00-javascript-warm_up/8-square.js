#!/usr/bin/node
const process = require('process');

const args = process.argv;

if (Number(args[2])) {
  for (let i = 0; i < args[2]; i++) {
    console.log('X'.repeat(args[2]));
  }
} else {
  console.log('Missing size');
}
