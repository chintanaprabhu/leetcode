class Solution {
    public int maxProduct(String[] words) {
        //Never write O(n^2) program!!!!!!!! time limit exceeded! 
    /*    int prod = Integer.MIN_VALUE;
        for (int i = 0; i < words.length; i++) {
            for(int j = i; j < words.length; j++) {
                int different = compare(words[i], words[j]);
                if (different > prod)
                    prod = different;
            }
        }
        return prod > Integer.MIN_VALUE ? prod : 0;
    }
    public int compare(String s1, String s2) {
        for(int i = 0; i < s1.length(); i++) {
            for(int j = 0; j < s2.length(); j++) {
                if((int)s1.charAt(i) == (int)s2.charAt(j))
                    return Integer.MIN_VALUE;
            }
        }
        return s1.length()*s2.length();*/
        //solution - use an integer of 32 bits to represent any string. Perform AND between strings to find
        // out if they are completely different from each other or not. 
        int[] arr = new int[words.length];
        int j = 0;
        int prod = 0;
        for (String word:words) {
            for(int i = 0; i < word.length(); i++)
                arr[j] = arr[j] | (1 << (word.charAt(i) - 'a'));
            j++;
        }
        for(int i = 0; i < arr.length; i++) {
            for (int k = i+1; k < arr.length; k++) {
               // System.out.println(arr[i] & arr[k]);
                if((arr[i] & arr[k]) == 0) {
                    int temp_prod = words[i].length() * words[k].length();
                    if(temp_prod > prod)
                        prod = temp_prod;
                }
            }
        }
        return prod;
    }
}
