male_names = {'николай', "пётр", "петр"}
female_names = {'анна', 'ольга', 'анастасия'}

def ismale(name: str) -> bool:
    if name.lower() in male_names:
        return True
    else:
        return False

