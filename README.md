# Raspberry I2c LCD system information display
Simple monitorig script for adafruit I2c interface Board for HD44780 16x2 LCD display 
![img](https://lh3.googleusercontent.com/pw/AL9nZEWXMHWoEelCvtFAKF2J2CsNtxoc76ZDeaeM3gfG7h7WfhGQTSTiI-L2wdZjnwjHVfS0qhzHU3METutaGuyhUK4c-hSpFLvzQZ2H0WqpHaz-GxG09lgSWS19xjeffaMS3bAx6KvaWTVYJ6Yy_BwpSaiR=w1280-h576-no?authuser=0)

## prereqs
- Raspberry :) 
- I2C Lcd (PCF8574) 
- Python3
- I2c 
- smbus?

## packages 
- [RPLCD.i2c](https://rplcd.readthedocs.io/en/stable/)
- [gpiozero](https://gpiozero.readthedocs.io/en/stable/)
- [psutil](https://psutil.readthedocs.io/en/latest/)

## systemd 
-  create .service file in : /etc/systemd/system/lcdMon.service
