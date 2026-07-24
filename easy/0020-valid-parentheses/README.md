# Valid Parentheses

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:


	Open brackets must be closed by the same type of brackets.
	Open brackets must be closed in the correct order.
	Every close bracket has a corresponding open bracket of the same type.


 
Example 1:


Input: s = "()"

Output: true


Example 2:


Input: s = "()[]{}"

Output: true


Example 3:


Input: s = "(]"

Output: false


Example 4:


Input: s = "([])"

Output: true


Example 5:


Input: s = "([)]"

Output: false


 
Constraints:


	1 <= s.length <= 104
	s consists of parentheses only '()[]{}'.

## Solution

**Language:** C  
**Runtime:** 0 ms  
**Memory:** 8.4 MB  
**Submitted:** 2026-07-24T17:24:09.944Z  

```c
        } 

        else {

            if (top == -1) return false;
            
            if (c == ')' && stack[top] != '(') return false;
            if (c == '}' && stack[top] != '{') return false;
            if (c == ']' && stack[top] != '[') return false;
            

            top--;
        }
    }

    return top == -1;

bool isValid(char* s) {
    int len = strlen(s);
    char stack[len]; 
    int top = -1; 

    for (int i = 0; i < len; i++) {
        char c = s[i];

        if (c == '(' || c == '{' || c == '[') {
            stack[++top] = c;
#include <string.h>
#include <stdbool.h>
}
#include <stdio.h>

```

---

[View on LeetCode](https://leetcode.com/problems/valid-parentheses/)