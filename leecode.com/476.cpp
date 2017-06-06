#include <iostream>
#include <vector>
#include <algorithm>
class Solution {
 public:
  int findComplement(int num) {
    int ret = 0, len = 0;
    for (int t = num; t; t >>= 1) ++len;
    for (int i = len - 1; i >= 0; i--) {
      ret = (ret << 1) + (((num >> i) & 1) ^ 1);
    }
    return ret;
  }
};

int main() {
  Solution sol;
  std::cout << sol.findComplement(2) << std::endl;
  return 0;
}