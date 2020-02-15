# -*- coding:utf-8 -*-
"""
__author__ = "TomTao"
"""
# 代码

# coding=utf-8
"""通过使用互斥锁，锁定全局变量，防止数据异常"""
import threading
num = 0
# 创建互斥锁
lock = threading.Lock()


def testOne():
    global num
    for i in range(100000):
    # 在num加1前进行资源抢占，如果抢到则锁定资源，在num+1完成之后进行资源释放
    #     lock.acquire()  # 上锁
        num += 1
        # lock.release()# 释放锁
    print("testOne 执行完毕,num的值为:",num)


def testTwo():
    global num
    for i in range(100000):
        lock.acquire()
        num += 1
        lock.release()
    print("testTwo 执行完毕,num的值为:",num)



from threading import Thread
import time
import asyncio


def io_func(i):
    # 模拟io等待时间，设置3秒
    print(i)
    time.sleep(3)

async def io_func_thread(i):
    # 模拟io等待时间，设置3秒
    print('waiting',i)
    await asyncio.sleep(3)

if __name__ == '__main__':
    # 采用多线程的方式
    # count = 100
    # start_time = time.time()
    # threads = [Thread(target=io_func,args=(i,)) for i in range(count)]
    # [threads[i].start() for i in range(count)]
    # [threads[i].join() for i in range(count)]
    # end_time = time.time()
    # print(end_time - start_time)
    # 采用 async协程的方式
    count = 100
    start_time = time.time()
    tasks = [asyncio.ensure_future(io_func_thread(i)) for i in range(count)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    end_time = time.time()
    print(end_time - start_time)
# if __name__ == '__main__':
#     # 创建线程
#     t1 = threading.Thread(target=testOne)
#     t2 = threading.Thread(target=testTwo)
#     # 启动线程
#     t1.start()
#     t1.join()
#     t2.start()
#     t2.join()