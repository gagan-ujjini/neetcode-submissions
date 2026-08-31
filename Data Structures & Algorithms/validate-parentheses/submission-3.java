class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> hashMap = new HashMap<>();
        hashMap.put(')', '(');
        hashMap.put(']', '[');
        hashMap.put('}', '{');

        Deque<Character> stack = new ArrayDeque<>();
        for (char c : s.toCharArray()){
            if(hashMap.containsKey(c)){
                //c is a closing bracket
                if(stack.isEmpty() || stack.pop() != hashMap.get(c)){
                    return false;
                }
            } else {
                stack.push(c);
            }
        }
        return stack.isEmpty();
    }
}
