class Solution {
    public int[] queryResults(int limit, int[][] queries) {
        Map<Integer , Integer> ballColors = new HashMap<>();
        Map<Integer, Integer> colorFrequency = new HashMap<>();        
        List<Integer> result = new ArrayList<>();
        int distinctColorCount = 0;

        for(int[] query : queries){
            int ball = query[0];
            int color = query[1];

            if(ballColors.containsKey(ball)){
                int oldColor = ballColors.get(ball);
                colorFrequency.put(oldColor, colorFrequency.get(oldColor) - 1);


                if(colorFrequency.get(oldColor) == 0){
                    colorFrequency.remove(oldColor);
                    distinctColorCount--;

                }
            }

            ballColors.put(ball, color);
            colorFrequency.put(color, colorFrequency.getOrDefault(color, 0) + 1);

            if (colorFrequency.get(color) == 1) {
                distinctColorCount++;
            }

            result.add(distinctColorCount);
        }
        
        return result.stream().mapToInt( i -> i).toArray();
    }
}