/**
*  struct ListNode {
*        int val;
*        struct ListNode *next;
*        ListNode(int x) :
*              val(x), next(NULL) {
*        }
*  };
*/
#include <cstddef>
#include <vector>
class Solution {
public:
    vector<int> printListFromTailToHead(ListNode* head) {
        vector<int> res;
        stack<int> s;
        while(head != NULL) {
            s.push(head->val);
            head = head->next;
        }

        while(!s.empty()){
            res.push_back(s.top());
            s.pop();
        }
        return res;
    }
};
