# biomechanical-goniometry-cv

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](#)
[![Computer Vision](https://img.shields.io/badge/CV-MediaPipe%20%7C%20OpenCV-teal.svg)](#)

Clinical-grade planar-projected joint angle and angular velocity tracking engine using on-device computer vision.

```mermaid
graph LR
    A[RGB Video Frame] --> B[33-Point Skeletal Keypoints]
    B --> C[Anatomical Plane Projection]
    C --> D[GoniometerSolver Vector Angle]
    D --> E[RepCounterFSM & Form Anomaly]
```

## Features

- **Planar Projection Goniometry**: Projects 3D keypoints onto Sagittal and Coronal anatomical planes to prevent foreshortening errors.
- **Micro-Jitter Landmark Filter**: Exponential moving average and velocity dampening.
- **Repetition State Machine**: Real-time rep validation and eccentric/concentric phase segmentation.

## License

MIT License (c) 2024-2026 Gaurav Bhardwaj / OmegaGaze Lab.
