#include <iostream>
#include <vector>
#include <algorithm>
class Solution {
 public:
  int arrayPairSum(std::vector<int>& nums) {
    sort(nums.begin(), nums.end());
    int tot = 0;
    for (size_t i = 0; i < nums.size(); i += 2) {
      tot += nums[i];
    }
    return tot;
  }
};

int main() {
  Solution sol;
  std::vector<int> v = {1, 4, 2, 3};
  std::cout << sol.arrayPairSum(v) << std::endl;
  return 0;
}