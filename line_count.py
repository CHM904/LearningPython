from io import open
import os
import os.path

def line_count(file_path, enc='utf8'):
    count = 0
    with open(file_path, mode='r', encoding=enc) as open_file:
        for line in open_file:
            if line.strip():
                count +=1
    
    return count


def what_encoding_by_head(file_path):
    enc = None
    with open(file_path, 'rb') as open_file:
        data = open_file.read(3)
        if len(data) == 3:
            if (data[0] == 0xEF and data[1] == 0xBB and data[2] == 0xBF):
                enc = 'utf8'
        if len(data) >= 2:
            if (data[0] == 0xFE and data[1] == 0xEF):
                enc = 'UTF-16BE'
        elif data[0] == 0xFF and data[1] == 0xFE:
            enc = 'UTF-16LE'

    return enc

def what_encoding_by_mark(file_path):
    enc = 'ascii'
    mark = 'coding'
    def extract_enc(line):
        chars = ' :=-*'
        return line.strip().lstrip(chars).rstrip(chars)
    
    with open(file_path, mode='r', encoding=enc, errors='ignore') as open_file:
        for i in range(2):
            line = open_file.readline()
            idx = line.find(mark)
            if (idx != -1):
                enc = extract_enc(line[idx+len(mark):])
                break
    return enc

def what_encoding(file_path):
    return what_encoding_by_head(file_path) or what_encoding_by_mark(file_path)

total_lines = 0
file_counts = 0

for x in os.listdir('.'):
    if os.path.isfile(x) and x[-3:] == ".py":
        try:
            enc = what_encoding(x)
            lines = line_count(x, enc)
            total_lines += lines
            file_counts += 1
            print (x, enc, lines)
        except:
            print (x,"cann't count lines")

print ('%d .py files totally have %d lines ' % (file_counts, total_lines))