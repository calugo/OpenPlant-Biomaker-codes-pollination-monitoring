import time
import subprocess
from board import SCL, SDA
import busio
import adafruit_ssd1306
from PIL import Image,ImageDraw,ImageFont

import board
import busio
import digitalio
import adafruit_bme280


spi = busio.SPI(board.SCK,MOSI=board.MOSI,MISO=board.MISO) 
cs = digitalio.DigitalInOut(board.D5)
bme280 = adafruit_bme280.Adafruit_BME280_SPI(spi,cs)


i2c=busio.I2C(SCL,SDA)
display=adafruit_ssd1306.SSD1306_I2C(128,64,i2c)
display.fill(0)
display.show()

width=display.width
height=display.height
image=Image.new("1",(width,height))
draw=ImageDraw.Draw(image)
draw.rectangle((0,0,width,height),outline=0,fill=0)
padding= -2
top=padding
bottom=height-padding
x=0
font=ImageFont.load_default()
while True:
    draw.rectangle((0,0,width,height),outline=0,fill=0)
    
    cmd="hostname -I | cut -d\' \' -f1"
    IP= subprocess.check_output(cmd, shell=True).decode("utf-8")
    draw.text((x,top+0),"IP: "+IP,font=font,fill=255)

    T=("T: %0.1f C" % bme280.temperature)
    draw.text((x,top+8),T,font=font,fill=255)
    
    P=("P: %0.1f hPa" %bme280.pressure)
    draw.text((x,top+16),P,font=font,fill=255)
    
    H=("Hum: %0.1f %%"%bme280.humidity)
    draw.text((x,top+25),H,font=font,fill=255)
   
    cmd = "df -h | awk '$NF==\"/\"{printf \"Disk: %d/%d GB %s\", $3,$2,$5}'"
    Disk = subprocess.check_output(cmd,shell=True).decode("utf-8")
    draw.text((x,top+33),Disk,font=font,fill=255)

    display.image(image)
    display.show()
    time.sleep(.1)
print("DONE")
