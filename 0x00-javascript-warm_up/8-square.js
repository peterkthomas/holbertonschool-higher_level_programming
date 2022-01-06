#!/usr/bin/node
const item = 'X';
const x = process.argv[2];
if (parseInt(x)) {
  for (let iter = 0; iter < x; iter++) {
    console.log(phrases.repeat(item));
  }
} else {
  console.log('Missing size');
}
