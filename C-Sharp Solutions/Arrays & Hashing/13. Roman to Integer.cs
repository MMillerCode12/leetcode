public class Solution {
    public int RomanToInt(string s) {
        var int_sum = 0;
        Dictionary<char, int> roman_dict = new Dictionary<char, int>{
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}
        };

        for (int i = 0; i < s.Length; i++) {
            if ((i + 1) < s.Length) {
                if (roman_dict[s[i]] < roman_dict[s[i + 1]]) {
                    int_sum -= roman_dict[s[i]];
                } else {
                    int_sum += roman_dict[s[i]];
                }
            } else {
                int_sum += roman_dict[s[i]];
            }
        }

        return int_sum;

    }
}
