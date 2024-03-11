#!/usr/bin/node

const arg = process.argv[2];

const convertedNumber = parseInt(arg);

if (!isNaN(convertedNumber)) {
  console.log('My number: ${convertedNumber}');
} else {
  console.log('Not a number');
}
