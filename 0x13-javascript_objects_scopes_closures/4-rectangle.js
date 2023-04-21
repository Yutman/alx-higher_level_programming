#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let w = '';
      for (let j = 0; j < this.width; j++) {
        w += 'X';
      }
      console.log(w);
    }
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }

  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }
}

module.exports = Rectangle;
