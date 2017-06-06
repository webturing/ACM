#include <string>
#include <iostream>
#include <stack>
#include <vector>
#include <cctype>
class Solution {
 public:
  std::string reverseWords(std::string s) {
    std::vector<char> ret;
    std::stack<char> v;
    for (auto p : s) {
      if (isspace(p)) {
        while (!v.empty()) {
          char c = v.top();
          ret.push_back(c);
          v.pop();
        }
        ret.push_back(p);
      } else {
        v.push(p);
      }
    }
    while (!v.empty()) {
      char c = v.top();
      ret.push_back(c);
      v.pop();
    }
    std::string t(ret.begin(), ret.end());
    return t;
  }
};
Solution solution;
int main() {
  std::string s = "Let's take LeetCode contest";
  std::cout << solution.reverseWords(s) << std::endl;
  return 0;
}