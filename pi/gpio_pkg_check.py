try:
  import gpiozero
  print('GPIOZero available')
except:
  print('GPIOZero is not available. Install with "pip install gpiozero"')

try:
  import pigpio
  print('pigpio available')
except:
  print('pigpio unavailable. Install with "pip install pigpio"')