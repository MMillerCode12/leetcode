class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        most_freq = [[] for i in range(len(nums) + 1)]
        return_list = []

        for i in count:
            most_freq[count[i]].append(i)

        print(most_freq)
        
        for i in range(len(most_freq) - 1, 0, -1):

            for j in most_freq[i]:
                return_list.append(j)

                if len(return_list) >= k:
                    return return_list
