class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder res = new StringBuilder();
        int i = 0;
        
        // Merge characters alternately until the shorter string ends
        while (i < word1.length() && i < word2.length()) {
            res.append(word1.charAt(i));
            res.append(word2.charAt(i));
            i++;
        }
        
        // Append remaining characters from word1 if any
        if (i < word1.length()) {
            res.append(word1.substring(i));
        }
        
        // Append remaining characters from word2 if any
        if (i < word2.length()) {
            res.append(word2.substring(i));
        }
        
        return res.toString();
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        String result = solution.mergeAlternately("abcdef", "pqr");
        System.out.println(result);
    }
}