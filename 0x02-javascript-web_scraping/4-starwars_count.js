#!/usr/bin/node
const process = require('process');
const args = process.argv;
const request = require('request');

request(args[2], function (_error, _response, body) {
  const list = JSON.parse(body);
  let count = 0;
  for (let i = 0; i < 7; i++) {
    if (list.results[i].characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
      count++;
    }
  }
  console.log(count);
});
