tempo = 0

def on_button_pressed_a():
    music.play(music.builtin_playable_sound_effect(soundExpression.giggle),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global tempo
    tempo = input.rotation(Rotation.PITCH)
    music.play(music.string_playable("B G C A E C5 D F ", tempo),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.B, on_button_pressed_b)
