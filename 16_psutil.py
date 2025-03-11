import psutil
psutil.cpu_count() # CPU逻辑数量

print(psutil.cpu_count(logical=False)) # CPU物理核心

# 2说明是双核超线程, 4则是4核非超线程
print(psutil.virtual_memory())
print(psutil.pids())