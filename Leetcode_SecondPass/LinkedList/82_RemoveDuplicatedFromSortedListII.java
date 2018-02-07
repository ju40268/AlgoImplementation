/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    // O(n), O(1)     
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode dummy = new ListNode(-1);
        dummy.next = head;
        ListNode p = dummy;
        while (p.next != null && p.next.next != null){
            if (p.next.val == p.next.next.val){
                int same_num = p.next.val;
                while (p.next != null && p.next.val == same_num) p.next = p.next.next;
            }
            else p = p.next;
        }
        return dummy.next;
    }
}
