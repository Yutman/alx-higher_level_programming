#!/usr/bin/node

const x = parseInt(process.argv[2]);

if (x) {
  for (let i = 0; i < x; i++) {
    let r = '';
    for (let j = 0; j < x; j++) {
      r += 'X';
    }
    console.log(r);
  }
} else {
  console.log('Missing size');
}
