#!/usr/bin/node

const args = process.argv;
const arr = [];

args.forEach((val, index) => {
  const n = parseInt(val);
  if (args.length > 2 && !isNaN(n)) {
    arr.push(n);
  }
});

const newArr = arr.sort((a, b) => a - b);

if (newArr.length === 0 || newArr.length === 1) {
  console.log(0);
} else {
  console.log(newArr[newArr.length - 2]);
}
