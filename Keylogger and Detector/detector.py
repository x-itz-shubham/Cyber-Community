import json
from subprocess import check_output
import os
import io


class Process(object):

    def __init__(self, proc_info):
        print(proc_info)
        self.pid = proc_info[1]
        self.cmd = proc_info[0]

    def name(self):
        return '%s' % self.cmd

    def procid(self):
        return '%s' % self.pid


def kill_logger(key_pid):
    response = input("\n\nDo you want to stop this process: y/n ?")
    if response == "y" or response == "Y":
        os.system('task kill /f /im ' + key_pid)
    else:
        pass


def get_process_list():
    process_list = []
    sub_process = str(check_output("tasklist", shell=True).decode())
    x = io.StringIO(sub_process)
    for line in x:
        line = line.split()
        if len(line) > 0:
            process_list.append(line)

    return process_list


if __name__ == "__main__":

    process_list = get_process_list()

    print('Reading Process list...\n')

    process_cmd = []
    process_pid = []

    for process in process_list:
        process_cmd.append(process[0])
        process_pid.append(process[1])

l1 = open("example_1.json", "r")
l1 = json.loads(l1.read())
dict1 = l1

record = 0
flag = 1

for x in process_cmd:
    for y in dict1:
        if x.find(y['name']) > -1:
            print("KeyLogger Detected: \nThe following process may be a key logger: \n\n\t" + process_pid[
                record] + " ---> " + x)
            kill_logger(x)
            flag = 0
    record += 1

if flag:
    print("No Keylogger Detected")