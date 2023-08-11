import subprocess
import threading
import ctypes
import os

def open_exe_file(exe_path):
    try:
        error_message = "An error occurred. Exit Code 1000"
        ctypes.windll.user32.MessageBoxW(None, error_message, "Error", 0x10)

        def open_program():
            subprocess.Popen([exe_path], shell=True)
            print("g0000")
        
        program_thread = threading.Thread(target=open_program)
        program_thread.start()
        program_thread.join()
    except FileNotFoundError:
        error_message = "An error occurred. Exit Code 0001, I dont think the program runs on ur os"
        ctypes.windll.user32.MessageBoxW(None, error_message, "Error", 0x10)
        print("b0000")
    except Exception as e:
        error_message = "An error occurred. Exit Code 0001, I dont think the program runs on ur os"
        ctypes.windll.user32.MessageBoxW(None, error_message, "Error", 0x10)     
        print("b0000")


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    exe_path = os.path.join(script_dir, "libraries", "gui.exe")
    open_exe_file(exe_path)