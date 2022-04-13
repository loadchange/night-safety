def on_button_pressed_a():
    global a
    a = 1
    music.start_melody(music.built_in_melody(Melodies.POWER_UP), MelodyOptions.ONCE)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global a
    a = 0
    music.start_melody(music.built_in_melody(Melodies.POWER_DOWN),
        MelodyOptions.ONCE)
input.on_button_pressed(Button.B, on_button_pressed_b)

light2 = 0
a = 0
led.enable(False)

def on_forever():
    global light2
    light2 = input.light_level()
basic.forever(on_forever)

def on_forever2():
    basic.show_leds("""
        # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
    """)
basic.forever(on_forever2)

def on_forever3():
    if a == 1:
        if light2 < 100:
            while a == 1:
                basic.pause(1000)
                led.enable(True)
                basic.pause(1000)
                led.enable(False)
basic.forever(on_forever3)
