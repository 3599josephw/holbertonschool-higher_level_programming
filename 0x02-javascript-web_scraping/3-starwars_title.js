#!/usr/bin/node
const process = require('process');
const args = process.argv;
const request = require('request');

const film = 'https://swapi-api.hbtn.io/api/films/' + args[2];

request(film, function (_error, _response, body) {
  const movie = JSON.parse(body);
  console.log(movie.title);
});
