def print_full_name(a, b):
    string = "Hello {} {}! You just delved into python."
    print(string.format(a,b))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
