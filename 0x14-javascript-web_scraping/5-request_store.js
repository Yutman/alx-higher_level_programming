#!/usr/bin/node

const { get } = require('request');
const { writeFile } = require('fs');
const url = process.argv[2];
get(url, (err, response, body) => {
  if (err) return;
  writeFile(process.argv[3], body, (err, res) => {
    if (err) {
      console.log(err);
    }
  });
});
