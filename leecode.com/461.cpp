#include <iostream>
class Solution {
 public:
  int hammingDistance(int x, int y) {
    int tot = 0, t = x ^ y;
    for (int i = 0; i < 31; i++) {
      tot += ((t >> i) & 1);
    }
    return tot;
  }
};
Solution solution;
int main() {
  std::cout << solution.hammingDistance(1, 4) << std::endl;
  return 0;
}