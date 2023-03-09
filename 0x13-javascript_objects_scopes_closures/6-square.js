#!/usr/bin/node

module.exports = class Square extends require("./5-square") {
  charPrint(c) {
    const chara = c ? c : "X";
    for (let i = 0; i <= this.height; i++) {
      console.log(chara.repeat(this.width));
    }
  }
};
