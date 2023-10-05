#!/usr/bin/python3

import pygame
import socket
import time

# Define IP address and port number of the TCP server
TCP_IP = 'carl.local'
TCP_PORT = 4143

# Initialize pygame and the Xbox controller
pygame.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Create a TCP socket and connect to the server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((TCP_IP, TCP_PORT))

# Loop to continuously send Xbox controller data
while True:
    pygame.event.pump()

    # Get controller input values
    l_axis_x = joystick.get_axis(0)
    l_axis_y = joystick.get_axis(1)
    r_axis_x = joystick.get_axis(3)
    r_axis_y = joystick.get_axis(4)
    LeftTrigger = joystick.get_axis(2)
    RightTrigger = joystick.get_axis(5)
    button_a = joystick.get_button(0)
    button_b = joystick.get_button(1)
    button_x = joystick.get_button(2)
    button_y = joystick.get_button(3)
    button_start = joystick.get_button(7)
    LeftBumper = joystick.get_button(4)
    RightBumper = joystick.get_button(5)

    # Convert input values to bytes
    data = bytearray()
    data.append(int(l_axis_x * 127 + 127))
    data.append(int(l_axis_y * 127 + 127))
    data.append(int(r_axis_x * 127 + 127))
    data.append(int(r_axis_y * 127 + 127))
    data.append(int(LeftTrigger * 127 + 127))
    data.append(int(RightTrigger * 127 + 127))
    data.append(button_a)
    data.append(button_b)
    data.append(button_x)
    data.append(button_y)
    data.append(button_start)
    data.append(LeftBumper)
    data.append(RightBumper)

    # Send data over TCP socket
    sock.sendall(data)
    time.sleep(0.05)
