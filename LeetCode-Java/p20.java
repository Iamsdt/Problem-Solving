class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        Map<Character, Character> match = new HashMap<>();
        match.put('(', ')');
        match.put('[', ']');
        match.put('{', '}');

        for (char c : s.toCharArray()) {
            // If it's an opening bracket, push onto the stack
            if (match.containsKey(c)) {
                stack.push(c);
            }
            // If it's a closing bracket, check for a matching opening bracket
            else if (stack.isEmpty() || match.get(stack.pop()) != c) {
                return false;
            }
        }
        // If the stack is empty, all brackets were matched correctly
        return stack.isEmpty();
    }
}