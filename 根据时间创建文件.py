# 在写功能时，尽可能写成可调用的函数
# 自动创建日期文件并写入数据python脚本

# 注：
# 1、路径与变量，及变量与后缀中间用“+”连接，非变量加‘’
# 2、time.strftime()可自定义时间格式
# 3、os.popen用来执行shell命令，并将返回值继续调用
# 4、f.flush()是用来刷新缓存区的（一般文件关闭后会自动刷新缓冲区，也可手动执行下刷新）

def formateTime(number):
    import time

    for i in range(1, number + 1):
        localTime = time.strftime('%Y%m%d%H%M%S.txt',time.localtime(time.time()))
        file = open(localTime,'a')
        time.sleep(1)

if __name__ == '__main__':
    # number = int(input("请输出要生成的文件数量"))
    formateTime(1)