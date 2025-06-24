public class Solution {
    public IList<int> FindKDistantIndices(int[] nums, int key, int k) {
        HashSet<int> return_indices = new HashSet<int>();

        for (int i = 0; i < nums.Length; i++) {
            if (nums[i] == key) {
                for (int j = i - k; j < (i + k + 1); j++) {
                    if (j >= 0 && j < nums.Length) {
                        return_indices.Add(j);
                    }
                }
            }
        }

        List<int> return_list = return_indices.ToList();

        return return_list;
    }
}
