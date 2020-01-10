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
    bool hasCycle(ListNode *head) {
        //O(n) space complexity 
       /* map<ListNode*, bool> visited;
        while(head != NULL) {
            cout<< "insterted: " << head << endl;
            auto find = visited.find(head);
            if(find != visited.end()) {
                return true;
            }
            else {
                visited.insert(pair<ListNode*, bool>(head, true));
            }
            head = head->next;
        }
        return false;*/
        /***************************************/
        //Using two pointers
        ListNode *fast = head, *slow = head;
        while(fast != NULL && fast->next != NULL) {
            fast = fast->next->next;
            slow = slow->next;
            if(fast == slow)
                return true;
            }
        return false;
    }
};
