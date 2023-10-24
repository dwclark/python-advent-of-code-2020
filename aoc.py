def single_int_line(the_file):
    return list(map(int, non_blank_lines(the_file)))

def non_blank_lines(the_file):
    with open(the_file, 'r') as f:
        return list(filter(lambda tmp: tmp != '', map(lambda s: s.strip(), f.readlines())))
