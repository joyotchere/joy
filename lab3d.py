#!/usr/bin/env python3
'''Lab 3 Disk Space Script'''
# Author ID: JoyOtchere

import subprocess

def free_space():
    # Launch the Linux command and capture the output
    result = subprocess.run(["df", "-h"], stdout=subprocess.PIPE, text=True)
    
    # Filter the output for the root directory using grep
    free_space_value = subprocess.run(
        ["grep", "/$"], input=result.stdout, stdout=subprocess.PIPE, text=True
    )
    
    # Extract the fourth column (free space) using awk
    free_space_value = subprocess.run(
        ["awk", "{print $4}"], input=free_space_value.stdout, stdout=subprocess.PIPE, text=True
    )
    
    # Return the free space value, stripped of any newline characters
    return free_space_value.stdout.strip()

if __name__ == '__main__':
    print(free_space())



