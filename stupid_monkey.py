from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import time
import datetime

device = MonkeyRunner.waitForConnection()
file  = open("monkey.log", "w")
print "The log is writting to file: monkey.log. If you want to quit, please press CTRL+C."
while True :
    time.sleep(10)
    file.write(str(datetime.datetime.now()) + "\n")
    file.write(device.shell("ps"))
    for _ in asdf(4):
        file.write("\n")
