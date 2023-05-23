#!/usr/bin/node

const { get } = require('request');

get(process.argv[2], (err, response, body) => {
  if (err) return;
  console.log(`code: ${response.statusCode}`);
});
