def format_byte_size(num: int):
    for unit in ["B", "KB", "MB"]:
        if abs(num) < 1000:
            return f"{num:3.1f}{unit}"
        num /= 1000
    return f"{num:.1f}GB"


def parse_byte_size(txt: str) -> int:
    num = 0
    for letter in txt:
        if letter <= '9' and letter >= '0':
            num = num*10 + int(letter)
        elif letter == 'G':
            num = num * 1000 * 1000 * 1000
        elif letter == 'M':
            num = num * 1000 * 1000
        elif letter == 'K':
            num = num * 1000
    return num
