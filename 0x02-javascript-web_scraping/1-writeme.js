#!/usr/bin/node

const fs = require('fs');
const fd = process.argv[2];
const tw = process.argv[3];

fs.writeFile(fd, tw, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
