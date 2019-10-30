def copy_file(name):
    if not isinstance(name, basestring):
        raise Exception('Not valid file name format!')
    a_file = open(name)
    file_copy = file('copy_' + name, 'w')
    list_of_lines = a_file.readlines()
    for line in list_of_lines:
        if line.startswith('#'):
            continue
        else:
            file_copy.write(line)
    file_copy.close()
    a_file.close()


file_name = '2.9-test.txt'
copy_file(file_name)
a_file_copy = open('copy_' + file_name)
result = a_file_copy.read()
valid_result = """aaaaaaaaaa
dddddddddd"""
assert result == valid_result
