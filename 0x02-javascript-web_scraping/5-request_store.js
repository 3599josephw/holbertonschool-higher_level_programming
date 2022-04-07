#!/usr/bin/node
const process = require('process');
const args = process.argv;
const request = require('request');
const fs = require('fs');

request(args[2], function (_error, _response, body) {
  fs.writeFile(args[3], body, err => {
    if (err) {
      console.log(err);
    }
  });
});
