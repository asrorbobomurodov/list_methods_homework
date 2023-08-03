def main(fruits):
    """
    A list called “fruits” is given and is five in length and contains at least one “apple”. Calculate how many “apple” were involved and return the indexes in a list view.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    i = 0
    x = fruits.count("apple")
    si = [x]
    while len(fruits)>i:
        if fruits[i] == "apple":
            si.append(i)
        i += 1
    return si
print(main(['apple', 'apple', 'pear', 'apple', 'kiwi','apple']))