public class Solution {
    public int LongestConsecutive(int[] nums) {
        HashSet<int> num_set = new HashSet<int>(nums);
        int longest_seq = 0;

        foreach (int num in num_set) {
            if (num_set.Contains(num - 1)) {
                continue;
            } else {
                int temp_num = num;
                int current_len = 0;

                while (num_set.Contains(temp_num)) {
                    current_len++;
                    temp_num++;
                }

                if (current_len > longest_seq) {
                    longest_seq = current_len;
                }
            }
        }

        return longest_seq;

    }
}
