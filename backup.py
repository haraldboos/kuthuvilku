from machine import Pin, UART

uart = UART(0, 9600)
led2=Pin(2,Pin.OUT)#5
led3 =Pin(3,Pin.OUT)#chief guest 3
led4 = Pin(4,Pin.OUT)#6
led5 = Pin(5,Pin.OUT)#7
led6 = Pin(6,Pin.OUT)#principle 4
led7 = Pin(7,Pin.OUT)#chief guset1
led8 = Pin(8,Pin.OUT)#8
led9 = Pin(9,Pin.OUT)#9
led10 = Pin(10,Pin.OUT)#chief guest 2
leds = (led2,led3,led4,led5,led6,led7,led8,led9,led10)

# for x in leds:
    
#     x.off()
while True:
  if uart.any() > 0:
    data = uart.read()
    print(data)
    if "onled2" in data:
      led2.value(1)
      print('LED on \n')
#       uart.write('LED3 on \n')
      uart.write('welcome to Trailblazer Awarding Cermony \n')
    elif "onled3" in data:
      led3.value(1)
      uart.write('welcome MR.Nirojan rajkumar\n')
      print('LED4 on\n')
    elif "onled4" in data:
      led4.value(1)
      uart.write('welcome to Trailblazer Awarding Cermony \n')
      print('LED on\n')
    elif "onled5" in data:
      led5.value(1)
      uart.write('welcome to Trailblazer Awarding Cermony \n')

      print('LED6 on\n')
    elif "onled6" in data:
      led6.value(1)
      uart.write('welcome to Trailblazer Awarding Cermony \n')
      print('LED7 on\n')
    elif "onled7" in data:
      led7.value(1)
      uart.write('welcome to MR.Kathirkamanathan Selvakumar\n')
      print('LED8 on\n')
    elif "onled8" in data:
      led8.value(1)
      uart.write('welcome to Trailblazer Awarding Cermony \n')

      print('LED9 on\n')
    elif "onled9" in data:
      led9.value(1)
      uart.write('welcome to Trailblazer Awarding Cermony \n')
      print('LED10 on\n')
    elif "onled10" in data:
      led10.value(1)
      uart.write('Welcome MR.Makeshwaran Rajethan\n')
      print('LED11 on\n')
    elif "onall" in data:
#         leds = (led3,led4,led5,led6,led7,led8,led9,led10,led11)
        for x in leds:
            x.on()
        uart.write('all leds on  \n')
    elif "offall" in data:
#         leds = (led3,led4,led5,led6,led7,led8,led9,led10,led11
        for x in leds:
            x.off()
        uart.write('all led off\n')

