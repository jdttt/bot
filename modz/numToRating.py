def convert(num):
    if num < 2:
        num = num + 4
    elif num < 11:
        num = ((num - 2)/3)+6
    else:
        num = ((num - 11)/2)+9
    return num


def numToRating(num):
    match num:
        case -1:  return "UNSEEN"
        case 0:  return "NO RATING"
        case 1:  return "F"
        case 2:  return "D-"
        case 3:  return "D"
        case 4:  return "D+"
        case 5:  return "C-"
        case 6:  return "C"
        case 7:  return "C+"
        case 8:  return "B-"
        case 9: return "B"
        case 10: return "B+"
        case 11: return "A-"
        case 12: return "A"
        case 13: return "A+"
        case _: return f"{round(convert(num),3)} (which is higher than {numToRating(num - num%1)} but lower than {numToRating((num - num%1) + 1)})"
