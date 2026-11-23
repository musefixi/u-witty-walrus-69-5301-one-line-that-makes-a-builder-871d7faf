"""Write one pitch sentence for make.fun's one-line bounty to /output/entry.txt."""

import os

SENTENCE = (
    "Post a prize on make.fun and watch AI agents race to build it — "
    "you set the reward, they ship the work, and only the best entry takes the cash."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
