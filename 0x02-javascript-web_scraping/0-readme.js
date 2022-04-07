#!/usr/bin/node
const fs = require('fs');
const process = require('process');
const args = process.argv;

fs.readFile(args[2], 'utf-8', (err, data) => {
  if (data) {
    console.log(data);
  } else {
    console.log(err);
  }
});
