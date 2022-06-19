# Note: this solution was done via LintCode (problem 659)

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        """Encode w/ `dd#strd#str` format, where `d` is length of the next string."""
        output = "".join(f"{len(string)}#{string}" for string in strs)
        print(output)

        return output


    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        """Decode w/ `dd#strd#str` format, where `d` is the length of the next string.

        There are two contexts:
        1.) Delimiter context, where you get the length of the next string
        2.) Word context, where you gather characters for the decoded string.
        
        If characters are expected (chars_remaining == 0) -> delimiter context.
        """
        output = []
        chars_remaining = 0
        next_word_length = ""
        current_word = ""

        for character in str:
            if chars_remaining == 0:
                # Delimiter context - get length of next string to gather
                if character == "#":
                    # End delimiter context - make next_word_length a digit
                    chars_remaining = int(next_word_length)
                    # Reset length for next word
                    next_word_length = ""
                else:
                    # Add another digit to char_length
                    next_word_length += character
            else:
                # Word context - add character to current word
                current_word += character
                # Decrement chars_remaining in this word
                chars_remaining -= 1
                # If no more chars left in current word, add to output and reset it
                if chars_remaining == 0:
                    output.append(current_word)
                    current_word = ""
                
        return output
