---
title: '💭 Pinout and Schematic - nice!nano'
date: 2024-07-10T12:40:26
template: link
link: https://nicekeyboards.com/docs/nice-nano/pinout-schematic/
tags:
  - keyboard
  - thoughts
  - thought
  - link
published: true

---

![[https://nicekeyboards.com/docs/nice-nano/pinout-schematic/]]

Pinout for nice!nano boards.   Note that P0.15 means gpio port 0 pin 15, they can be referenced in zmk when setting column and row pins.


``` c
#include <dt-bindings/zmk/matrix_transform.h>

/ {
    chosen {
        zmk,kscan = &default_kscan;
        zmk,matrix_transform = &default_transform;
        /delete-property/ zephyr,console;
        /delete-property/ zephyr,shell-uart;
    };

    default_kscan: kscan {
        compatible = "zmk,kscan-gpio-matrix";
        label = "default_kscan";
        diode-direction = "col2row";

        col-gpios
            = <&gpio0 31 GPIO_ACTIVE_HIGH>
            , <&gpio0 29 GPIO_ACTIVE_HIGH>
            , <&gpio0 2 GPIO_ACTIVE_HIGH>
            ;

        row-gpios
            = <&gpio1 15 (GPIO_ACTIVE_HIGH | GPIO_PULL_DOWN)>
            , <&gpio1 13 (GPIO_ACTIVE_HIGH | GPIO_PULL_DOWN)>
            , <&gpio1 11 (GPIO_ACTIVE_HIGH | GPIO_PULL_DOWN)>
            ;
    };

    default_transform: matrix_transform {
        compatible = "zmk,matrix-transform";
        columns = <3>;
        rows = <3>;
        map = <
            RC(0,0) RC(0,1) RC(0,2)
            RC(1,0) RC(1,1) RC(1,2)
            RC(2,0) RC(2,1) RC(2,2)
        >;
    };
};


```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
