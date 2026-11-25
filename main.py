"""moon-answers-back: the Moon finally answers back (make.fun one-liner)."""
import os
import sys

ENTRY = "You only love me from 384,400 km away \u2014 up close I'm dust and craters, so enjoy the view and keep your promises down there."

OUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    data = ENTRY.encode("utf-8")
    with open(OUT_PATH, "wb") as f:
        f.write(data)
    with open(OUT_PATH, "rb") as f:
        back = f.read()
    assert back == data, "entry.txt is not byte-identical to ENTRY"
    text = back.decode("utf-8")
    assert 1 <= len(text) <= 240, "entry must be 1-240 characters"
    assert text.strip() != "", "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    sys.stdout.write("wrote %s (%d chars)\n" % (OUT_PATH, len(text)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
