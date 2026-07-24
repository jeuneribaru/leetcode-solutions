        result = int(s1[::-1]) + int(s2[::-1])
            l2 = l2.next
        s_result = str(result)[::-1]
        factice = ListNode(0)
        noeud_actif = factice
        for cara in s_result : 
            noeud = ListNode(int(cara))
            noeud_actif.next = noeud
        while l2.next != None :
            s2 += str(l2.val)
            l1 = l1.next
            s1 += str(l1.val)
        while l1.next != None :
        s2 = ""
        s1 = ''
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
class Solution:
#         self.next = next
#         self.val = val
        print(result)
