def single_int_line(the_file):
    return list(map(int, non_blank_lines(the_file)))

def non_blank_lines(the_file):
    with open(the_file, 'r') as f:
        return list(filter(lambda tmp: tmp != '', map(lambda s: s.strip(), f.readlines())))

def blank_line_grouped(the_file):
    batch = []
    group = []
    with open(the_file, 'r') as f:
        for line in f.readlines():
            s = line.strip()
            if s:
                group.append(s)
            else:
                batch.append(group)
                group = []
    if group:
        batch.append(group)

    return batch

def blank_line_delimited(the_file):
    return list(map(lambda g: ' '.join(g), blank_line_grouped(the_file)))

