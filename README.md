# Swerve-concept

## process
 - Roborio starts with the inital values on start, along with the xbox values
 - sends the values to the motor
 - the encoders and sensors give the motor controllers nesc. values
 - The motor controllers (All at the same time, parallel), do the swerve math, (look at `swerveMath.py`*, also [article](https://www.freshconsulting.com/insights/blog/how-to-build-a-swerve-drive-robot/#:~:text=Swerve%2Ddrive%20is%20an%20omnidirectional,Ackermann%20steering%20or%20differential%20drive.))
 - move all the motors
 - Roborio constantly broadcasts Xbox values, motors move

**Imp. Note**: The motors don't need to complete a movement to do the next movement, they move whenever they recieve an xbox value

<br>

red(Rio) Orange(Motor Controller)

![Screen Shot 2024-01-27 at 10 44 06 AM](https://github.com/CAPS-Robotics/Swerve-concept/assets/71975550/9cc2d907-8ca7-4037-8dd7-bb406d848ebf)

* - `swerveMath.py` contains raw equations, Wpilib/Rev has abstractions
