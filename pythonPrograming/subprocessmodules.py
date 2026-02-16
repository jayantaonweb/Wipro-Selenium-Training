#Subprocess module -

# executes external system commands
# interact with the os
# capture output, error and return codes
# control the process execution

# run the OS level commands - linux , macOS, windows

# subprocess.run() - run command and wait
# subprocess.PIPE - capture the output
#subprocess.Popen() - runs process asynchronously
#subprocess.CompleteProcess - result
#subprocess.TimeoutExpired - Time out exception
#subprocess.CalledProcessError - command failure

import subprocess

result = subprocess.run("dir",shell=True, capture_output=True, text =True)
print(result)
result = subprocess.run("ipconfig",shell=True, capture_output=True, text =True)
print(result.stdout)
result = subprocess.run("python --version",shell=True, capture_output=True, text =True)
print(result.stdout)
#print(result.stderr)