def make_readable(seconds):
    h = int(seconds / (60 * 60))
    m = int(seconds / 60 % 60)
    s = int(seconds % 60)
    return f"{'0' if h < 10 else ''}{h}:{'0' if m < 10 else ''}{m}:{'0' if s < 10 else ''}{s}"