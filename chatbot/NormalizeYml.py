import string


def normalize_yml(in_file, out_file):
    file_handle = open(in_file, 'r')
    lines = file_handle.readlines()
    lines = [filter(lambda x: x in set(string.printable), line[:-1]) for line in lines]
    write_file = open(out_file, 'w')
    for line in lines:
        print line
        write_file.write('{}"{}"\n'.format(line[:4], line[4:]))

"""
out_file = open('intrebari.yml', 'w')
out_file.write('categories:\n- intrebari random\nconversations:\n')


"""

normalize_yml('fromgabi.txt', 'intrebari.yml')