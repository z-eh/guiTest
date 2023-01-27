import machine

led = machine.Pin(25, machine.Pin.OUT)

while True:
    command = input()
    if command == "toggle":
        led.value(not led.value())
