// HashTable
#include <iostream>
#include <vector>
using namespace std;
class Solution {
 public:
  vector<int> twoSum(std::vector<int>& nums, int target) {
    std::vector<int> v(2, 0);
    for (size_t i = 0; i < nums.size(); i++)
      for (size_t j = i + 1; j < nums.size(); j++) {
        if (nums[i] + nums[j] == target) {
          v[0] = i;
          v[1] = j;
          return v;
        }
      }
    return v;
  }
};

Solution solution;
int main() {
  std::vector<int> nums = {4, 5, 1, 2, 3};
  int target = 9;
  std::vector<int> ans = solution.twoSum(nums, target);
  std::cout << "[" << ans[0] << "," << ans[1] << "]" << std::endl;
  return 0;
}