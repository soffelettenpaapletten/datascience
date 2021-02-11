def read_data(input):
    fil = input.readlines
    list = []
    n = sum(1 for line in input)
    for i in range(n):
        list = list + [fil[n]]
    input.close

in = open('experimental_results.txt','r')
read_data(in)
