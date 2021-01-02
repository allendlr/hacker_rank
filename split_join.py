def split_and_join(line):
    # write your code here
    list = line.split(" ")
    list = "-".join(list)
    return list

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
