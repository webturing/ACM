#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
class Solution {
 public:
  std::vector<std::string> K = {"WQERTYUIOP", "ASDFGHJKL", "ZXCVBNM"};
  size_t hash(char c) {
    for (size_t i = 0; i < K.size(); i++)
      if (count(K[i].begin(), K[i].end(), c)) return i;
  }
  std::vector<std::string> findWords(std::vector<std::string> words) {
    std::vector<std::string> v;
    for (auto word : words) {
      if (ok(word)) {
        v.push_back(word);
      }
    }
    return v;
  }
};

int main() {
  Solution sol;
  std::vector<std::string> words = {"Hello", "Alaska", "Dad", "Peace"};
  std::vector<std::string> ret = sol.findWords(words);
  std::cout << "[";
  for (auto w : ret) {
    std::cout << w << ",";
  }
  std::cout << "]" << std::endl;
  return 0;
}