import platform
import os
from pystyle import Write, Colors, Box, System

my_system = platform.uname()
System.Title("PC Status Checker")

def clear_console():
    os.system('cls')

def Main():
    clear_console() #Clear terminal
    info = f"""
    System: {my_system.system} | Node Name: {my_system.node}
    release: {my_system.release} | Version: {my_system.version}
    Machine: {my_system.machine} | Processor: {my_system.processor}"""

    print(Colors.green, info, True)
if __name__ == "__main__":
    Main()
