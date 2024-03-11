# MuteOverThreshold

## How to setup
1. Install [SteelSeries GG](https://steelseries.com/gg)
2. Install [VB-CABLE Virtual Audio Device](https://vb-audio.com/Cable/)
3. Setup SteelSeries GG
    - Use Streamer Mode <br> ![obraz](https://github.com/GrzegorzWalewski/muteOverThreshold/assets/25950627/c8bc533d-dab6-4cf6-8256-802b824c2b66)
    - Set CABLE Input (VB-Audio Virtual Cable) as Your STREAM MIX device <br> ![obraz](https://github.com/GrzegorzWalewski/muteOverThreshold/assets/25950627/eca34adc-df1a-42cc-8220-7e58b4a89a19)  
    - MIC -> SHORTCUTS -> Personal -> Mute set to `ALT` + `=` <br> ![obraz](https://github.com/GrzegorzWalewski/muteOverThreshold/assets/25950627/0a99723f-8041-45a8-97e8-6cda6b79eef8)

3. Clone/Download as ZIP this repo
4. Install requiremenst: `pip install -r requirements.txt`

## How to run
1. `python app.py` <br> ![obraz](https://github.com/GrzegorzWalewski/muteOverThreshold/assets/25950627/00d152a7-23f6-49a7-a7af-408e8d5ec06c)
2. Select `CABLE Output`* <br> ![obraz](https://github.com/GrzegorzWalewski/muteOverThreshold/assets/25950627/348e99f1-120b-4752-9d52-450bf7032326)
3. Script should mute your mic when threshold of `0.14` RMS is crossed <br> ![obraz](https://github.com/GrzegorzWalewski/muteOverThreshold/assets/25950627/71b8b54f-592a-4988-8d41-04cfc0f2d800)

* there may be more then 1 device with such name - use the one with the lowest ID
