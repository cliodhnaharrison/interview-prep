from string import ascii_lowercase, ascii_uppercase

def solution(S):
    if S.lower() == S or S.upper() == S or len(S) < 2:
        return "NO"

    upper_list = list(ascii_uppercase)[::-1]
    lower_list = list(ascii_lowercase)[::-1]

    for i in range(len(upper_list)):
        if upper_list[i] in S and lower_list[i] in S:
            return upper_list[i]

    return "NO"


def main():
    # tests = ["aaBabcDaA", "Codility", "WeTestCodErs", "AaZ", "A", "Aa", ""]
    #for x in tests:
    #    print (solution(x))

    a = "a" * 199999 + "A"
    print (solution(a))

if __name__ == "__main__":
    main()
