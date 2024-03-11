import sounddevice as sd
import numpy as np
from pynput.keyboard import Key, Controller

muted = False
treshold = 0.14

def change_mute():
    global muted
    muted = not muted
    keyboard = Controller()

    with keyboard.pressed(Key.alt):
        keyboard.press('=')
        keyboard.release('=')

def list_audio_devices():
    devices = sd.query_devices()
    for i, device in enumerate(devices):
        print(f"Device {i + 1}: {device['name']}")

def select_device():
    try:
        list_audio_devices()
        device_index = int(input("Enter the device index (1, 2, ...): ")) - 1
        selected_device = sd.query_devices(device=device_index)['name']
        print(f"Selected device: {selected_device}")
        return device_index
    except ValueError:
        print("Invalid input. Please enter a valid device index.")
        return select_device()

def monitor_rms(device_name):
    stream = sd.InputStream(device=device_name, channels=1, samplerate=44100)
    stream.start()

    try:
        while True:
            audio_data, overflowed = stream.read(1024)
            rms_value = np.sqrt(np.mean(audio_data**2))
            if rms_value > treshold:
                if not muted:
                    print(f"To loud! Muting {rms_value:.2f}")
                    change_mute()
            else:
                if muted:
                    print(f"Back to normal. Unmuting {rms_value:.2f}")
                    change_mute()
            # print(f"Current RMS ({device_name}): {rms_value:.2f}")
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
    finally:
        stream.stop()

if __name__ == "__main__":
    selected_output_device = select_device()
    monitor_rms(device_name=selected_output_device)
