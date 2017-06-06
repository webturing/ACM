#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
class Solution {

 public:
  bool ok(std::string &k, std::string &s) {
    for (auto p : s) {
      if (count(k.begin(), k.end(), toupper(p)) == 0) {
        return false;
      }
    }
    return true;
  }
  bool ok(std::string &s) {
    std::vector<std::string> K = {"WQERTYUIOP", "ASDFGHJKL", "ZXCVBNM"};
    for (auto k : K) {
      if (ok(k, s)) {
        return true;
      }
    }
    return false;
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