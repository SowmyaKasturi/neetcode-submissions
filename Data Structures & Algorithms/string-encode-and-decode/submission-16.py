class Solution:
    
    def encode(self, strs: List[str]) -> str:
        if not strs:  # check for empty list
            return ""
        encoded_parts = []
        for word in strs:
            if word == "":  # Handle empty string
                encoded_word = "#EMPTY#"  # Use a unique placeholder for empty string
            else:
                encoded_word = ";".join(str(ord(ch)) for ch in word)
            encoded_parts.append(encoded_word)
        return "|".join(encoded_parts)

    def decode(self, s: str) -> List[str]:
        if not s:  # check if the string is empty
            return []
        words = s.split("|")
        decoded_words = []
        for word in words:
            if word == "#EMPTY#":  # Handle the empty string placeholder
                decoded_words.append("")
            else:
                decoded_word = "".join(chr(int(num)) for num in word.split(";") if num)
                decoded_words.append(decoded_word)
        return decoded_words
