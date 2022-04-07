#!/usr/bin/node
const request = require('request');
const process = require('process');
const args = process.argv;

request(args[2], function (_error, response) {
  console.log('code:', response.statusCode);
});
