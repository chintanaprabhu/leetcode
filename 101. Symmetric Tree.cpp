/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool checkSymmetry(TreeNode* subTree1, TreeNode* subTree2) {
        if(subTree1 == NULL && subTree2 == NULL) 
            return true;
        if(subTree1 == NULL || subTree2 == NULL) 
            return false;
        return (subTree1->val == subTree2->val) 
            && checkSymmetry(subTree1->right, subTree2->left) 
            && checkSymmetry(subTree1->left, subTree2->right);
    }
    
    bool isSymmetric(TreeNode* root) {
        if (root == NULL)
            return true;
        return (checkSymmetry(root, root));
    }
};
