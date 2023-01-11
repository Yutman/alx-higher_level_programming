#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    defNames = dir(hidden_4)

    for i in defNames:
        if ord(i[:1]) != 95:
            print(i)
