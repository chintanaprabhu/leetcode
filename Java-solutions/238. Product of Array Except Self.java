class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] output = new int[nums.length];
        output[0] = 1;
        for (int i = 1; i < nums.length; i++) {
            output[i] = nums[i-1] * output[i-1];
        }
        int R = 1;
        for (int i = nums.length-1; i >= 0; i--){
            output[i] = output[i] * R;
            R = R * nums[i];
        }
        return output;
    }
}
