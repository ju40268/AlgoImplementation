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
    public ListNode plusOne(ListNode head) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode i = dummy;
        ListNode j = dummy;
        while (j.next != null) {
            j = j.next;
            if (j.val != 9) i = j;
        }
        i.val++; 
        i = i.next;
        while (i != null){
            i.val = 0;
            i = i.next;
        }
        if (dummy.val == 0) return dummy.next;
        return dummy;
    }
}


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
    public ListNode plusOne(ListNode head) {
        head = reverse(head);
        //         
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        //
        ListNode current = dummy;
        int carry = 1;
        //   
        while (carry > 0 || current.next != null){
            if (current.next != null) {
                current = current.next;
                carry += current.val;
                current.val = carry % 10;
                carry /= 10;
            }else{
                current.next = new ListNode(carry);
                current = current.next;
                carry = 0;
            }
        }
        return reverse(dummy.next);       
    }
    // reverse linked list function     
    public ListNode reverse(ListNode current){
        ListNode prev = null;
        while (current != null){
            ListNode next = current.next;
            current.next = prev;
            prev = current;
            current = next;
        }
        return prev;
    }
}