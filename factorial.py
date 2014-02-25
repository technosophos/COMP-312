import sys

def main(n):
    if n <= 1:
        return 1
    else:
        return n * main(n - 1)

if __name__ == '__main__':
  print main(int(sys.argv[1]))
