import tailer
from settings import logfile_path

while True:
    for line in tailer.follow(open(logfile_path, encoding="UTF-8")):
        log = line.strip()
        print(log)




