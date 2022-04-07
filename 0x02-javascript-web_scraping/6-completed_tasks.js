#!/usr/bin/node
const process = require('process');
const args = process.argv;
const request = require('request');

request(args[2], function (_error, _response, body) {
  const tasks = JSON.parse(body);
  const result = {};

  for (let i = 0; i < tasks.length; i++) {
    if (tasks[i].completed === true) {
      if (tasks[i].userId in result) {
        result[tasks[i].userId] += 1;
      } else {
        result[tasks[i].userId] = 1;
      }
    }
  }
  console.log(result);
});
