#!/usr/bin/node

const { get } = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
get(url, (err, response, body) => {
  if (err) return;
  const { characters } = JSON.parse(body);

  for (let i = 0; i < characters.length; i++) {
    get(characters[i], (err, response, body) => {
      if (err) return;
      const { name } = JSON.parse(body);
      console.log(name);
    });
  }
});
