# TBD
Simple monitorig script for adafruit I2c interface Board for HD44780 16x2 LCD display 
![](https://photos.google.com/share/AF1QipPMoTXPE0PjlQJlsPRVZDbi1vgnhamLD2ONFz1o99vifgEwWKZtdIRH1TxNjyBE2Q/photo/AF1QipMNyUexx4KZf9O_u5CUYDYRh17ksByfKJX8bu8P?key=QkZ3WTlYcTZtYWQwLThJMDlvUTdvUTJNVXRrdTRR | width=640)

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
