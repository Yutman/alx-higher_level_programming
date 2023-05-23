#!/usr/bin/node

const { get } = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
get(url, (err, response, body) => {
  if (err) return;
  const { characters } = JSON.parse(body);

  characters.forEach(characterUrl => {
    get(characterUrl, (err, response, body) => {
      if (err) return;
      const { name } = JSON.parse(body);
      console.log(name);
    });
  });
});
