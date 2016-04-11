#(1)����һ����3��ʼ���������У���һ���������е�������
def _odd_order():
    n = 1
    while True:
        n = n + 2
        yield n

#(2)����һ��ɸѡ����
def _not_divisible(n):
    return lambda x : x % n > 0

#(3)����һ�������������Ϸ�����һ������
def primes():
    yield 2
    it = _odd_order() #��ʼ����
    while True:
        n = next(it)    #�������еĵ�һ����
        yield n
        it = filter(_not_divisible(n),it)   #����������

#(4)��ӡ100���ڵ���������
for n in primes():
    if n < 100:
        print(n)
    else:
        break
