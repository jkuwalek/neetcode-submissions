class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int left = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != nums[i+1]) {
                nums[left++] = nums[i];
            }
        }
        return left;
    }
};