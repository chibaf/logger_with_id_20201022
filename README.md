# logger_with_id_20201022
logger programs added with logger id


sketch_M5SSMCP9600OCT22_01.ino = logger program with logger id (is not check with logger hard)


sketch_M5SSMCP9600OCT22.ino = logger program with logger id and running without sensor chip MCP9601

output = "01,00:00:12.7,20.0000,23.0000,20.0000,20.0000,20.0000,21.0000,23.0000,23.0000,23.0000,24.0000"


read_logger_02.py: reading logger program. 

$ python3 read_logger_02.py d2020xxxx.csv "/dev/tty.SLAB_USBtoUART"

, where serial communication speed is 112500bps


![logger-20201023a](https://user-images.githubusercontent.com/1296728/96927092-84a4d180-14f1-11eb-96e9-d7616ad75763.jpg)
