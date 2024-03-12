#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) {
      return {}; // Return an empty object if width or height is not a positive integer
    }
    this.width = w;
    this.height = h;
  }

  print() {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;

