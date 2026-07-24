# Add Two Numbers

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 
Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.


Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]


Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


 
Constraints:


	The number of nodes in each linked list is in the range [1, 100].
	0 <= Node.val <= 9
	It is guaranteed that the list represents a number that does not have leading zeros.

## Solution

**Language:** Python  
**Runtime:** 0 ms  
**Memory:** 19.3 MB  
**Submitted:** 2026-07-24T14:54:10.739Z  

```py
        result = int(s1) + int(s2)
            l2 = l2.next
        s_result = str(result)[::-1]
        factice = ListNode(0)
        while l2.next != None :
            s2 += str(l2.val)
            l1 = l1.next
            s1 += str(l1.val)
        while l1.next != None :
        s2 = ""
        s1 = ''
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        print(s1, s2,result)
        noeud_actif = factice
        for cara in s_result : 
            noeud = ListNode(int(cara))
        s1 += str(l1.val)
        s2 += str(l2.val)
            noeud_actif.next = noeud
            noeud_actif = noeud 

```

---

[View on LeetCode](https://leetcode.com/problems/add-two-numbers/)