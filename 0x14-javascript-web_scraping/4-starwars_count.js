#!/usr/bin/node

const { get } = require('request');

const url = process.argv[2];
get(url, (err, response, body) => {
  if (err) return;
  const { results } = JSON.parse(body);
  const newResults = results.map(({ characters }) => {
    return characters.find(character => {
      const charArr = character.split('/');
      return Number(charArr[charArr.length - 2]) === 18;
    });
  });
  console.log(newResults.filter(Boolean).length);
});
