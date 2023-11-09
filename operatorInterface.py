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
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((TCP_IP, TCP_PORT))

# Loop to continuously send Xbox controller data
while True:
    pygame.event.pump()

    # Get controller input values
    l_axis_x = joystick.get_axis(0) #0
    l_axis_y = joystick.get_axis(1) #1
    r_axis_x = joystick.get_axis(3) #2
    r_axis_y = joystick.get_axis(4) #3
    button_a = joystick.get_button(0) #4
    button_b = joystick.get_button(1) #5
    button_x = joystick.get_button(2) #6
    button_y = joystick.get_button(3) #7
    button_start = joystick.get_button(7) #8
    leftBumper = joystick.get_button(4) #9
    rightBumper = joystick.get_button(5) #10
    leftTrigger = joystick.get_axis(2) #11
    rightTrigger = joystick.get_axis(5) #12
    # TODO: Add input values
    leftTrigger_down = joystick.get_button() #13
    rightTrigger_down = joystick.get_button() #14
    button_back = joystick.get_button() #15
    button_xbox = joystick.get_button() #16
    d_pad_x = joystick.get_hat() #17
    d_pad_y = joystick.get_hat() #18

    # Convert input values to bytes
    data = bytearray()
    data.append(int(l_axis_x * 127 + 127)) #0
    data.append(int(l_axis_y * 127 + 127)) #1
    data.append(int(r_axis_x * 127 + 127)) #2
    data.append(int(r_axis_y * 127 + 127)) #3
    data.append(button_a) #4
    data.append(button_b) #5
    data.append(button_x) #6
    data.append(button_y) #7
    data.append(button_start) #8
    data.append(leftBumper) #9
    data.append(rightBumper) #10
    data.append(int(leftTrigger * 127 + 127)) #11
    data.append(int(rightTrigger * 127 + 127)) #12
    # TODO: Add additional controller inputs

    # Send data over TCP socket
    sock.sendall(data)
    time.sleep(0.05)
