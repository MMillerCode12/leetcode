class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        sorted_str = {}
        return_strs = []

        for i in strs:
            temp_sort = "".join(sorted(i))

            if temp_sort in sorted_str:
                sorted_str[temp_sort].append(i)
            else:
                sorted_str[temp_sort] = [i]

        return list(sorted_str.values())
