---
date: 2024-08-03 09:54
templateKey: blog-post
title: Printing 42 keys at once
published: false
tags:
  - 3d-printing
  - tmk
  - keeb
---
I'm working on creating some gcode to create a whole set of key caps in one print, it is getting tedious to print them one at a time, and my past experience with my printer proves that printing a bunch of separate pieces increases the chances of failure.  I don't want to end up with 42 keys that are half done and a ball of filament.

## figuring out the coordinates

To figure out the coordinates I printed one key cap, and manually jogged the printer in position to knock off the cap, then sweep it out of the way.

![designing-a-knock-off-key-20240803095740665.webp](https://dropper.wayl.one/api/file/26a0eaf3-fbee-4570-80a7-0c14debf2017.webp)
> print head in position to knock

![designing-a-knock-off-key-20240803095731272.webp](https://dropper.wayl.one/api/file/03dcb61b-79d7-43ab-a1ac-f9503b7b921e.webp)
> Position before the knock

![designing-a-knock-off-key-20240803150150445.webp](https://dropper.wayl.one/api/file/066c28a9-bfd6-4214-83e0-54d2e93e94c9.webp)
> Position after the sweep

## gcode

I opened the gcode split it into start.gcode, end.gcode, and part.gcode.

### start.gcode

``` gcode
;FLAVOR:Marlin
;TIME:1488
;Filament used: 0.265511m
;Layer height: 0.12
;MINX:105.708
;MINY:101.231
;MINZ:0.12
;MAXX:113.512
;MAXY:118.776
;MAXZ:17.04
;TARGET_MACHINE.NAME:Creality Ender-3 S1 Pro
;Generated with Cura_SteamEngine 5.8.0
M82 ;absolute extrusion mode
; Ender 3 S1 Pro Start G-code
; M413 S0 ; Disable power loss recovery
G92 E0 ; Reset Extruder

; Prep surfaces before auto home for better accuracy
M140 S60
M104 S200

G28 ; Home all axes
G1 Z10.0 F3000 ; Move Z Axis up little to prevent scratching of Heat Bed
G1 X0 Y0

M190 S60
M109 S200

M82 ;absolute extrusion mode
; Ender 3 S1 Pro Start G-code
; M413 S0 ; Disable power loss recovery
G92 E0 ; Reset Extruder

; Prep surfaces before auto home for better accuracy
M140 S60
M104 S200

G28 ; Home all axes
G1 Z10.0 F3000 ; Move Z Axis up little to prevent scratching of Heat Bed
G1 X0 Y0

M190 S60
M109 S200

G1 X0.1 Y20 Z0.3 F5000.0 ; Move to start position
G1 X0.1 Y200.0 Z0.3 F1500.0 E15 ; Draw the first line
G1 X0.4 Y200.0 Z0.3 F5000.0 ; Move to side a little
G1 X0.4 Y20 Z0.3 F1500.0 E30 ; Draw the second line

```

### end.gcode

```gcode
M140 S0 ; Turn off bed
M107 ; Turn off fan
G91 ;Relative positioning
G1 E-2 F2700 ;Retract a bit
G1 E-2 Z0.2 F2400 ;Retract and raise Z
G1 X5 Y5 F3000 ;Wipe out
G1 Z10 ;Raise Z more
G90 ;Absolute positioning

G1 X0 Y220 ;Present print
M106 S0 ;Turn-off fan
M104 S0 ;Turn-off hotend
M140 S0 ;Turn-off bed

M84 X Y E ;Disable all steppers but Z

M82 ;absolute extrusion mode
M104 S0
;End of Gcode
;SETTING_3 {"global_quality": "[general]\\nversion = 4\\nname = Super Quality #2
;SETTING_3 \\ndefinition = creality_ender3s1pro\\n\\n[metadata]\\ntype = quality
;SETTING_3 _changes\\nquality_type = super\\nsetting_version = 23\\n\\n[values]\
;SETTING_3 \nadhesion_type = none\\nsupport_type = buildplate\\n\\n", "extruder_
;SETTING_3 quality": ["[general]\\nversion = 4\\nname = Super Quality #2\\ndefin
;SETTING_3 ition = creality_ender3s1pro\\n\\n[metadata]\\ntype = quality_changes
;SETTING_3 \\nquality_type = super\\nsetting_version = 23\\nposition = 0\\n\\n[v
;SETTING_3 alues]\\nbrim_gap = 0.1\\nspeed_print = 120\\nsupport_angle = 35\\nz_
;SETTING_3 seam_corner = z_seam_corner_inner\\nz_seam_position = right\\n\\n"]}

```

### part.gcode

Now part.gcode is the rest of the gcode, and is 22k lines long, I'll spare putting that in this post.

## Writing the knock and sweep

Now that I have the coordinates, and my gcode split up, I am going to write the code for the knock and sweep by hand, and just add this to the end of part.gcode.

```gcode
; KNOCK AND SWEEP
G0 X80 Y140 ; move to knock position
G0 Z2 ; lower z to knock
G0 X140 ; knock
G0 Y40 ; sweep
```

## A python script to make multiples

Now I wrote this python script to generate a gcode file to print `n` number of caps

```python
from pathlib import Path
import sys

n = int(sys.argv[1])
print("printing " + str(n) + " times")


start = Path("start.gcode").read_text()
end = Path("end.gcode").read_text()
part = Path("part.gcode").read_text()

full = start + part * n + end
Path("kp-lame-normal-" + str(n) + ".gcode").write_text(full)

```

```python
python render.py 42
```

## Results

The final result here is me printing out 42 new caps in this beautiful black and purple silk fillament.

![knock-and-sweep.mp4](https://dropper.wayl.one/api/file/7dacc55a-666f-4592-bc3b-cb46324227f8.mp4)
