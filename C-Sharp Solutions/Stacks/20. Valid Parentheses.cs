public class Solution {
    public bool IsValid(string s) {
        Dictionary<char, char> dict_keys = new Dictionary<char, char>{
            {'(', ')'},
            {'[', ']'},
            {'{', '}'} 
        };

        Stack<char> parentheses_stack = new Stack<char>();

        foreach (char letter in s) {
            if (dict_keys.ContainsKey(letter)) {
                parentheses_stack.Push(letter);
            } else {
                if (parentheses_stack.Count == 0) {
                    return false;
                } else {
                    if (dict_keys[parentheses_stack.Pop()] != letter) {
                        return false;
                    }
                }
            }
        }

        if (parentheses_stack.Count > 0) {
            return false;
        }

        return true;

    }
}
