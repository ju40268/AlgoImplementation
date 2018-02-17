/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode middle = getMiddle(head);
        ListNode right = middle.next;
        middle.next = null;
        return merge(sortList(head), sortList(right));
    }

    private static ListNode merge(ListNode p, ListNode q) {
        ListNode dummy = new ListNode(-1);
        ListNode current = dummy;
        while (p != null && q != null){
            if (p.val < q.val){
                current.next = new ListNode(p.val);
                p = p.next;
            }else {
                current.next = new ListNode(q.val);
                q = q.next;
            }
            current = current.next;
        }
        if (p != null) current.next = p;
        if (q != null) current.next = q;
        return dummy.next;
    }

    private static ListNode getMiddle(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode fast = head, slow = head;
        while (fast.next != null && fast.next.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }
        
}