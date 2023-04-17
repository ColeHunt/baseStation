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
    axis_x = joystick.get_axis(0)
    axis_y = joystick.get_axis(1)
    button_a = joystick.get_button(0)
    button_b = joystick.get_button(1)

    # Convert input values to bytes
    data = bytearray()
    data.append(int(axis_x * 127 + 127))
    data.append(int(axis_y * 127 + 127))
    data.append(button_a)
    data.append(button_b)

    # Send data over TCP socket
    sock.sendall(data)
    time.sleep(0.05)
