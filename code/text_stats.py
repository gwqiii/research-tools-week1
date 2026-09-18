import re
import sys
from collections import Counter
from pathlib import Path


def main():
    if len(sys.argv) < 2:
        print("python code/text_stats.py sample.txt")
        return

    file_path = Path(sys.argv[1])
    text = file_path.read_text(encoding="utf-8")
    words = re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", text.lower())

    for word, count in sorted(Counter(words).items()):
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
