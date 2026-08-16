class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> hashmap = new HashMap<>(); //value: index
        for(int i = 0; i<nums.length; i++){
            int diff = target - nums[i];
            if(hashmap.containsKey(diff)){
                return new int[]{hashmap.get(diff), i};
            }else{
                hashmap.put(nums[i], i);
            }
        }
        return new int[]{}; // no solution found
    }
}