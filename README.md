# MuteOverThreshold

## How to setup
1. Install (SteelSeries GG)[https://steelseries.com/gg] 
2. Install (VB-CABLE Virtual Audio Device.)[https://vb-audio.com/Cable/]
3. Setup SteelSeries GG
    - Use Streamer Mode
    - Set CABLE Input (VB-Audio Virtual Cable) as Your STREAM MIX device
    - MIC -> SHORTCUTS -> Personal -> Mute set to `ALT` + `=`
3. Clone/Download as ZIP this repo
4. Install requiremenst: `pip install requirements.txt`

## How to run
1. `python app.py`
2. Select `CABLE Output`*
3. Script should mute your mic when threshold of `0.14` RMS is crossed

* there may be more then 1 device with such name - use the one with the lowest ID
