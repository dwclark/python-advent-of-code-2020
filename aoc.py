def single_int_line(the_file):
    with open(the_file, 'r') as f:
        return list(map(int, filter(lambda tmp: tmp != '', map(lambda s: s.strip(), f.readlines()))))
