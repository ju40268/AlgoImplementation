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
    // Solution 1
    public ListNode removeElements(ListNode head, int val) {
        if (head == null) return head;
        
        ListNode dummy = new ListNode(-1);
        dummy.next = head;
        
        ListNode p = dummy;
        while (p.next != null){
            if (p.next.val == val) p.next = p.next.next;
            else p = p.next;
        }
    
        return dummy.next;   
    }

    // O(n), O(1)
    // Solution 2
    // need to deal with extra head element
    public ListNode removeElements(ListNode head, int val) {
        if (head == null) return head;
        
        ListNode p = head;
        while (p.next != null){
            if (p.next.val == val) p.next = p.next.next;
            else p = p.next;
        }   
        return head.val == val ? head.next : head;
    }




}