# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    N = int(input())
    for i in range(N):
        div = input()
        div = div.split(" ")
        
        try:
            num = int(div[0])
            den = int(div[1])
            quo = num//den
            print(quo)
        except ZeroDivisionError as e:
            print("Error Code:", e)
        except ValueError as e:
            print("Error Code:", e)
    
