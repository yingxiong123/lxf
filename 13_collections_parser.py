from datetime import datetime
from collections import ChainMap
import os, argparse

now = datetime.now()
print(now)

defaults = {'color': 'red', 'user': 'guest'}

#构造命令行参数
parser = argparse.ArgumentParser()
parser.add_argument('-c', '--color')
parser.add_argument('-u', '--user')
namespace = parser.parse_args()
command_line_args = { k: v for k, v in vars(namespace).items() if v }

# 组合成ChainMap:
combined = ChainMap(command_line_args, os.environ, defaults)

# 打印参数:
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])


