#include <iostream>
#include <vector>
#include <fstream>
#include <string>

int partOne(std::vector<int> numbers)
{
  int amount = 0;
  for(int i = 0; i < numbers.size(); i++) {
    if (i > 0 && numbers[i] > numbers[i - 1]) {
      amount++;
    }
  }
  return amount;
}


int sum(std::vector<int> numbers, int index) { 
  int sum = 0;
  std::vector<int> nums;
  for (int j = 0 + index; j < 3 + index; j++) {
    nums.push_back(numbers[j]);
  }
  for (auto& n : nums)
    sum += n;
  return sum;
}

int partTwo(std::vector<int> numbers)
{ 
  std::vector<int> nums;
  for(int i = 0; i < numbers.size() - 2 ; i++) {
    nums.push_back(sum(numbers, i));
  }
  return partOne(nums);
}


int main (int argc, char *argv[])
{
  std::ifstream input("input.txt");
  std::string line;
  std::vector<int> numbers; 
  while (std::getline(input, line)) {
    numbers.push_back(std::stoi(line));
  }
  std::cout << "Part One: " << partOne(numbers) << std::endl;
  std::cout << "Part Two: " << partTwo(numbers) << std::endl;
  return 0;
}
