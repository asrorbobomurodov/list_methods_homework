def main(list1):
    """
    A list of zeros and ones is given. Find how many ones and how many zeros there are and return to the list form.
    Args:
        list1(list): parameter
    Returns:
        list: return answer
    """
    x = list1.count(1)
    y = list1.count(0)
    s = [x,y]
    return s
print(main([0,1,0,1,0,1,1]))