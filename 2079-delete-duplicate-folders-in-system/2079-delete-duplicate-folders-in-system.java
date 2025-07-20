class Solution {

    static class TrieNode {
        Map<String, TrieNode> children = new HashMap<>();
        boolean toDelete = false;
    }

    TrieNode root = new TrieNode();
    Map<String, List<TrieNode>> serialMap = new HashMap<>();

    public List<List<String>> deleteDuplicateFolder(List<List<String>> paths) {
        // Step 1: Build Trie
        for (List<String> path : paths) {
            insert(path);
        }

        // Step 2: Serialize subtrees
        serialize(root);

        // Step 3: Mark duplicate folders
        markDuplicates();

        // Step 4: Collect valid paths
        List<List<String>> result = new ArrayList<>();
        dfs(root, new ArrayList<>(), result);
        return result;
    }

    private void insert(List<String> path) {
        TrieNode node = root;
        for (String folder : path) {
            node = node.children.computeIfAbsent(folder, k -> new TrieNode());
        }
    }

    private String serialize(TrieNode node) {
        if (node.children.isEmpty()) return "";

        List<String> serials = new ArrayList<>();
        for (String name : new TreeSet<>(node.children.keySet())) {
            String childSerial = serialize(node.children.get(name));
            serials.add(name + "(" + childSerial + ")");
        }

        String serial = String.join("", serials);
        serialMap.computeIfAbsent(serial, k -> new ArrayList<>()).add(node);
        return serial;
    }

    private void markDuplicates() {
        for (List<TrieNode> nodes : serialMap.values()) {
            if (nodes.size() > 1) {
                for (TrieNode node : nodes) {
                    node.toDelete = true;
                }
            }
        }
    }

    private void dfs(TrieNode node, List<String> path, List<List<String>> result) {
        for (Map.Entry<String, TrieNode> entry : node.children.entrySet()) {
            String name = entry.getKey();
            TrieNode child = entry.getValue();
            if (!child.toDelete) {
                path.add(name);
                result.add(new ArrayList<>(path));
                dfs(child, path, result);
                path.remove(path.size() - 1);
            }
        }
    }
}
