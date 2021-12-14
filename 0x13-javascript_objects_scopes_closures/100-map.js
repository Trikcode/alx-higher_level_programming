#!/usr/bin/node
const list = require('./100-data').list;
const map1 = list.map((x, i) => i * x);
console.log(list);
console.log(map1);
