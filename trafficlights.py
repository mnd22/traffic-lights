#! /usr/bin/env python3
from gpiozero import LED
from time import sleep

green = LED(27)
amber = LED(22)
red = LED(17)

def main():
  print("Starting lights cycle")
  cyclelights(3, 3, 1, 3)
  print("Lights cycle complete")

def cyclelights(numcycles = 5,
                redperiod = 10.0,
                amberperiod = 2.0,
                greenperiod = 10.0):

  for ii in range(numcycles):
    print("Red")    
    red.on()
    sleep(redperiod)

    print("Red & Amber")
    amber.on()
    sleep(amberperiod)
    red.off()
    amber.off()

    print("Green")
    green.on()
    sleep(greenperiod)
    green.off()

    print("Amber")    
    amber.on()
    sleep(amberperiod)
    amber.off()

def redonly():
  green.off()
  amber.off()
  red.on()

def redamber():
  green.off()
  amber.on()
  red.on()

def greenonly():
  amber.off()
  red.off()
  green.on()

def amberonly():
  green.off()
  red.off()
  amber.on()
  
def alloff():
  green.off()
  red.off()
  amber.off()

def flash_forever():
  print("Starting to flash")

  try:
    while True:
      red.on()
      sleep(1)
      red.off()
      sleep(1)
      yellow.on()
      sleep(1)
      yellow.off()
      sleep(1)
      yellow.on()
      red.on()
      sleep(1)
      yellow.off()
      red.off()
      sleep(1)
  except KeyboardInterrupt:
    print("Stopped flashing")

if __name__ == "__main__":
  main()
