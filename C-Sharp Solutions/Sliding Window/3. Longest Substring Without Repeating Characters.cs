public class Solution {
    public int LengthOfLongestSubstring(string s) {
        int left = 0;
        int max_length = 0;
        HashSet<char> substring = new HashSet<char>();

        for (int right = 0; right < s.Length; right++) {

            while (substring.Contains(s[right])) {
                substring.Remove(s[left]);
                left++;
            }

            substring.Add(s[right]);

            if (substring.Count > max_length) {
                max_length = substring.Count;
            }
        }

        return max_length;
    }
}
