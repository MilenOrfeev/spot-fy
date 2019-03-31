from threading import Lock, Thread
import serial, time

def scanVariable():
    port = "/dev/ttyACM0" # FINISH THIS
    baud = 115200
    s = serial.Serial(port)
    s.baudrate = baud
    s.flush() # it is buffering. required to get the data out *now*
    done = False

    while not done:
        data = s.readline()
        if data != '':
            print (data)
            if not ":" in data.decode("utf-8"):
                continue
            temperature, light = data.decode("utf-8").strip().split(':')
            done = True
            return int(temperature), int(light)


def tooFar():
    port = "/dev/ttyACM0" # FINISH THIS
    baud = 115200
    s = serial.Serial(port)
    s.baudrate = baud
    s.flush() # it is buffering. required to get the data out *now*
    done = False
    while not done:
        data = s.readline()
        if "FAR" in data.decode("utf-8"):
            done = True
            return True


scanVariable()

#def showVariable():
#    global temperature
#    while True:
#        #demoInput = input("Enter something:")
#        time.sleep(5)
#        lock.acquire()
#        print (temperature)
#        lock.release()
#
#threads = []
#for func in [scanVariable, showVariable]:
#    threads.append(Thread(target=func))
#    threads[-1].start()
#
