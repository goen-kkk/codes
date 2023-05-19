#include <cstddef>
class Solution {
public:
    ListNode* ReverseList(ListNode* pHead) {
		ListNode* pnode = pHead;
		if(pHead==NULL || pHead->next==NULL) {
			return pnode;
		}
		ListNode* qnode = pnode->next;
		while(qnode!=NULL){
			pHead->next=qnode->next;
			qnode->next = pnode;
			pnode = qnode;
			qnode = pHead->next;
		}
		return pnode;
    }
};
