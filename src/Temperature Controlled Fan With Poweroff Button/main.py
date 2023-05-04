from gpiozero import CPUTemperature, DigitalOutputDevice, Button
from time import sleep
from subprocess import check_call

def shutdown():
    check_call(['sudo', 'poweroff'])

cpu = CPUTemperature(min_temp=40, max_temp=90)
fan = DigitalOutputDevice(17)

shutdown_btn = Button(4, hold_time=2)
shutdown_btn.when_held = shutdown

while True:
    print("Temp:" + str(cpu.temperature))
    if cpu.temperature > 40:
        fan.on()
    else:
        fan.off()

    sleep(10)

