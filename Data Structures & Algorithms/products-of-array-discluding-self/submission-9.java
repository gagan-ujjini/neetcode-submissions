class Solution {
    public int[] productExceptSelf(int[] nums) {
        int result[] = new int[nums.length];

        // Step 1: left-to-right pass — fill result[i] with prefix product (everything before i)
        result[0] = 1;  // nothing to the left of index 0
        for(int i=1;i<nums.length;i++){
            result[i] = result[i-1] * nums[i-1];
        }

        // Step 2: right-to-left pass — multiply in the suffix product (everything after i)
        int suffix = 1; // nothing to the right of the last index
        for(int i=nums.length-1;i>=0;i--){
            result[i] = result[i] * suffix;
            suffix = suffix * nums[i];
        }

        return result;
    }
}  
