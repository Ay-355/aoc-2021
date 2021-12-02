const fs = require("fs");

const partOne = (numbers: number[]): number => {
  let amount: number = 0;
  for (let i = 0; i < numbers.length; i++) {
    if (i > 0 && numbers[i] > numbers[i - 1]) {
      amount++;
    }
  }
  return amount;
};

const partTwo = (numbers: number[]): number => {
  let nums: number[] = [];
  for (let i = 0; i < numbers.length - 2; i++) {
    nums.push(
      numbers.slice(i, i + 3).reduce(function (a, b) {
        return a + b;
      })
    );
  }
  return partOne(nums);
};

let numbers: number[] = fs
  .readFileSync("input.txt", "utf-8")
  .split("\n")
  .map(Number);

console.log(`Part One: ${partOne(numbers)}`);
console.log(`Part Two: ${partTwo(numbers)}`);
