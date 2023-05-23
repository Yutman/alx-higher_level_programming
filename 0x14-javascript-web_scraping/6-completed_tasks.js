#!/usr/bin/node

const { get } = require('request');

const url = process.argv[2];
get(url, (err, response, body) => {
  if (!err) {
    const data = JSON.parse(body);
    const completedObj = {};

    data.forEach(({ userId, completed }) => {
      if (completed && !completedObj[userId]) {
        completedObj[userId] = 1;
      } else if (completed) {
        completedObj[userId] += 1;
      }
    });
    console.log(completedObj);
  }
});
