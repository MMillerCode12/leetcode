public class Solution {
    public IList<IList<int>> Generate(int numRows) {

        var return_list = new List<IList<int>>();

        for (int i = 0; i < numRows; i++) {
            
            var new_list = new List<int>();
            
            for (int j = 0; j <= i; j++){ 
                if (j == 0|| j == i){
                    new_list.Add(1);
                } else {
                    new_list.Add((return_list[i - 1][j - 1]) + (return_list[i - 1][j]));
                }
            }
            
            return_list.Add(new_list);

        }
        
        return return_list;

    }
}
