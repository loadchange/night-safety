input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    a = 1
    music.startMelody(music.builtInMelody(Melodies.PowerUp), MelodyOptions.Once)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    a = 0
    music.startMelody(music.builtInMelody(Melodies.PowerDown), MelodyOptions.Once)
})
let light2 = 0
let a = 0
led.enable(false)
basic.forever(function on_forever() {
    
    light2 = input.lightLevel()
})
basic.forever(function on_forever2() {
    basic.showLeds(`
        # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
    `)
})
basic.forever(function on_forever3() {
    if (a == 1) {
        if (light2 < 100) {
            while (a == 1) {
                basic.pause(1000)
                led.enable(true)
                basic.pause(1000)
                led.enable(false)
            }
        }
        
    }
    
})