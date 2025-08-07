import platform
import os

def play_beep():
    if platform.system() == "Windows":
        import winsound
        winsound.Beep(1000, 100)
    else:
        print("\a", end="") 

def play_start_sound():
    sound_path = os.path.join(os.path.dirname(__file__), "happy_piano_theme.wav")
    # Use winsound or subprocess for cross-platform playback
    if platform.system() == "Windows":
        import winsound
        winsound.PlaySound(sound_path, winsound.SND_FILENAME | winsound.SND_ASYNC)
    elif platform.system() == "Darwin":  # macOS
        import subprocess
        subprocess.Popen(["afplay", sound_path])
    else:  # Linux
        import subprocess
        subprocess.Popen(["aplay", sound_path])

if __name__ == "__main__":
    print("Testing play_beep()...")
    play_beep()
    input("Press Enter to test play_start_sound()...")
    print("Testing play_start_sound()...")
    play_start_sound()
    input("Press Enter to exit...")