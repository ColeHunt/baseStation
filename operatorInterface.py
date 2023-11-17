#!/usr/bin/python3

import pygame
import socket
import time

# Define IP address and port number of the TCP server
TCP_IP = '2610:130:110:1525:47e7:9414:7e67:15e4'
TCP_PORT = 4143

# Initialize pygame and the Xbox controller
pygame.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Create a TCP socket and connect to the server
sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
sock.connect((TCP_IP, TCP_PORT))

# Loop to continuously send Xbox controller data
while True:
    pygame.event.pump()

    # Get controller input values
    l_axis_x = joystick.get_axis(0) # 0
    l_axis_y = joystick.get_axis(1) # 1
    leftTrigger = joystick.get_axis(2) # 2
    rightTrigger = joystick.get_axis(5) # 3
    button_a = joystick.get_button(0) # 4
    button_b = joystick.get_button(1) # 5
    button_x = joystick.get_button(2) # 6
    button_y = joystick.get_button(3) # 7
    button_back = joystick.get_button(6) # 8
    button_start = joystick.get_button(7) # 9
    button_xbox = joystick.get_button(8) # 10
    button_lstick = joystick.get_button(9) # 11
    button_rstick = joystick.get_button(10) # 12
    leftBumper = joystick.get_button(4) # 13
    rightBumper = joystick.get_button(5) # 14
    r_axis_x = joystick.get_axis(3) # 15
    r_axis_y = joystick.get_axis(4) # 16
    d_pad_up = joystick.get_hat(0)[1] == 1 # 17
    d_pad_down = joystick.get_hat(0)[1] == -1 # 18
    d_pad_left = joystick.get_hat(0)[0] == -1 # 19
    d_pad_right = joystick.get_hat(0)[0] == 1 # 20


    # Convert input values to bytes
    data = bytearray()
    data.append(int(l_axis_x * 127 + 127)) # 0
    data.append(int(l_axis_y * -127 + 127)) # 1
    data.append(int(r_axis_x * 127 + 127)) # 2
    data.append(int(r_axis_y * -127 + 127)) # 3
    data.append(int(leftTrigger * 127 + 127)) # 4
    data.append(int(rightTrigger * 127 + 127)) # 5
    data.append(button_a) # 6
    data.append(button_b) # 7
    data.append(button_x) # 8
    data.append(button_y) # 9
    data.append(leftBumper) # 10
    data.append(rightBumper) # 11
    data.append(button_back) # 12
    data.append(button_xbox) # 13
    data.append(button_start) # 14
    data.append(button_lstick) # 15
    data.append(button_rstick) # 16
    data.append(d_pad_up) # 17
    data.append(d_pad_down) # 18
    data.append(d_pad_left) # 19
    data.append(d_pad_right) # 20


    # Send data over TCP socket
    sock.sendall(data)
    time.sleep(0.05)
