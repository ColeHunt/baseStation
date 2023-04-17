# CySAR - baseStation

## Description
The baseStation is the FrontEnd application that allows communication with CARL the CySAR robot. The baseStation caputes controller inputs and other user interface devices and send them to the robot to control accordingly. The robot will also send data, back such as encoder positions and camera feeds to assit the driver in opperation.

## Connecting to the Robot
In order to control the robot using the baseStation there a few setup steps need
1. Ensure CARL and the baseStation computer are connected to the same network.
    - This can be either a wireless of physical network.
2. Ensure there is a controller plugged into the baseStation computer
    - Most common controller types are accepted *(Tested: DS4, Xbox 360)*
3. Ensure that the robot `teleop.py` program has been started on the robot
    - See [CARL](https://github.com/M2I-CYSAR/carl#readme) for further details

**WARNING: Once the next step is run the robot will attempt to react to Joystick inputs. Do not continue if this not desired**

4. Run the `operatorInterface.py` script on the baseStation