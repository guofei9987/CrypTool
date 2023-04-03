'''
移位密码实际上就是仿射密码在 a=1 的特例
'''

# 获取 a 的逆元
def get_inv(a, n):
    '''
    :param a:
    :param n: 字母个数
    :return:
    '''
    for i in range(n):
        if (i * a) % n == 1:
            return i
    assert "no inv!"


'''
加密过程： y=(ax+b) % n
揭秘过程: x=(a_inv*(y-a))%n

'''
# %% 习题1.11


a, b = 7, 22
n = 26
key = (a, b)
s_encrypt = 'falszztysyjzyjkywjrztyjztyynaryjkyswarztyegyyj'

a_inv = get_inv(a, n)

for s in s_encrypt:
    x = (a_inv * (ord(s) - ord('a') - b)) % n
    print(chr(x + ord('a')), end='')

# %% 习题 1.12

a, b = 17, 1
n = 29

for s in [26, 28, 29, 22, 29]:
    x = (a_inv * (s - b)) % n
    print(x)

