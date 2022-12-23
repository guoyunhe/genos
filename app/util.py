def format_byte_size(num: int):
    for unit in ["B", "KB", "MB"]:
        if abs(num) < 1000:
            return f"{num:3.1f}{unit}"
        num /= 1000
    return f"{num:.1f}GB"
