---
date: 2022-04-07 13:14:20.752946
templateKey: til
title: pygame events are queued | Don't make this mistake
tags:
  - python
  - pygame

---

pygame events are stored in a queue, by default the most suggested way
shown in all tutorials "`pumps`" the queue, which removes all the
messages.

## start up pygame

You don't necessarily need a full
[boilerplate](https://waylonwalker.com/til/pygame-boilerplate-apr-2022/)
to start looking at events, you just just need to `pygame.init()` and
to capture any keystrokes you need a window to capture them on, so you
will need a display running.

```python
import pygame
pygame.init()
pygame.display.set_mode((854, 480))
```

## get some events

Let's use pygames normal `event.get` method to get events.

```python
events = pygame.event.get()
```

printing the events reveal this

```python
[
    <Event(1541-JoyDeviceAdded {'device_index': 0, 'guid': '030000005e0400008e02000010010000'})>,
    <Event(4352-AudioDeviceAdded {'which': 0, 'iscapture': 0})>,
    <Event(4352-AudioDeviceAdded {'which': 1, 'iscapture': 0})>,
    <Event(4352-AudioDeviceAdded {'which': 2, 'iscapture': 0})>,
    <Event(4352-AudioDeviceAdded {'which': 0, 'iscapture': 1})>,
    <Event(4352-AudioDeviceAdded {'which': 1, 'iscapture': 1})>,
    <Event(32774-WindowShown {'window': None})>,
    <Event(32777-WindowMoved {'x': 535, 'y': 302, 'window': None})>,
    <Event(32770-VideoExpose {})>,
    <Event(32776-WindowExposed {'window': None})>,
    <Event(32788-WindowTakeFocus {'window': None})>,
    <Event(32768-ActiveEvent {'gain': 1, 'state': 1})>,
    <Event(32785-WindowFocusGained {'window': None})>,
    <Event(768-KeyDown {'unicode': 'a', 'key': 97, 'mod': 0, 'scancode': 4, 'window': None})>,
    <Event(771-TextInput {'text': 'a', 'window': None})>,
    <Event(768-KeyDown {'unicode': 's', 'key': 115, 'mod': 0, 'scancode': 22, 'window': None})>,
    <Event(771-TextInput {'text': 's', 'window': None})>,
    <Event(769-KeyUp {'unicode': 'a', 'key': 97, 'mod': 0, 'scancode': 4, 'window': None})>,
    <Event(768-KeyDown {'unicode': 'd', 'key': 100, 'mod': 0, 'scancode': 7, 'window': None})>,
    <Event(771-TextInput {'text': 'd', 'window': None})>,
    <Event(769-KeyUp {'unicode': 's', 'key': 115, 'mod': 0, 'scancode': 22, 'window': None})>,
    <Event(769-KeyUp {'unicode': 'd', 'key': 100, 'mod': 0, 'scancode': 7, 'window': None})>,
    <Event(768-KeyDown {'unicode': 'f', 'key': 102, 'mod': 0, 'scancode': 9, 'window': None})>,
    <Event(771-TextInput {'text': 'f', 'window': None})>,
    <Event(769-KeyUp {'unicode': 'f', 'key': 102, 'mod': 0, 'scancode': 9, 'window': None})>,
    <Event(768-KeyDown {'unicode': 's', 'key': 115, 'mod': 0, 'scancode': 22, 'window': None})>,
    <Event(771-TextInput {'text': 's', 'window': None})>,
    <Event(768-KeyDown {'unicode': 'd', 'key': 100, 'mod': 0, 'scancode': 7, 'window': None})>,
    <Event(771-TextInput {'text': 'd', 'window': None})>,
    <Event(769-KeyUp {'unicode': 's', 'key': 115, 'mod': 0, 'scancode': 22, 'window': None})>,
    <Event(769-KeyUp {'unicode': 'd', 'key': 100, 'mod': 0, 'scancode': 7, 'window': None})>,
    <Event(768-KeyDown {'unicode': 'f', 'key': 102, 'mod': 0, 'scancode': 9, 'window': None})>,
    <Event(771-TextInput {'text': 'f', 'window': None})>,
    <Event(768-KeyDown {'unicode': 'a', 'key': 97, 'mod': 0, 'scancode': 4, 'window': None})>,
    <Event(771-TextInput {'text': 'a', 'window': None})>,
    <Event(769-KeyUp {'unicode': 'f', 'key': 102, 'mod': 0, 'scancode': 9, 'window': None})>,
    <Event(768-KeyDown {'unicode': 's', 'key': 115, 'mod': 0, 'scancode': 22, 'window': None})>,
    <Event(771-TextInput {'text': 's', 'window': None})>,
    <Event(769-KeyUp {'unicode': 'a', 'key': 97, 'mod': 0, 'scancode': 4, 'window': None})>,
    <Event(768-KeyDown {'unicode': 'd', 'key': 100, 'mod': 0, 'scancode': 7, 'window': None})>,
    <Event(771-TextInput {'text': 'd', 'window': None})>,
    <Event(769-KeyUp {'unicode': 's', 'key': 115, 'mod': 0, 'scancode': 22, 'window': None})>,
    <Event(769-KeyUp {'unicode': 'd', 'key': 100, 'mod': 0, 'scancode': 7, 'window': None})>,
    <Event(768-KeyDown {'unicode': 'f', 'key': 102, 'mod': 0, 'scancode': 9, 'window': None})>,
    <Event(771-TextInput {'text': 'f', 'window': None})>,
    <Event(769-KeyUp {'unicode': 'f', 'key': 102, 'mod': 0, 'scancode': 9, 'window': None})>,
    <Event(768-KeyDown {'unicode': 'a', 'key': 97, 'mod': 0, 'scancode': 4, 'window': None})>,
    <Event(771-TextInput {'text': 'a', 'window': None})>,
    <Event(768-KeyDown {'unicode': 's', 'key': 115, 'mod': 0, 'scancode': 22, 'window': None})>,
    <Event(771-TextInput {'text': 's', 'window': None})>,
    <Event(768-KeyDown {'unicode': 'd', 'key': 100, 'mod': 0, 'scancode': 7, 'window': None})>,
    <Event(771-TextInput {'text': 'd', 'window': None})>,
    <Event(769-KeyUp {'unicode': 'a', 'key': 97, 'mod': 0, 'scancode': 4, 'window': None})>,
    <Event(769-KeyUp {'unicode': 's', 'key': 115, 'mod': 0, 'scancode': 22, 'window': None})>,
    <Event(769-KeyUp {'unicode': 'd', 'key': 100, 'mod': 0, 'scancode': 7, 'window': None})>,
    <Event(768-KeyDown {'unicode': 'f', 'key': 102, 'mod': 0, 'scancode': 9, 'window': None})>,
    <Event(771-TextInput {'text': 'f', 'window': None})>,
    <Event(769-KeyUp {'unicode': 'f', 'key': 102, 'mod': 0, 'scancode': 9, 'window': None})>,
    <Event(768-KeyDown {'unicode': 's', 'key': 115, 'mod': 0, 'scancode': 22, 'window': None})>,
    <Event(771-TextInput {'text': 's', 'window': None})>,
    <Event(769-KeyUp {'unicode': 's', 'key': 115, 'mod': 0, 'scancode': 22, 'window': None})>,
    <Event(768-KeyDown {'unicode': 'd', 'key': 100, 'mod': 0, 'scancode': 7, 'window': None})>,
    <Event(771-TextInput {'text': 'd', 'window': None})>,
    <Event(769-KeyUp {'unicode': 'd', 'key': 100, 'mod': 0, 'scancode': 7, 'window': None})>,
    <Event(768-KeyDown {'unicode': 'f', 'key': 102, 'mod': 0, 'scancode': 9, 'window': None})>,
    <Event(771-TextInput {'text': 'f', 'window': None})>,
    <Event(769-KeyUp {'unicode': 'f', 'key': 102, 'mod': 0, 'scancode': 9, 'window': None})>,
    <Event(768-KeyDown {'unicode': 's', 'key': 115, 'mod': 0, 'scancode': 22, 'window': None})>,
    <Event(771-TextInput {'text': 's', 'window': None})>,
    <Event(769-KeyUp {'unicode': 's', 'key': 115, 'mod': 0, 'scancode': 22, 'window': None})>,
    <Event(768-KeyDown {'unicode': 'd', 'key': 100, 'mod': 0, 'scancode': 7, 'window': None})>,
    <Event(771-TextInput {'text': 'd', 'window': None})>,
    <Event(769-KeyUp {'unicode': 'd', 'key': 100, 'mod': 0, 'scancode': 7, 'window': None})>,
    <Event(768-KeyDown {'unicode': '', 'key': 1073742051, 'mod': 1024, 'scancode': 227, 'window': None})>,
    <Event(772-Unknown {})>,
    <Event(769-KeyUp {'unicode': '', 'key': 1073742051, 'mod': 0, 'scancode': 227, 'window': None})>,
    <Event(32768-ActiveEvent {'gain': 0, 'state': 1})>,
    <Event(32786-WindowFocusLost {'window': None})>,
    <Event(772-Unknown {})>
]
```

## Lets get some more events.

Let's say that we have multpile sprites all asking for the events from
different places in our game. If we assume that our game loop runs very
fastand we get events one after another the second one will have no
events.

```python
events_one = pygame.event.get()
events_two = pygame.event.get()
```
printing the events reveals that there are no events, well i

```python
[]
```

## Making things more maddening

Even simple games don't quite run infinitely fast there is some delay,
with this delay most events will go to event_one, while any that occur
in the short time between event_one and two will be in event_two's
queue.


```python
import time
events_one = pygame.event.get()
time.sleep(.05) # simulating some delay that would naturally occur
events_two = pygame.event.get()
```

## How to Resolve this

Store events for each frame in memory.

## Pump

I thought `pump=False` would be the answer I was looking for, but I was
proven wrong.  It does not behave intuitivly to me.

```python
events_one = pygame.event.get(pump=False)
events_two = pygame.event.get(pump=False)
events_three = pygame.event.get()
```

`events_one` and `events_three` will have a list of events, while
`events_two` will be empty.  It seems that `pump=False` leaves the
events there for the next `event.get()`, but appears cleared to any
`event.get(pump=False)`.

## Keep a Game State

If you want objects to do their own event handling, outside of the main
game, you will need to give them some game state with the events in it.
However you decide, you may only call `event.get()` once per game loop
otherwise weird things will happen.
