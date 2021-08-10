import board
import busio
from digitalio import DigitalInOut
from adafruit_pn532.i2c import PN532_I2C

class nfcUtil:
     
    def __init__(self):
            self.i2c = busio.I2C(board.SCL, board.SDA)
            self.reset_pin = DigitalInOut(board.D6)
            self.req_pin = DigitalInOut(board.D12)
            self.pn532 = PN532_I2C(self.i2c, debug=False, reset=self.reset_pin, req=self.req_pin)
            self.ic, ver, rev, support = self.pn532.firmware_version
            self.pn532.SAM_configuration()
    
    def get_uid(self):
        while True:
            uid_raw = self.pn532.read_passive_target(timeout=0.5)
            uid = ''
            if uid_raw is None:
                continue
            for byte in uid_raw:
                uid += str(byte)
            return uid