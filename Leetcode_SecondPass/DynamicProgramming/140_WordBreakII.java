class Solution {
    // TLE     
    private static HashMap<Integer, List<String>> map = new HashMap<>();
    public static List<String> wordBreak(String s, List<String> wordDict) {
        return dfs(s, wordDict, 0);
    }

    private static List<String> dfs(String s, List<String> wordDict, int start) {
        if (map.containsKey(s)) return map.get(s);
        List<String> res = new ArrayList<>();
        if (start == s.length()){
            res.add("");
        }
        for (int end = start+1; end <= s.length(); end++){
            if (wordDict.contains(s.substring(start,end))){
                List<String> current = dfs(s, wordDict, end);
                for (String element : current){
                    res.add(s.substring(start, end) + (element.equals("") ? "": " ") + element);
                }
            }

        }
        map.put(start, res);
        return res;
    }
}