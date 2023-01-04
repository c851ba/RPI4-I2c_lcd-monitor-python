#!/usr/bin/env python3

from RPLCD.i2c import CharLCD
from gpiozero import CPUTemperature
import psutil
from psutil._common import bytes2human
import time
import socket
from datetime import datetime
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,
              cols=16, rows=2, dotsize=8,
              charmap='A00',
              auto_linebreaks=True,
              backlight_enabled=True)
lcd.clear()

Transition = 10
Refresh = .5


while True:
    # time
    for _ in range(Transition):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        #lcd.clear()
        lcd.cursor_pos = (0, 0)
        lcd.write_string('Time: ')
        lcd.cursor_pos = (1, 0)
        lcd.write_string(current_time)
        time.sleep(Refresh)
    else:
        lcd.clear()
    # cpu usage and temperature 
    for _ in range(Transition):
        cpuusg = str(psutil.cpu_percent()) + '%'
        cputemp = str(int(CPUTemperature().temperature))+ '°C'

        #lcd.clear()
        lcd.cursor_pos = (0, 0)
        lcd.write_string('CPU Usage&Temp')
        lcd.cursor_pos = (1, 0)
        lcd.write_string('U:'+cpuusg+' T:'+cputemp)
        time.sleep(Refresh)
    else:
        lcd.clear()
    # ram
    for _ in range(Transition):
        ramFree = (bytes2human(psutil.virtual_memory()[4]))
        ramUsed = (bytes2human(psutil.virtual_memory()[3]))
        lcd.cursor_pos = (0, 0)
        lcd.write_string('RAM Used/Free')
        lcd.cursor_pos = (1, 0)
        lcd.write_string(ramUsed+'/'+ramFree)
        time.sleep(Refresh)
    else:
        lcd.clear()

    # Disk
    for _ in range(Transition):
        diskTotal = (bytes2human(psutil.disk_usage('/')[0]))
        diskFree = (bytes2human(psutil.disk_usage('/')[2]))
        lcd.cursor_pos = (0, 0)
        lcd.write_string('SD Total/Free')
        lcd.cursor_pos = (1, 0)
        lcd.write_string(diskTotal+'/'+diskFree)
        time.sleep(Refresh)
    else:
        lcd.clear()

    for _ in range(Transition):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 1))  # connect() for UDP doesn't send packets
        IPAddress = s.getsockname()[0]
        lcd.cursor_pos = (0, 0)
        lcd.write_string('IP Address')
        lcd.cursor_pos = (1, 0)
        lcd.write_string(IPAddress)
        time.sleep(Refresh)
    else:
        lcd.clear()

    


    








