def encode(self, strs: List[str]) -> str:
    s = ''

    for string in strs:
        s += str(len(string)) + ' ' + string

    return s

def decode(self, s: str) -> List[str]:
    strs = []

    while s:
        num = ''

        while s[0] != ' ':
            num += s[0]
            s = s[1 :]

        strs.append(s[1 : int(num) + 1])
        s = s[int(num) + 1 :]
    
    return strs
