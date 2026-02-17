---
title: '💭 all lt keys to hl · WaylonWalker/zmk-config-42block@ce25356'
date: 2024-07-22T13:42:46
templateKey: link
link: https://github.com/WaylonWalker/zmk-config-42block/commit/ce25356e88eb2439182201700314133de719457e
tags:
  - keyboard
  - zmk
published: true

---

> Today I swapped out all of my keys that are used dual purpose for letters and layers to homerow layers.  This prevents goofy things happening when rolling, and prefers-tap makes it so that keys that are rolled over get hit as letters instead of as layers.  This was one of my biggest hurdles jumping into zmk,  lt as a homerow key just does not behave the same as the ht/hm behaviors with tap-preferred set.


!!! seealso
  See previous commit where I added the hl https://github.com/WaylonWalker/zmk-config-42block/commit/9522c859cdf024a2c2b73931c130ddc907c09ffc

``` c
        hl: homerow_layer {
            compatible = "zmk,behavior-hold-tap";
            label = "HOMEROW_LAYER";
            bindings = <&mo>, <&kp>;

            #binding-cells = <2>;
            tapping-term-ms = <150>;
            flavor = "tap-preferred";
        };
```

[Original thought](https://github.com/WaylonWalker/zmk-config-42block/commit/ce25356e88eb2439182201700314133de719457e)
