from datetime import datetime
def is_it_valid(pic: str):
    day = int(pic[0:2])
    month = int(pic[2:4])
    now = datetime.now()
    if pic[6] == "+":
        year = int(f"18{pic[4:6]}")
    elif pic[6] == "-":
        year = int(f"19{pic[4:6]}")
    elif pic[6] == "A":
        year = int(f"20{pic[4:6]}")
    else:
        return False
    try:
        birthday = datetime(year, month, day)
        if birthday > now:
            return False
    except:
        return False
    comparison_id = int(f"{pic[0:6]}{pic[7:10]}") % 31
    string = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    try:
        if string[comparison_id] != pic[10]:
            return False
    except:
        return False
    if len(pic) > 11:
        return False
    return True



   
  

