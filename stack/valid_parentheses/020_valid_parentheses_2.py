class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
    
        # Handle 1st character in string (guaranteed to be present)
        match s[0]:
            case '(' | '[' | '{':
                brackets.append(s[0])
            case _:
                # Invalid if not an opening bracket
                return False

        # Handle remaining characters if present
        for character in s[1:]:
            match character:
                # For closing brackets, top of stack *must* be matching opening bracket
                case ')':                
                    if len(brackets) > 0 and brackets[-1] == '(':
                        brackets.pop()
                    else:
                        return False
                case ']':               
                    if len(brackets) > 0 and brackets[-1] == '[':
                        brackets.pop()
                    else:
                        return False
                case '}':                
                    if len(brackets) > 0 and brackets[-1] == '{':
                        brackets.pop()
                    else:
                        return False                         
                case _:
                    # It's an opening bracket -> add to stack
                    brackets.append(character)

        # If all parentheses are properly closed, brackets will be empty
        if len(brackets) == 0:
            return True
        else:
            return False
