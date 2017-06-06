#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
class Solution {
 public:
  int distributeCandies(std::vector<int>& candies) {
    int size = candies.size();
    std::set<int> s(candies.begin(), candies.end());
    int mx = s.size();
    if (mx * 2 <= size) return mx;
    return size / 2;
  }
};

int main() {
  Solution sol;
  std::vector<int> v = {1, 2, 3, 1, 2, 3};
  std::cout << sol.distributeCandies(v) << std::endl;
  return 0;
}