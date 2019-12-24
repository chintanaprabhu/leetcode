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
    bool isSubtree(TreeNode* s, TreeNode* t) {
        if(check(s, t))
            return true;
        if(s && s->left && isSubtree(s->left, t))
            return true;
        if(s && s->right && isSubtree(s->right, t))
            return true;
        return false;
    }
    
    bool check(TreeNode* s, TreeNode* t){
        if(s==NULL && t==NULL)
            return true;
        if(s==NULL || t==NULL)
            return false;
        if(s->val != t-> val)
            return false;
        if(!check(s->left, t->left))
            return false;
        if(!check(s->right, t->right))
            return false;
        return true;
    }
};
