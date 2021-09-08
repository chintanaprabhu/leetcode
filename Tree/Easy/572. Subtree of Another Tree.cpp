/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        if (!root) {
            return false;
        }
        if ((root->val == subRoot->val) && isSubtreeHelper(root, subRoot)) {
            return true;
        }
        if (isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot)) {
            return true;
        }
        return false;
    }
    
    bool isSubtreeHelper(TreeNode* root, TreeNode* subRoot) {
        if (!root && !subRoot) {
            return true;
        }
        if (root && subRoot) {
            if (root->val != subRoot->val) {
                return false;
            }
            if (isSubtreeHelper(root->left, subRoot->left) && isSubtreeHelper(root->right, subRoot->right)) {
                return true;
            }
        }
        return false;
    }
};
