class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> result = new ArrayList<>();
        int rows = matrix.length;
        if(rows==0)
        {
            return result;
        }
        int columns = matrix[0].length;
        int top = 0;
        int bottom = rows-1;
        int left = 0;
        int right = columns-1;
        int direction = 0;
        while(top<=bottom && left<=right)
        {
            if(direction == 0)
            {
                for(int i=left;i<=right;i++)
                {
                    result.add(matrix[top][i]);
                }
                top++;
                direction = 1;
            }
            else if(direction == 1)
            {
                for(int i=top;i<=bottom;i++)
                {
                    result.add(matrix[i][right]);
                }
                right--;
                direction = 2;
            }
            else if(direction == 2)
            {
                for(int i=right;i>=left;i--)
                {
                    result.add(matrix[bottom][i]);
                }
                bottom--;
                direction = 3;
            }
            else
            {
                for(int i=bottom;i>=top;i--)
                {
                    result.add(matrix[i][left]);
                }
                left++;
                direction = 0;
            }
            
            
        }
        return result;
        
    }
}
