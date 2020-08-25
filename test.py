#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# import os
# import time
#
# for i in range(2):
#     print('**********%d***********' % i)
#     pid = os.fork()
#     # print(pid)
#     if pid == 0:
#         # We are in the child process.
#         print("%d (child) just was created by %d." % (os.getpid(), os.getppid()))
#     else:
#         # We are in the parent process.
#         print("%d (parent) just created %d." % (os.getpid(), pid))

# import os
#
# # Create a child process
# # using os.fork() method
# pid = os.fork()
#
# # pid greater than 0 represents
# # the parent process
# if pid > 0:
#     print("I am parent process:")
#     print("Process ID:", os.getpid())
#     print("Child's process ID:", pid)
#
# # pid equal to 0 represnts
# # the created child process
# else:
#     print("\nI am child process:")
#     print("Process ID:", os.getpid())
#     print("Parent's process ID:", os.getppid())
#
# for i in range(5):
#     print(i)

d = {'a':1}
b = {'c':2}
print(type({**d, **b}))
a = 1
b = 0

print(a or b)
