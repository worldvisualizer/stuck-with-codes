/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    carryover := 0
    sumList := ListNode{}

    for l1.Next != nil && l2.Next != nil {
        value := l1.Val + l2.Val + carryover
        if !sumList {
            sumList = ListNode{
                Val: value % 10,
                Next: nil,
            }
        } else {
            sumList.Next = ListNode{
                Val: value % 10,
                Next: nil,
            }
        }
        carryover = l1.Val + l2.Val / 10
        l1 = l1.Next
        l2 = l2.Next
    }
    return sumList
}
