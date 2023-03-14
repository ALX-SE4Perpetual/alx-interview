#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${filmId}`;

request(url, async(err, response, body) => {
  err && console.log(err);
	
  const charactersArray = (JSON.parse(res.body).characters);
  for (const character of charactersArray) {
    await new Promise((resolve, reject) => {
      request(character, (err, response, body) => {
        err && console.log(err);

	console.log(JSON.parse(body).name);
	resolve();
      })
    })
  }
});

