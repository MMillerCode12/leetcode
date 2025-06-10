public class Solution {
    public int RemoveDuplicates(int[] nums) {
        var k = 0;
        var current_num = nums[0];

        foreach (int num in nums) {
            if (num != current_num) {
                nums[k] = current_num;
                current_num = num;
                k++;
            }
        }

        nums[k] = current_num;
        k++;
        
        return k;

    }
}
