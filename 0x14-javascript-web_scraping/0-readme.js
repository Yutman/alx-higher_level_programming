#!/usr/bin/node

const { readFile } = require('fs');

readFile(process.argv[2], 'utf-8', (err, res) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(res);
});
