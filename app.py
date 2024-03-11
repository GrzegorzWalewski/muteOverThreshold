import sounddevice as sd
import numpy as np
import tkinter as tk
from pynput.keyboard import Key, Controller

muted = False
threshold = 0.14

def change_mute():
    global muted
    muted = not muted
    keyboard = Controller()
    # Simulate pressing the Alt key and then the = key
    with keyboard.pressed(Key.alt):
        keyboard.press('=')
        keyboard.release('=')

def list_audio_devices():
    devices = sd.query_devices()
    return [device['name'] for device in devices]

def create_gui():
    window = tk.Tk()
    window.tk.call('tk', 'scaling', 3)
    window.title("Mute Over Threshold")

    device_combo = tk.StringVar(window)
    device_combo.set(list_audio_devices()[2])  # Default selected device

    label_device = tk.Label(window, text="Select Audio Device:")
    label_device.pack()

    combo_device = tk.OptionMenu(window, device_combo, *list_audio_devices())
    combo_device.pack()

    label_rms = tk.Label(window, text="Current RMS Value:")
    label_rms.pack()

    rms_value = tk.Label(window, text="")
    rms_value.pack()

    label_mute = tk.Label(window, text="Microphone Status:")
    label_mute.pack()
    canvas = tk.Canvas(window, width=100, height=100)
    canvas.pack()

    def start_monitoring():
        monitoring.set(True)
        selected_device = device_combo.get()
        def monitor():
            nonlocal selected_device
            if monitoring.get():
                current_rms = get_current_rms(device_name=selected_device)
                rms_value.config(text=current_rms)
                canvas.create_oval(25, 25, 75, 75, fill="red") if current_rms > threshold else canvas.create_oval(25, 25, 75, 75, fill="green")
                window.after(1, monitor)  # Run again after 1 millisecond
        monitor()  # Start monitoring

    def stop_monitoring():
        monitoring.set(False)

    start_button = tk.Button(window, text="Start Monitoring", command=start_monitoring)
    start_button.pack()

    stop_button = tk.Button(window, text="Stop Monitoring", command=stop_monitoring)
    stop_button.pack()

    exit_button = tk.Button(window, text="Exit", command=window.destroy)
    exit_button.pack()

    monitoring = tk.BooleanVar()
    monitoring.set(True)

    window.mainloop()

def get_current_rms(device_name):
    stream = sd.InputStream(device=device_name, channels=1, samplerate=44100)
    stream.start()

    try:
        audio_data, _ = stream.read(1024)
        rms_value = np.sqrt(np.mean(audio_data**2))
        if rms_value > threshold:
            if not muted:
                print(f"Too loud! Muting {rms_value:.2f}")
                change_mute()
        else:
            if muted:
                print(f"Back to normal. Unmuting {rms_value:.2f}")
                change_mute()
        return rms_value
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
    finally:
        stream.stop()

if __name__ == "__main__":
    create_gui()