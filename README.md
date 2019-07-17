# DMX485
## Requirements
This script requires pyserial.
```
pip install --user pyserial
```

## Installation
Install from pip:
```
pip install --user dmx485
```
Install from source:
```
python setup.py install
```

## Hardware Compatibility
This should work with any FTDI RS485 dongle or any of the similar knock-offs.

FTDI to RS485 cheap dongle:

https://fr.aliexpress.com/item/USB-to-TTL-RS485-Serial-Converter-Adapter-FTDI-Module-FT232RL-SN75176-double-function-double/32771847720.html?spm=a2g0w.search0104.3.15.63586239S7KSon&ws_ab_test=searchweb0_0,searchweb201602_2_10065_10068_319_10892_317_10696_453_10084_454_10083_10618_10304_10307_10820_10821_538_537_10302_536_10843_10059_10884_10887_100031_321_322_10103,searchweb201603_51,ppcSwitch_0&algo_expid=6957aa39-4868-4f8d-ac7f-b10f610a4a24-2&algo_pvid=6957aa39-4868-4f8d-ac7f-b10f610a4a24


## Hardware Example
https://stevenbreuls.com/2013/05/diy-usb-dmx-dongle-interface-for-under-10/

## Usage
First create an instance of dmx.DMX_Serial(), then start the background thread. Once that is running the dongle will begin sending a full DMX universe.
To change the value of a channel use set_data(). This function takes a bytes() object with 512 bytes, each representing a single DMX channel. It will be sent on the next DMX refresh.
```
import time
import dmx

sender = dmx.DMX_Serial()
sender.start()
for i in range(200):
    if i % 2:
        sender.set_data(bytes((255,)*512))
    else:
        sender.set_data(bytes((0,)*512))
    time.sleep(1)
```