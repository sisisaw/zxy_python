# string.ascii_letters+string.digits 大小写字母和数字
# string.printable 大小写和数字和特殊字符

import string
import random
import time

def MyPassword(lenght):
    random.seed(time.time())
    chars = string.printable
    return ''.join([random.choice(chars) for i in range(lenght)])

# 生成10个随机密码
for i in range(5):
    # 生成16位的随机密码
    print(MyPassword(16))

