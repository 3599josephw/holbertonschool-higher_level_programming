#!/usr/bin/node
const OtherSquare = require('./5-square.js');

class Square extends OtherSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      // pass
    } else {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
