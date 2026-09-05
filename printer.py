def show_sum(a, b):
    print(a+b)

def get_sum(a,b):
    return a+b

def format_sum(a,b):
    result=a+b
    return f"sum of {a} and {b} is {result}"

if __name__ == "__main__":
    show_sum(3, 5)
    print(get_sum(3, 5))
    print(format_sum(3, 5))