import subprocess



cmd = "ls"



process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE,
                                   bufsize=1, universal_newlines=True)

pid = process.pid



print(pid)
