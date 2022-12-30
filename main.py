import time

def multiplyAllNumbers(num,multiplier):
    for i in range(num):
        print(f"{i/num*100}% Done")

def main():
    multiplyAllNumbers(1000000000,2)

def askPermission():
    s = input("Are You Sure You Want To Start The Benchmark(y/n): ")
    if s.lower() == "y":
        return True
    return False

if __name__ == '__main__':
    if askPermission() == True:
        start = time.time()
        main()
        end = time.time()
        print(f"The Computer Took {end-start} Seconds To Finish The Benchmark")