def findWords(words: list[str]) -> list[str]:
    top_row = {'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}
    middle_row = {'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
    bottom_row = {'Z', 'X', 'C', 'V', 'B', 'N', 'M', 'z', 'x', 'c', 'v', 'b', 'n', 'm'}

    output = []
    for word in words:
        top_match = False
        middle_match = False
        bottom_match = False

        for ch in word:
            if ch in top_row and middle_match is False and bottom_match is False:
                top_match = True

            elif ch in middle_row and top_match is False and bottom_match is False:
                middle_match = True

            elif ch in bottom_row and top_match is False and middle_match is False:
                bottom_match = True

            else:
                break
        else:
            output.append(word)
    return output
