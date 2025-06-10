public class Solution {
    public int RemoveElement(int[] nums, int val) {
        var result = 0;

        foreach (int num in nums) {
            if (num != val) {
                nums[result] = num;
                result++;
            }
        }

        return result;
    }
}
