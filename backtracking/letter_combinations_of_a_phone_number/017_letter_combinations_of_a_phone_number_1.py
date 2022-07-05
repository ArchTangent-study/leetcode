from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """Iterative solution."""
        if len(digits) == 0:
            return []
        
        map = { 
            "2": "abc", 
            "3": "def", 
            "4": "ghi", 
            "5": "jkl", 
            "6": "mno", 
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        answer = [c for c in map[digits[0]]]
        to_add = []
        for d in digits[1:]:
            for char in map[d]:
                to_add.extend(string + char for string in answer)
            answer.clear()
            answer.extend(to_add)
            to_add.clear()  

        return answer
