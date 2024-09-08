def modify_words(words):
    for w in words:
        size = len(w)
        if size <= 10:
            print(w)
        else:
            word = w[0] + str(len(w[1:])-1) + w[-1]
            print(word)

# n = int(input())
# words = [input().strip() for _ in range(n)]
# modify_words(words)

def main():
    words = ["word", "localization", "internationalization", "pneumonoultramicroscopicsilicovolcanoconiosis"]
    modify_words(words)

if __name__ == "__main__":
    main()
