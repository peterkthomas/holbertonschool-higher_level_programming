#!/usr/bin/node
const x = process.argv[2];
const phrase = 'C is fun';
let i = 0;

if (parseInt(x)) {
  while (i < x) {
    console.log(phrase);
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
