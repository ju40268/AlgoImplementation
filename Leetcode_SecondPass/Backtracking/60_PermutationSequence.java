class Solution {
    public String getPermutation(int n, int k) {
        // O(n), O(n)
        List<Integer> res = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            res.add(i);
        }
        int[] fact = new int[n];
        fact[0] = 1;
        for (int i = 1; i < n; i++){
            fact[i] = i * fact[i-1];
        }
        k = k - 1;
        // cause program starts from 0
        StringBuilder sb = new StringBuilder();

        for (int i = n; i > 0; i--){
            int index = k / fact[i-1];
            k = k % fact[i-1];
            sb.append(res.get(index));
            res.remove(index);
        }
        return sb.toString();
    }
}
