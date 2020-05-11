import string
def srange(N):
    return list(range(N))+list(range(N-2,-1,-1))

def print_rangoli(size):
    alpha = string.ascii_lowercase
    num = size
    for i in srange(num):
      print( '-'.join([alpha[num-j-1] for j in  srange(i+1)]).center(4 * (num - 1) + 1,'-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
