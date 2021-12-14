#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    // If w or h is equal to 0 or not a positive integer, create empty object
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
};
