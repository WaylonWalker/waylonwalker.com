---
date: 2022-02-11 22:01:41.246996
templateKey: til
title: Bluetooth at the command line on Ubuntu
tags:
  - linux
  - desktop

---

One thing about moving to a tiling window manager like awesome wm or i3 is that
they are so lightweight they are all missing things like bluetooth gui's out of
the box, and you generally bring your own.  Today I just needed to connet a new
set of headphones, so I decided to just give the `bluetoothctl` cli a try.  It
seems to come with Ubuntu, I don't think I did anything to get it.

``` bash
bluetoothctl
```

Running `bluetoothctl` pops you into a repl/shell like bah, python, or ipython.
From here you can execute `bluetoothctl` commands.


Here is what I had to do to connect my headphones.

``` bash
# list out the commands available
help

# scan for new devices and stop when you see your device show up
scan on
scan off

# list devices
devices
paired-devices

# pair the device
pair XX:XX:XX:XX:XX:XX

# now your device should show up in the paired list
paired-devices

# connet the device
connect XX:XX:XX:XX:XX:XX
```

## help

Here is the output of the help menu on my machine, it seems pretty straight
forward to block, and remove devices from here.

note ctrl revers to the bluetooth controller on the machine you are on, and dev
refers to a device id.

``` bash
Menu main:
Available commands:
-------------------
advertise                                         Advertise Options Submenu
scan                                              Scan Options Submenu
gatt                                              Generic Attribute Submenu
list                                              List available controllers
show [ctrl]                                       Controller information
select <ctrl>                                     Select default controller
devices                                           List available devices
paired-devices                                    List paired devices
system-alias <name>                               Set controller alias
reset-alias                                       Reset controller alias
power <on/off>                                    Set controller power
pairable <on/off>                                 Set controller pairable mode
discoverable <on/off>                             Set controller discoverable mode
agent <on/off/capability>                         Enable/disable agent with given capability
default-agent                                     Set agent as the default one
advertise <on/off/type>                           Enable/disable advertising with given type
set-alias <alias>                                 Set device alias
scan <on/off>                                     Scan for devices
info [dev]                                        Device information
pair [dev]                                        Pair with device
trust [dev]                                       Trust device
untrust [dev]                                     Untrust device
block [dev]                                       Block device
unblock [dev]                                     Unblock device
remove <dev>                                      Remove device
connect <dev>                                     Connect device
disconnect [dev]                                  Disconnect device
menu <name>                                       Select submenu
version                                           Display version
quit                                              Quit program
exit                                              Quit program
help                                              Display help about this program
```

## Final Impressions

This was something that I have never used, and thought it would be intimidating
but it worked great first try out of the box.  It could have been my device on
the other end, but this was one of the least frustrations I have had pairing a
new device.
