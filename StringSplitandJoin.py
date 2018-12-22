def split_and_join(line):
    # write your code here
    line=line.split(" ")
    line="-".join(line)
    return line

print(split_and_join("this is a string"))