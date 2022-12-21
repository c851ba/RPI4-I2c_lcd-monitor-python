#!/usr/bin/env python3

from RPLCD.i2c import CharLCD
from gpiozero import CPUTemperature
import psutil
from psutil._common import bytes2human
import time
from datetime import datetime
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,
              cols=16, rows=2, dotsize=8,
              charmap='A00',
              auto_linebreaks=True,
              backlight_enabled=True)
lcd.clear()



while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    cpu = str(psutil.cpu_percent()) + '%'
    temp = str(int(CPUTemperature().temperature))+ '°C'
    ramUsed = (psutil.virtual_memory()[3])
    ramFree = (psutil.virtual_memory()[4])


    #ramUsed = 'RAM Used ' + str(bytes2human(ramUsed))
    #ramFree = 'RAM Free ' + str(bytes2human(ramFree))
    ramUsed = (bytes2human(ramUsed))
    ramFree = (bytes2human(ramFree))
    #rampct = 'RAM Used (GB):' + str(psutil.virtual_memory()[3]/1000000000)
    
    # time
    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write_string('Time: ')
    lcd.cursor_pos = (1, 0)
    lcd.write_string(current_time)
    time.sleep(3)
    
    # cpu used
    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write_string('CPU Usage: ')
    lcd.cursor_pos = (1, 0)
    lcd.write_string(cpu)
    time.sleep(3)
    # cpu temp
    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write_string('CPU Temperature: ')
    lcd.cursor_pos = (1, 0)
    lcd.write_string(temp)
    time.sleep(3)
    # ram free 
    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write_string('Memory Free')
    lcd.cursor_pos = (1, 0)
    lcd.write_string(ramFree)
    time.sleep(3)
    # ram used
    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write_string('Memory Used')
    lcd.cursor_pos = (1, 0)
    lcd.write_string(ramUsed)
    time.sleep(3)


    








