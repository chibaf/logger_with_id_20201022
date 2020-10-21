import serial, sys, queue
import re, time
#from pylab import *
from threading import (Event, Thread)

itime=0


def port_read():
  ser.reset_input_buffer
  line_byte = ser.readline()  #一回、読み飛ばしをかける
  #一回バッファークリアしないといけない？？？
  ser.reset_input_buffer
  time.sleep(0.2)
  while True:
    try:
      A=ser.in_waiting
      if (ser.in_waiting)>0:
        line_byte = ser.readline()
        q.put(line_byte)
        if False :
          print(A,q.qsize(),line_byte)
          #(q.qsize(),"=queue_size")
        event.wait()
    except KeyboardInterrupt:
      print ('exiting thread-1 in port_read')
      sys.exit

def PID():
  itime=0
  time.sleep(0.2)
  event.set()#フラグを true にして起動
  time.sleep(3)
  if False :      #debug
    event.clear() #フラグを false にして止める
  time.sleep(1)
  print("plotting now")
  while True:
    itime=itime+0.1
    line_byte=q.get()
    #print(q.qsize(),"line_byte",line_byte)
    line=line_byte.decode(encoding='utf-8')
     #line=line.replace("\x000","")
    line_s=line.split(',')  # list of numbers(character) separated by "," 
    line_s.insert(0,str(itime))
    f.write(",".join(line_s))
    line_p=str(line).replace("\r\n","")
    T_meas=float(line_s[3])  # temperature is from float(line_s[2]).  coreresponds to Tc-1.
    print(line)   
    s_work="""
    T_measは、Tc-1なので、これをPIDの計測値としてPID制御をする。
    """
    itime=itime+0.1

    

#     time.sleep(1)

event=Event()
q = queue.Queue()

strPort = sys.argv[2]   # serial port
ser=serial.Serial(strPort,115200,timeout=0) #20200627 115200->19200
ser.send_break()
ser.reset_input_buffer
ser.reset_input_buffer
ser.reset_input_buffer
ser.reset_input_buffer
#何回もリセットするとin_waitingの数が減る。
#スリープさせるとin_waitingの数が増えてくる。
print("connected to: " + ser.portstr)

file=sys.argv[1]  # file name
regex = re.compile('\d+')  # for extracting number from strings
f=open(file,"w+")
y=[0]*100
data=[];

thread1 = Thread(target=port_read)
thread2 = Thread(target=PID)

thread1.start()
time.sleep(3)
thread2.start()


thread1.join()
print ('exiting at thread1.join')
ser.close()
f.close()

#thread2.start()

ser.reset_input_buffer
ser.close()
f.close()
