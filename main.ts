let tempo = 0
input.onButtonPressed(Button.A, function () {
    music.play(music.builtinPlayableSoundEffect(soundExpression.giggle), music.PlaybackMode.UntilDone)
})
input.onButtonPressed(Button.B, function () {
    tempo = input.rotation(Rotation.Roll)
    music.play(music.stringPlayable("B G C A E C5 D F ", tempo), music.PlaybackMode.UntilDone)
})
