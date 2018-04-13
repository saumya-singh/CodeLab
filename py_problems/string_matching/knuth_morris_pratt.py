def preprocessing(pattern):
    lsp = [0]
    len_of_previous_prefix = 0
    len_of_pattern = len(pattern)
    for index in range(1, len_of_pattern):
        if pattern[index] == pattern[len_of_previous_prefix]:
            len_of_previous_prefix += 1
        else:
            len_of_previous_prefix = 0
        lsp.append(len_of_previous_prefix)
    return lsp


def kmp_string_matching(text, pattern):
    len_of_pattern = len(pattern)
    len_of_text = len(text)
    text_index = 0
    pattern_index = 0
    lsp = preprocessing(pattern)
    found_pattern_index = []

    while text_index < len_of_text:  #
        if pattern[pattern_index] == text[text_index]:
            pattern_index += 1
            text_index += 1
            if pattern_index == len_of_pattern:
                found_pattern_index.append(text_index - len_of_pattern)
                pattern_index = lsp[pattern_index - 1]
        else:
            if pattern_index == 0:
                text_index += 1
            else:
                pattern_index = lsp[pattern_index - 1]

    return found_pattern_index


def main():
    pattern = "AABAACAABAA"
    text = "AABAACDAABAACAABAACAABAA"
    indicies = kmp_string_matching(text, pattern)
    print(indicies)


if __name__ == "__main__":
    main()
