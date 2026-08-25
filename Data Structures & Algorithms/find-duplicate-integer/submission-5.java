class Solution {
    public int findDuplicate(int[] nums) {
        Set<Integer> numSet = new HashSet<>();
        for(int i=0;i<nums.length;i++){
            if(!numSet.contains(nums[i])){
                numSet.add(nums[i]);
            } else {
                return nums[i];
            }
        }
        return -1;
    }
}
