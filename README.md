AirDraw AI

Draw in the air using your hand. Convert motion into digital sketches in real time.

Overview

AirDraw AI is a computer vision system that transforms hand gestures into digital drawing input using a standard webcam.

It tracks the index finger and converts movement into continuous strokes on a virtual canvas.

The system is designed as the foundation for gesture-based creative interfaces and future AI-driven sketch-to-object generation.

Core Capabilities
Real-time hand tracking using webcam
Index finger-based drawing control
Open palm gesture to stop drawing
Smooth stroke rendering with noise reduction
Continuous canvas drawing system
Compatible with DroidCam or standard webcam input
How It Works

The system follows a simple interaction model:

Index finger raised → drawing enabled
Open palm detected → drawing disabled
Finger movement → stroke generation on canvas

Each stroke is captured as a sequence of points and rendered in real time.

Technology Stack
Python
OpenCV
MediaPipe
NumPy
Setup Instructions

Clone the repository:

git clone https://github.com/your-username/airdraw-ai.git
cd airdraw-ai

Install dependencies:

pip install opencv-python mediapipe numpy

Run the application:

python main.py
Camera Configuration

The application supports:

Built-in webcam
External webcam
DroidCam (mobile camera over IP or USB)

If the video feed does not appear, update the camera index in the code (0 or 1).

Controls
Input	Behavior
Index finger up	Enable drawing
Open palm	Disable drawing
C key	Clear canvas
Q key	Exit application
Current Limitations
Freehand strokes are not perfectly smooth due to natural hand jitter
No semantic recognition of shapes or letters yet
Performance depends on lighting and camera quality
Future Development
Gesture-based command system
Shape recognition and correction
Letter and symbol recognition
Sketch-to-3D object generation
Virtual camera integration for Zoom and Teams
Purpose

This project explores the intersection of:

Computer vision
Human-computer interaction
Gesture-based interfaces
AI-assisted creativity

The goal is to eliminate traditional input devices and enable natural interaction through motion.

Status

Experimental prototype stage.
