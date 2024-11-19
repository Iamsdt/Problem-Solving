import java.util.HashMap;
import java.util.HashSet;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashSet<Character> window = new HashSet<>();
        int l = 0;
        int res = 0;
        for (int i = 0; i < s.length(); i++) {
            while (window.contains(s.charAt(i))) {
                window.remove(s.charAt(l));
                l++;
            }
            window.add(s.charAt(i));
            res = Math.max(res, i - l + 1);
        }
        return res;
    }
}

class Solution3 {
    public int lengthOfLongestSubstring(String s) {
        if (s.length() <= 1) {
            return s.length();
        }

        HashMap<Character, Integer> di = new HashMap<>();
        int maxLength = 0;
        int start = 0;

        for (int i = 0; i < s.length(); i++) {
            if (di.containsKey(s.charAt(i)) && start <= di.get(s.charAt(i))) {
                start = di.get(s.charAt(i)) + 1;
            } else {
                int length = i - start + 1;
                maxLength = Math.max(length, maxLength);
            }
            di.put(s.charAt(i), i);
        }
        return maxLength;
    }
}

class Solution2 {
    public int lengthOfLongestSubstring(String s) {
        int ans = 0;
        for (int i = 0; i < s.length(); i++) {
            for (int j = i; j < s.length(); j++) {
                if (allUnique(s, i, j)) {
                    ans = Math.max(ans, j - i);
                }
            }
        }
        return ans;
    }

    private boolean allUnique(String s, int start, int end) {
        HashSet<Character> values = new HashSet<>();
        for (int i = start; i < end; i++) {
            char c = s.charAt(i);
            if (values.contains(c)) {
                return false;
            }
            values.add(c);
        }
        return true;
    }
}
