# Deep Learning Computer Vision Pipeline

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.1-EE4C2C.svg)](https://pytorch.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109-009688.svg)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A **production-grade computer vision pipeline** for real-time image and video processing. Powered by PyTorch and FastAPI, this repository provides a high-performance interface for object detection, image classification, and segmentation.

## 🚀 Features

- **Real-time Inference**: Optimized inference loop for low-latency processing.
- **Object Detection**: Support for pre-trained models (Faster R-CNN, SSD) and custom model integration.
- **RESTful API**: Easy-to-use endpoints for uploading images and receiving structured results.
- **Batch Processing**: Efficiently handle multiple images in a single request.
- **Metrics & Logging**: Integrated monitoring for inference performance and model health.
- **Containerized**: Production-ready Docker environment for seamless deployment.

## 📁 Project Structure

```
deep-learning-computer-vision-pipeline/
├── app/
│   ├── api/          # API route handlers
│   ├── core/         # Config and logging
│   ├── models/       # PyTorch model definitions and wrappers
│   └── services/     # Inference and image processing logic
├── tests/            # Unit and functional tests
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## 🛠️ Quick Start

```bash
# Clone
git clone https://github.com/Shivay00001/deep-learning-computer-vision-pipeline.git

# Install
pip install -r requirements.txt

# Run
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## 📄 License

MIT License
