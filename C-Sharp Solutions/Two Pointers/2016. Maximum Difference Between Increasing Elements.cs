public class Solution {
    public int MaximumDifference(int[] nums) {
        var l = 0;
        var r = 1;
        var max_diff = -1;

        while (r < nums.Length) {

            if (nums[l] < nums[r]) {
                if ((nums[r] - nums[l]) > max_diff) {
                    max_diff = nums[r] - nums[l];
                }
            } else if (nums[l] > nums[r]) {
                l = r;
            }

            r++;
        }

        return max_diff;

        
    }
}
