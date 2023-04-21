#!/usr/bin/node

const SquareParent = require('./5-square');

class Square extends SquareParent {
  charPrint (c) {
    for (let i = 0; i < this.width; i++) {
      let r = '';
      for (let j = 0; j < this.height; j++) {
        r += c || 'X';
      }
      console.log(r);
    }
  }
}

module.exports = Square;
