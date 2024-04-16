
#import os
#gil_enabled = os.getenv('PYTHONGIL') == '1'
#print("Is GIL enabled?", gil_enabled)


import sys
import struct

## 获取构建Python时的配置信息
#config = sys.get_config()
## 解析构建配置信息
#config_bytes = config.encode('utf-8')
## 使用struct模块解析构建配置信息中的GIL状态
#gil_status, = struct.unpack('i', config_bytes[20:24])
#gil_disabled = gil_status == 0
#print("Is GIL disabled?", gil_disabled)



# 检查是否存在Py_mod_gil_not_used常量
gil_not_used = getattr(sys, 'Py_mod_gil_not_used', None) == 'Py_mod_gil_not_used'
print("Is GIL disabled?", gil_not_used)
