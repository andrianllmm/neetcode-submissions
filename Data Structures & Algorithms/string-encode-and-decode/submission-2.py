class Solution:

    def encode(self, strs: List[str]) -> str:
        output = []
        for s in strs:
            output.append(str(len(s)) + "#" + s)
        return "".join(output)

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0

        while i < len(s):
            n = 0

            while s[i] != "#":
                n = n * 10 + int(s[i])
                i += 1

            i += 1
            output.append(s[i:i+n])
            i += n

        return output