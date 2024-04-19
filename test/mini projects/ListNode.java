//  //Definition for singly-linked list.
//  public class ListNode {
//      int val;
//      ListNode next;
//      ListNode() {}
//      ListNode(int val) { this.val = val; }
//      ListNode(int val, ListNode next) { this.val = val; this.next = next; }
//  }
 
//  class Solution {
//     public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
//         int sum, carry;
//         sum = l1.val + l2.val;
//         carry = 0;
//         if (sum >= 10){
//             sum = sum - 10;
//             carry = 1;
//         }
//         l1.val = sum;
//         if(carry == 1){
//             if(l1.next != null) {
//                 l1.next.val++;
//             }
//             else {
//                 l1.next = new ListNode(carry);
//             } 
//         }
//         if(l1.next != null && l2.next!= null) addTwoNumbers(l1.next, l2.next);
//         else if (l1.next!= null && l2.next == null) addTwoNumbers(l1.next, new ListNode(0));
//         else if (l2.next != null && l1.next == null) {
//             l1.next = new ListNode(0);
//             addTwoNumbers(l1.next, l2.next);
//         }
//         return l1;
//     }

public class ListNode {
    Node list[];

    public static void main(String[] args){
       System.out.println("Linked list solution");
        //    # single linked list solution
        // # two arrays 
        // # three variables for calculation
        // # range of node 0 -> 9
        System.out.println(extract());

        
    }
    
    public static int extract(){
        Node l1 = new Node();
        l1.val = 20;
        l1.next= new Node(79);
        while (l1.next!=null) {
            System.out.println(l1.val);
            l1.val+=23;
        }
        return l1.val;
    }
    public static class Node{
        int val;
        Node next;
        Node(){}
        Node(int value){
            value=this.val;
        }
        Node(int value,Node nextNode){
            value=this.val;
            nextNode=this.next;
        }
    }
}