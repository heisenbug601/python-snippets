s = 'Line1\nLine2\nLine3'
print(s)
# Line1
# Line2
# Line3

s = 'Line1\r\nLine2\r\nLine3'
print(s)
# Line1
# Line2
# Line3

s = '''Line1
Line2
Line3'''
print(s)
# Line1
# Line2
# Line3

s = '''
    Line1
    Line2
    Line3
    '''
print(s)
# 
#     Line1
#     Line2
#     Line3
#     

s = 'Line1\n'\
    'Line2\n'\
    'Line3'
print(s)
# Line1
# Line2
# Line3

s = 'Line1\n'\
    '    Line2\n'\
    '        Line3'
print(s)
# Line1
#     Line2
#         Line3

s = ('Line1\n'
     'Line2\n'
     'Line3')
print(s)
# Line1
# Line2
# Line3

s = ('Line1\n'
     '    Line2\n'
     '        Line3')
print(s)
# Line1
#     Line2
#         Line3

s = '''\
Line1
Line2
Line3'''
print(s)
# Line1
# Line2
# Line3

s = '''\
Line1
    Line2
        Line3'''
print(s)
# Line1
#     Line2
#         Line3

l = ['Line1', 'Line2', 'Line3']
s = '\n'.join(l)
print(s)
# Line1
# Line2
# Line3

s = 'Line1\nLine2\r\nLine3'
l = s.splitlines()
print(l)
# ['Line1', 'Line2', 'Line3']

s = 'Line1\nLine2\r\nLine3'

s_new = ''.join(s.splitlines())
print(s_new)
# Line1Line2Line3

s_new = ' '.join(s.splitlines())
print(s_new)
# Line1 Line2 Line3

s_new = ','.join(s.splitlines())
print(s_new)
# Line1,Line2,Line3

s_new = '\r\n'.join(s.splitlines())
print(s_new)
# Line1
# Line2
# Line3

s = 'Line1\nLine2\nLine3'

s_new = s.replace('\n', '')
print(s_new)
# Line1Line2Line3

s_new = s.replace('\n', ',')
print(s_new)
# Line1,Line2,Line3

s = 'Line1\nLine2\r\nLine3'

s_new = s.replace('\n', ',')
print(s_new)
# ,Line3

s_new = s.replace('\r\n', ',')
print(s_new)
# Line1
# Line2,Line3

s = 'Line1\nLine2\r\nLine3'

s_new = s.replace('\r\n', ',').replace('\n', ',')
print(s_new)
# Line1,Line2,Line3

s_new = s.replace('\n', ',').replace('\r\n', ',')
print(s_new)
# ,Line3

s_new = ','.join(s.splitlines())
print(s_new)
# Line1,Line2,Line3

s = 'aaa\n'
print(s + 'bbb')
# aaa
# bbb

s_new = s.rstrip()
print(s_new + 'bbb')
# aaabbb

print('a')
print('b')
print('c')
# a
# b
# c

print('a', end='')
print('b', end='')
print('c', end='')
# abc

print('a', end='-')
print('b', end='-')
print('c')
# a-b-c
