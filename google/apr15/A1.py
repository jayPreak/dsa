def check_collisions(mapping, words):
    encoded_words = set()
    for word in words:
        encoded_word = "".join(
            [mapping[ord(letter) - ord('A')] for letter in word])
        if encoded_word in encoded_words:
            return "YES"
        encoded_words.add(encoded_word)
    return "NO"


def main():
    T = int(input().strip())
    for t in range(1, T + 1):
        mapping = input().strip().split()
        N = int(input().strip())
        words = [input().strip() for _ in range(N)]
        result = check_collisions(mapping, words)
        print(f"Case #{t}: {result}")


if __name__ == "__main__":
    main()
