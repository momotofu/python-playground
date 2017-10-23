from functools import reduce

def convert_to_numeric(input):
    return float(input)

def sum_of_middle_three(n1, n2, n3, n4, n5):
    list = [n1, n2, n3, n4, n5]
    list.remove(max(list))
    list.remove(min(list))

    return reduce((lambda x, y: x + y), list)

def score_to_rating_string(score):
    """
    Takes a numerical input and maps its value to
    the correct rating. That rating is then returned.
    """

    if 0 <= score < 1:
        return "Terrible"
    elif 1 <= score < 2:
        return "Bad"
    elif 2 <= score < 3:
        return "OK"
    elif 3 <= score < 4:
        return "Good"
    elif 4 <= score <= 5:
        return "Excellent"

def scores_to_rating(n1, n2, n3, n4, n5):
    in1 = convert_to_numeric(n1)
    in2 = convert_to_numeric(n2)
    in3 = convert_to_numeric(n3)
    in4 = convert_to_numeric(n4)
    in5 = convert_to_numeric(n5)

    average = sum_of_middle_three(in1, in2, in3, in4, in5)/3
    return score_to_rating_string(average)

print(scores_to_rating(1, 1, 4, 3, 2))
