import smbus
import time
import RPi.GPIO as GPIO

rev = GPIO.RPI_REVISION
if rev == 2 or rev == 3:
    bus = smbus.SMBus(1)
else:
    bus = smbus.SMBus(0)

MOTOR_DEFAULT_ADDR = 0x14
MOTOR_CMD_BRAKE = 0x00
MOTOR_CMD_STOP = 0x01
MOTOR_CMD_CW = 0x02
MOTOR_CMD_CCW = 0x03
MOTOR_CMD_STANDBY = 0x04
MOTOR_CMD_NOT_STANDBY = 0x05
MOTOR_CMD_STEPPER_RUN = 0x06
MOTOR_CMD_STEPPER_STOP = 0x07
MOTOR_CMD_STEPPER_KEEP_RUN = 0x08
MOTOR_CMD_SET_ADDR = 0x11

def standby():
    bus.write_byte_data(MOTOR_DEFAULT_ADDR,MOTOR_CMD_STANDBY,0)
    
def notStandby():
    bus.write_byte_data(MOTOR_DEFAULT_ADDR,MOTOR_CMD_NOT_STANDBY,0)

# Speed is -255 to 255; Side is 0 or 1
def dcMotorRun(Speed,Side):
    Direction = MOTOR_CMD_CCW
    if Speed >= 0:
        Direction = MOTOR_CMD_CW
    Command = (abs(Speed) << 8) + Side
    print(Command)
    bus.write_word_data(MOTOR_DEFAULT_ADDR,Direction,Command)
    
# Side is 0 or 1
def dcMotorStop(Side):
    bus.write_byte_data(MOTOR_DEFAULT_ADDR,MOTOR_CMD_STOP,Side)
    
## MY CODE
def dcrun():
    Side = 0
    print("running...")
    standby()
    #notStandby()
    dcMotorRun(-80,Side)
    time.sleep(1)
    dcMotorRun(80,Side)
    time.sleep(1)
    dcMotorStop(Side)
    time.sleep(1)

print("setup")
dcrun()