#!/usr/bin/node
const fs = require('fs');
const theFile = process.argv[2];
fs.readFile(theFile, 'utf-8', function (error, data) {
  if (error) console.log(error);
  else console.log(data);
});
