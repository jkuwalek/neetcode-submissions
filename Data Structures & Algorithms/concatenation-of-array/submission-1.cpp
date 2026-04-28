class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> answer;
        for (int i = 0; i < 2; i++) {
            for (int num : nums) {
                answer.push_back(num);
            }
        }
        return answer;
    }
};