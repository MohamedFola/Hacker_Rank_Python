def mutate_string(string, position, character):
    st = list(string)
    st[position] = character
    st = "".join(st)
    # (string[:position] + character + string[position+1:])
    return st
