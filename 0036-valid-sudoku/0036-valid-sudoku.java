class Solution {
    public boolean isValidSudoku(char[][] board) {
        HashSet<Character>[] rows = new HashSet[9];
        HashSet<Character>[] cols = new HashSet[9];
        HashSet<Character>[][] boxes = new HashSet[3][3];

        for(int i = 0; i < 9; i++){
            rows[i] = new HashSet<>();
            cols[i] = new HashSet<>();
        }

        for(int i = 0; i < 3; i++){
            for (int j = 0; j < 3; j++){
                boxes[i][j] = new HashSet<>();
            }
        }

        for(int i = 0; i < 9; i++){
            for (int j = 0; j < 9; j++){
                char ch = board[i][j];

                if(ch == '.') continue;

                if(rows[i].contains(ch)) return false;
                rows[i].add(ch);

                if(cols[j].contains(ch)) return false;
                cols[j].add(ch);

                if(boxes[i/3][j/3].contains(ch)) return false;
                boxes[i/3][j/3].add(ch);
            }
        }
        return true;
        
    }
}