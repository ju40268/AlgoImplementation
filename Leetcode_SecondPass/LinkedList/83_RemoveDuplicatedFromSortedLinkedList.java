/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
    	// O(n), O(1)
        if (head == null || head.next == null) return head;
        ListNode current = head;
        while (current.next != null){
            if (current.next.val == current.val) current.next = current.next.next;
            else current = current.next;
        }
        return head;
    }
}