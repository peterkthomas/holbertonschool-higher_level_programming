#!/usr/bin/node
const phrase = 'X';
const x = process.argv[2];
if (parseInt(x)) {
  for (let iter = 0; iter < x; iter++) {
    console.log(phrase.repeat(x));
  }
} else {
  console.log('Missing size');
}
