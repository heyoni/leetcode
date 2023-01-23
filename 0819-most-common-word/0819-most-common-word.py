import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = [w for w in re.sub(r'[^a-zA-Z]',' ',paragraph).lower().split() if w not in banned]

        count = 0
        result = ''
        for i in paragraph:
            if paragraph.count(i) > count:
                result = i
                count = paragraph.count(i)
        return result
