
from machine import Pin, UART
from time import sleep
 
led3 = Pin(3, Pin.OUT)
led4= Pin(4, Pin.OUT)
led5 = Pin(5, Pin.OUT)
led6 = Pin(6, Pin.OUT)
led7 = Pin(7, Pin.OUT)
led8 = Pin(8, Pin.OUT)
led9 = Pin(9, Pin.OUT)
led10 = Pin(10, Pin.OUT)
led11 = Pin(11, Pin.OUT)

uart = UART(0, 9600)
# led6.off()
while True:
  if uart.any() > 0:
    data = uart.read()
    print(data)
    if "onled3" in data:
      led3.value(1)
      print('LED on \n')
      uart.write('LED3 on \n')
    elif "onled4" in data:
      led4.value(1)
      print('LED4 on\n')
    elif "onled5" in data:
      led5.value(1)
      print('LED5 on\n')
    elif "onled6" in data:
      led6.value(1)
      print('LED6 on\n')
    elif "onled7" in data:
      led7.value(1)
      print('LED7 on\n')
    elif "onled8" in data:
      led8.value(1)
      print('LED8 on\n')
    elif "onled9" in data:
      led9.value(1)
      print('LED9 on\n')
    elif "onled10" in data:
      led10.value(1)
      print('LED10 on\n')
    elif "onled11" in data:
      led11.value(1)
      print('LED11 on\n')
    elif "onall" in data:
        leds = (led3,led4,led5,led6,led7,led8,led9,led10,led11)
        for x in leds:
            x.on()
    elif "offall" in data:
        leds = (led3,led4,led5,led6,led7,led8,led9,led10,led11)
        for x in leds:
            x.off()

