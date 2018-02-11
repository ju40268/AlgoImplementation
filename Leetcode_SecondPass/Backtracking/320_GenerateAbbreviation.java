class Solution {
    // "word" ==> ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
    public static List<String> generateAbbreviations(String word) {
        List<String> res = new ArrayList<>();
        helper(res, word, "", 0, 0);
        return res;

    }

    private static void helper(List<String> res, String word, String current, int position, int count) {
        if (position == word.length()){
            if (count > 0) current += count;
            res.add(current);

        }else{
            helper(res, word, current, position+1, count+1);
            helper(res, word, current + (count > 0 ? count: "") + word.charAt(position), position+1, 0);
        }
    }
}