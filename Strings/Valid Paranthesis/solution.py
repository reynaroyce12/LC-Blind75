class Solution(object):
    def isValid(self, s):
        opening_brackets = {'(', '{', '['}
        closing_brackets = {')', '}', ']'}

        matching_pairs = {
            '(' : ')', 
            '{' : '}',
            '[' : ']'
        }

        character_stack = []

        for char in s:
            if char in opening_brackets:
                character_stack.append(char)

            elif char in closing_brackets:
                if not character_stack:
                    return False

                top_character = character_stack[-1]
                if matching_pairs[top_character] == char:
                    character_stack.pop()
                else:
                    return False
            else:
                return False

        return len(character_stack) == 0

solution = Solution()
s = "([)"

result = solution.isValid(s)
print(result)