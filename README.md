# AirSketch AI

Draw in the air using your hand. Convert motion into real-time digital sketches using computer vision.

---

## Overview

AirSketch AI is a real-time computer vision system that transforms hand gestures into digital drawing input using a standard webcam.

It tracks the index finger and converts movement into continuous strokes on a virtual canvas.

This project is designed as a foundation for gesture-based interaction systems and future AI-driven sketch-to-object generation.

---

## Features

Real-time hand tracking using webcam
Index finger-based drawing control
Open palm gesture to stop drawing
Smooth stroke rendering with noise reduction
Continuous canvas drawing system
Supports webcam and DroidCam input

---

## How It Works

The system uses a simple interaction model:

Index finger up enables drawing
Open palm disables drawing
Finger movement generates stroke points

Each movement is captured as coordinates and rendered on a canvas in real time.

---

## Tech Stack

Python
OpenCV
MediaPipe
NumPy

---

## Installation

Clone the repository:

```bash id="clone1"
git clone https://github.com/your-username/airsketch-ai.git
cd airsketch-ai
```

Install dependencies:

```bash id="install1"
pip install opencv-python mediapipe numpy
```

---

## Run the Project

```bash id="run1"
python main.py
```

---

## Camera Setup

Supported inputs:

Built-in webcam
External webcam
DroidCam (mobile as webcam)

If video does not appear, change camera index in code:

0 or 1 depending on your system

---

## Controls

Index finger up → Start drawing
Open palm → Stop drawing
C key → Clear canvas
Q key → Quit application

---

## Limitations

Freehand drawing is affected by natural hand movement noise
No shape or letter recognition yet
Performance depends on lighting and camera stability

---

## Future Scope

Gesture-based command system
Shape recognition and auto correction
Alphabet and symbol recognition
Sketch to 3D object generation
Zoom and Teams virtual camera integration

---

## Purpose

This project explores:

Computer vision based interaction
Gesture-driven user interfaces
AI-assisted creative systems

The goal is to replace traditional input devices with natural hand movement interaction.

---

## Status

Experimental prototype stage.

