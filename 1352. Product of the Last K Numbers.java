class ProductOfNumbers {
    ArrayList<Integer> prod;
    public ProductOfNumbers() {
        add(0);
    }
    
    public void add(int num) {
        if(num > 0) {
            //save the product of all n numbers at position n
            int newProd = prod.get(prod.size()-1);
            prod.add(newProd*num);
        }
        else {
            //clear the arrayList if the element to be added is 0 
            prod = new ArrayList();
            prod.add(1);
        }
    }
    
    public int getProduct(int k) {
        int size = prod.size();
        return k < size ? prod.get(size-1) / prod.get(size-k-1) : 0;
    }
}

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * ProductOfNumbers obj = new ProductOfNumbers();
 * obj.add(num);
 * int param_2 = obj.getProduct(k);
 */
