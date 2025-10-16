# SVD Applications in Computer Vision and LIDAR Data Analysis

A comprehensive university project demonstrating practical applications of Singular Value Decomposition (SVD) and pseudo-inverse (Moore-Penrose inverse) in image compression and 3D LIDAR point cloud analysis.

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Dataset](#dataset)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Results](#results)
- [Technologies](#technologies)
- [Mathematical Background](#mathematical-background)

## 🎯 Overview

This project explores two main applications of linear algebra concepts:

1. **Image Compression with SVD**: Demonstrates how Singular Value Decomposition can be used to compress images while maintaining visual quality. The project analyzes the trade-off between compression ratio and image quality.

2. **LIDAR Point Cloud Analysis**: Applies the Moore-Penrose pseudo-inverse to fit ground planes in 3D LIDAR point cloud data from the Toronto 3D dataset, with statistical analysis of approximation quality.

## ✨ Features

### SVD-Based Image Compression
- Decomposition of grayscale images using SVD
- Reconstruction with varying ranks (r = 10, 30, 150)
- Visualization of singular values decay
- Cumulative energy analysis
- Compression ratio vs. quality trade-off analysis

### LIDAR Data Processing
- 3D visualization of point cloud data (215,672 points)
- Multi-class segmentation (9 categories):
  - Unclassified
  - Ground
  - Road markings
  - Natural
  - Building
  - Utility line
  - Pole
  - Car
  - Fence
- Ground plane approximation using pseudo-inverse
- Mesh-based surface reconstruction with density filtering
- Statistical analysis:
  - RMSE and MAE calculation
  - Residual distribution analysis
  - Outlier detection (>3σ threshold)
  - Kernel Density Estimation (KDE) visualization

### Geometric Visualization
- Step-by-step visualization of SVD geometric transformations
- Demonstration of rotation and scaling operations
- Basis vector transformations

## 🚀 Installation

### Prerequisites
- Python 3.11+
- pip or conda package manager

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd pinv-seminarski
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Key Dependencies
- **numpy**: Linear algebra operations
- **matplotlib**: 2D plotting and visualization
- **open3d**: 3D point cloud processing
- **pandas**: Data manipulation and analysis
- **scipy**: Scientific computing and statistics
- **scikit-learn**: Machine learning utilities
- **seaborn**: Statistical data visualization
- **plotly**: Interactive 3D visualizations
- **pillow**: Image processing

## 📊 Dataset

### LIDAR Data
The project uses the **Toronto 3D** dataset:
- **Source**: Point cloud LIDAR data from Toronto
- **Format**: CSV file with 215,672 points
- **Features**: 
  - 3D coordinates (x, y, z)
  - RGB color information
  - Intensity values
  - GPS timestamps
  - Scan angle
  - Classification labels

### Image Data
- Sample image (`dog.jpeg`) for SVD compression demonstration
- Can be replaced with any grayscale image

## 💻 Usage

### Running the Main Analysis

1. **LIDAR Point Cloud Analysis**:
   - Open `pinv_lidar.ipynb` in Jupyter Notebook or JupyterLab
   - Run cells sequentially to:
     - Load and explore LIDAR data
     - Visualize 3D point clouds
     - Perform ground plane approximation
     - Analyze statistical properties

2. **SVD Image Compression**:
```bash
python svd-compression.py
```
   - Processes the input image
   - Generates reconstructions at different ranks
   - Saves visualization results

3. **SVD Geometry Visualization**:
```bash
python svd_geometry.py
```
   - Creates geometric transformation visualizations
   - Shows step-by-step SVD operations

### Customization

#### Changing Compression Ranks
In `svd-compression.py`, modify:
```python
r_vals = [10, 30, 150]  # Change these values
```

#### Adjusting Ground Plane Parameters
In `pinv_lidar.ipynb`, modify:
```python
threshold = np.percentile(density[density > 0], 15)  # Adjust percentile
```

## 📁 Project Structure

```
pinv-seminarski/
├── data/
│   ├── dog.jpeg                        # Sample image for SVD compression
│   └── LIDAR data/
│       ├── lidar_data.csv              # Toronto 3D point cloud data
│       ├── Colors.xml                  # Color mapping for labels
│       └── Mavericks_classes_9.txt     # Class definitions
├── experiments/
│   └── experiments.ipynb               # Additional experiments
├── results/                            # Generated visualizations
│   ├── 3d_cloud.png                    # RGB point cloud
│   ├── 3d_cloud_labeled.png            # Classified point cloud
│   ├── ground_approx.png               # Ground plane approximation
│   ├── ground_approx_mesh.png          # Mesh-based approximation
│   ├── histogram.png                   # Residual histogram
│   ├── kde.png                         # Kernel density estimation
│   ├── image_recons.png                # Image reconstructions
│   ├── sigma_v_r.png                   # Singular values plot
│   ├── cum_sum.png                     # Cumulative energy plot
│   └── svd_geometry.png                # Geometric transformations
├── utils/
│   └── unzipper.py                     # Utility for extracting data
├── pinv_lidar.ipynb                    # Main LIDAR analysis notebook
├── svd-compression.py                  # Image compression script
├── svd_geometry.py                     # Geometric visualization script
├── requirements.txt                    # Python dependencies
└── README.md                           # This file
```

## 📈 Results

### Image Compression Results
- **Rank 10**: ~98% compression, visible quality loss
- **Rank 30**: ~94% compression, good quality retention
- **Rank 150**: ~70% compression, near-perfect quality

### Ground Plane Approximation Results
- **RMSE**: 0.1162 meters
- **MAE**: 0.0771 meters
- **Outliers**: 1.11% (>3σ threshold)
- **Mean Residual**: ~0.0000 meters (unbiased estimator)
- **Standard Deviation**: 0.1162 meters

These results demonstrate high accuracy in ground plane approximation using the pseudo-inverse method.

## 🛠 Technologies

- **Python 3.11**: Main programming language
- **NumPy**: Numerical computing and linear algebra
- **Matplotlib**: Static visualizations
- **Open3D**: 3D point cloud processing and visualization
- **Pandas**: Data manipulation
- **SciPy**: Statistical analysis
- **Seaborn**: Statistical plotting
- **Plotly**: Interactive 3D visualizations
- **scikit-learn**: Machine learning utilities

## 📐 Mathematical Background

### Singular Value Decomposition (SVD)
For any matrix **A** ∈ ℝ^(m×n), there exists a decomposition:

**A** = **U Σ V**^T

where:
- **U** ∈ ℝ^(m×m): Left singular vectors (orthogonal)
- **Σ** ∈ ℝ^(m×n): Diagonal matrix of singular values
- **V**^T ∈ ℝ^(n×n): Right singular vectors (orthogonal)

### Moore-Penrose Pseudo-Inverse
For an overdetermined system **Ax** = **b**, the least-squares solution is:

**x** = **A**^+ **b**

where **A**^+ = (**A**^T **A**)^(-1) **A**^T is the pseudo-inverse.

This minimizes the residual ||**Ax** - **b**||₂.

### Ground Plane Fitting
The ground plane is modeled as:

z = ax + by + c

Using pseudo-inverse, we solve:
```
[x₁ y₁ 1]   [a  ]   [z₁]
[x₂ y₂ 1] × [b  ] = [z₂]
[... ... ]  [c  ]   [...]
[xₙ yₙ 1]           [zₙ]
```

## 📝 Notes

- All visualizations include Serbian (Cyrillic) labels as per project requirements
- The project demonstrates practical applications of linear algebra in computer vision
- Results are reproducible by following the installation and usage instructions

## 🎓 Academic Context

This project was developed as a seminar work for a university course on numerical analysis and linear algebra. It demonstrates the practical applications of theoretical concepts in real-world scenarios.

## 📄 License

This project is intended for educational purposes.

---

**Author**: University Project  
**Date**: October 2025

