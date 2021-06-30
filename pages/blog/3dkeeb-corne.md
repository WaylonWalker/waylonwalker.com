---
templateKey: blog-post
tags: ['keeb', ]
title: My experience with a new 3dkeeb corne
date: 2021-06-21T14:27:19
status: draft

---


## specs

## first days typing


## first days working

What did I sign myself up for? If the lower typing speed with alpha characters
was not enough throw in special characters and keybings I setup long ago and
only remember by muscle memory.  I have so far killed my tmux pane instead of
zooming in (m-x instead of m-z), killed my zsh line instead of paste to the end
of a command (c-c instead of c-v).


## VIA

```
LT(1, KC_ENT)
LT(1, KC_TAB)
LT(1, KC_SHIFT)

MT(MOD_RSHFT, KC_ESC)
MT(MOD_HYPR, KC_GESC)

```

## setting up qmk cli

``` bash
conda create -n qmk python=3.8 -y

qmk config compile.keyboard=crkbd/rev1 compile.keymap=default
qmk config user.keyboard=crkbd/rev1 user.keymap=default

# This will clone into ~/qmk_firmware
# you can change this behavior by setting QMK_HOME
# export QMK_HOME=~/custo_qmk_home_dir
qmk setup

# qmk setup took 10 minutes on my machine with wsl over a mobile network
```

``` bash
qmk setup 
ImportError: Unable to load any of the following libraries:libhidapi-hidraw.so libhidapi-hidraw.so.0 libhidapi-libusb.so libhidapi-libusb.so.0 libhidapi-iohidmanager.so libhidapi-iohidmanager.so.0 libhidapi.dylib hidapi.dll libhidapi-0.dll

pip install hidapi
sudo apt-get install python-dev libusb-1.0-0-dev libudev-dev
sudo apt-get update
sudo apt-get install python-dev libusb-1.0-0-dev libudev-dev
qmk setup
# https://pypi.org/project/hid/
apt install libhidapi-hidraw0
qmk setup
```
