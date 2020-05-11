def merge_the_tools(string, k):
    n = len(string)
    d = int(n/k)
    split= int(n/d)
    substring =''
    i=0
    array=list(map(''.join, zip(*[iter(string)]*split)))

    for i in array:
        reduced  = ''.join([char for index,char in enumerate(i) if char not in i[0:index        ]])
        print (reduced)                

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
