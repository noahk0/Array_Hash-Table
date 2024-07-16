def encode(self, strs: List[str]) -> str:
    str = ''

    for string in strs:
        str += str(len(string)) + ' ' + string

    return str

def decode(self, s: str) -> List[str]:
    str = []

    while s:
        num = ''

        while s[0] != ' ':
            num += s[0]
            s = s[1 :]

        str.append(s[1 : int(num) + 1])
        s = s[int(num) + 1 :]
    
    return str
