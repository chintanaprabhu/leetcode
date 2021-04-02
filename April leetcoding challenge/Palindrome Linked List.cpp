/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        ListNode* midNode = head;
        ListNode* endNode = head;
        int llLen = 0;
        while(endNode != nullptr) {
            llLen++;
            midNode = midNode->next;
            endNode = endNode->next;
            if(endNode) {
                llLen++;
                endNode = endNode->next;
            }
        }
        ListNode* prev = nullptr;
        ListNode* cur = midNode;
        while(cur != nullptr) {
            ListNode* nxt = cur->next;
            cur->next = prev;
            prev = cur;
            cur = nxt;
        }
        int halfLen = llLen/2;
        while(halfLen > 0) {
            if(head->val != prev->val) {
                return false;
            }
            head = head->next;
            prev = prev->next;
            halfLen--;
        }
        return true;
    }
};  
