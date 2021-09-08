/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* reverse (ListNode* head) {
        ListNode *prev=NULL;
        ListNode* cur = head;
        while (cur != NULL) {
            ListNode* temp = cur->next;
            cur->next = prev;
            
            prev = cur;
            cur = temp;
        }
        return prev;
    }
    
    bool isPalindrome(ListNode* head) {
       /* vector<int> isPal;
        int i, j;
        while(head != NULL) {
            isPal.push_back(head->val);
            head = head->next;
        }
        for (i = 0, j = isPal.size()-1; i<j; i++, j--) {
            if(isPal.at(i) != isPal.at(j)) 
                return false;
        }
        return true;*/
        
        if(head == NULL) return true;
        
        ListNode* fast = head;
        ListNode* slow = head;
        while(fast->next != NULL && fast->next->next != NULL) {
            fast = fast->next->next;
            slow = slow->next;
        }

        ListNode* secHalf = reverse(slow->next);
        while(secHalf != NULL && (head->val == secHalf->val) ) {
            head = head->next;
            secHalf = secHalf->next;
        }
        return (secHalf==NULL);
    }
};
