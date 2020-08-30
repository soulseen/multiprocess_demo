from multiprocessing import Process
import os
import time

# 子进程要执行的代码
def run_proc_1(name):
    p = Process(target=run_proc_2, args=('test2',))
    print('Child 2 process will start.')
    p.start()
    while True:
        time.sleep(5)
        print('Run child process %s (%s)...' % (name, os.getpid()))

def run_proc_2(name):
    while True:
        time.sleep(5)
        print('Run child process %s (%s)...' % (name, os.getpid()))


if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc_1, args=('test1',))
    print('Child 1 process will start.')
    p.start()
    p.join()
    while True:
        time.sleep(5)
        print('Child process end.')
