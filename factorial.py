def main(n):
    if n<=1:
        return 1
    else:
        return n*main(n-1)
        
if __name__ == '__main__':
  main(8)
