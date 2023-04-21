#!/usr/bin/node

function fact (n) {
  if (n === 1 || !n) {
    return 1;
  } else {
    return n * fact(n - 1);
  }
}

console.log(fact(parseInt(process.argv[2])));
