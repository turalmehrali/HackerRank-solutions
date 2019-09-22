

def solve(s):
    
    new_s = []
    for i in s.split(" "):
        new_s.append(i.capitalize())

    return " ".join(new_s)


