#!/usr/bin/node
const array = process.argv.slice(2).map((x) => {
  return Number(x);
});
array.sort((a, b) => {
  return a - b;
});
if (array.length > 1) {
  console.log(array[array.length - 2]);
} else {
  console.log(0);
}
