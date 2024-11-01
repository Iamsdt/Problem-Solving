class Solution {
    public boolean isAnagram(String s, String t) {
        // If lengths are different, they can't be anagrams
        if (s.length() != t.length()) {
            return false;
        }

        // Create a HashMap to count characters in s
        Map<Character, Integer> count = new HashMap<>();

        // Count each character in s
        for (char charInS : s.toCharArray()) {
            count.put(charInS, count.getOrDefault(charInS, 0) + 1);
        }

        // Decrement the count for each character in t
        for (char charInT : t.toCharArray()) {
            if (count.containsKey(charInT)) {
                count.put(charInT, count.get(charInT) - 1);
                if (count.get(charInT) == 0) {
                    count.remove(charInT);
                }
            } else {
                return false;
            }
        }

        // If the map is empty, s and t are anagrams
        return count.isEmpty();
    }
}