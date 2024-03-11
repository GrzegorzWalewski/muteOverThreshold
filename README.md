<h1 style="display: flex; align-items: center;">
  <img src="icon.png" alt="icon" style="width: 100px; height: 100px; margin-right: 10px;">
  MuteOverThreshold
</h1>
Mute Your microphone when PC output audio get's to loud to prevent echo. Prevent echo on discord when using speaker instead of headphones. Good alternative to push to talk.

## How to setup
1. Install [SteelSeries GG](https://steelseries.com/gg)
2. Install [VB-CABLE Virtual Audio Device](https://vb-audio.com/Cable/)
3. Setup SteelSeries GG
    - Use Streamer Mode <br> ![obraz](https://github.com/GrzegorzWalewski/muteOverThreshold/assets/25950627/c8bc533d-dab6-4cf6-8256-802b824c2b66)
    - Set CABLE Input (VB-Audio Virtual Cable) as Your STREAM MIX device <br> ![obraz](https://github.com/GrzegorzWalewski/muteOverThreshold/assets/25950627/eca34adc-df1a-42cc-8220-7e58b4a89a19)  
    - Set shortcut(keybindin) to `Pause/Break` button either in SteelSeries GG or Discord mute/unmute. I used `Pause/Break` button, as it's no longer used by anything, and spam clicking this button shouldn't make any harm ;)

4. Download latest release: [https://github.com/GrzegorzWalewski/muteOverThreshold/releases](https://github.com/GrzegorzWalewski/muteOverThreshold/releases)

## How to use
1. run `muteOverThreshold.exe`
2. You will see this beauty: <br> ![obraz](https://github.com/GrzegorzWalewski/muteOverThreshold/assets/25950627/2d76c43a-85f5-4458-a515-93ba477bce92)
3. You can set custom RMS Threshold - you just really have to experiment with this. For me `0.07` was working perfectly, but it all depends on your sound settings
4. Select `CABLE Output` - there may be more then 1 device with such name - use the one that's highest on the list
5. RED dot means, your microphone is muted; GREEN means it's unmuted
6. Click START, and the program should do it's magic!
