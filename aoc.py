def single_int_line(the_file):
    return list(map(int, non_blank_lines(the_file)))

def non_blank_lines(the_file):
    with open(the_file, 'r') as f:
        return list(filter(lambda tmp: tmp != '', map(lambda s: s.strip(), f.readlines())))

def blank_line_delimited(the_file):
    batch = []
    current = ''
    with open(the_file, 'r') as f:
        for line in f.readlines():
            s = line.strip()
            if s:
                current += current + ' ' + s
            else:
                batch.append(current.strip())
                current = ''
    if current:
        batch.append(current.strip())

    return batch
