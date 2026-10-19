from typing import Optional

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []  # Renamed min_so_far to min_stack for clarity

    def push(self, val: int) -> None:
        """Push a value onto the stack and update the min_stack."""
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        """Remove the top element from both stacks if necessary."""
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:  
                self.min_stack.pop()  # Correctly maintaining min tracking
            self.stack.pop()

    def top(self) -> Optional[int]:
        """Return the top element of the stack."""
        return self.stack[-1] if self.stack else None  # Handles empty stack case

    def getMin(self) -> Optional[int]:
        """Return the minimum element in the stack."""
        return self.min_stack[-1] if self.min_stack else None  # Handles empty stack case
