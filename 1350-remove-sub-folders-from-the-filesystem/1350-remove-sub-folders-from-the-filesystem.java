class Solution {
    public List<String> removeSubfolders(String[] folder) {
        
        Arrays.sort(folder);
        List<String> result = new ArrayList<>();
        for(String path : folder){
            if(result.isEmpty() || !path.startsWith(result.get(result.size() - 1) + "/")){
                result.add(path);
            }
        }
        return result;
    }
    
}