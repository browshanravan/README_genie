# Forecast Engine

An interactive Streamlit application for univariate time-series forecasting using Facebook’s Prophet library. Upload your CSV, validate date formats and data granularity, visualize historical trends, specify seasonality and forecast horizons, and generate future forecasts with a single click.

---

## Table of Contents

- [About This Project](#about-this-project)  
- [Features](#features)  
- [Project Description](#project-description)  
- [Getting Started](#getting-started)  
  - [Prerequisites](#prerequisites)  
  - [Installation](#installation)  
  - [Running the App](#running-the-app)  
  - [Using a Dev Container](#using-a-dev-container)  
- [Usage](#usage)  
- [Configuration](#configuration)  
- [File Structure](#file-structure)  
- [Contributing](#contributing)  
- [License](#license)

---

## About This Project

Forecast Engine demonstrates how to build a minimal, interactive time-series forecasting web application with:

- **Prophet** for model fitting and seasonality handling  
- **Streamlit** for UI and rapid prototyping  
- **Altair**, **Matplotlib**, and **Plotly** for visualizations  

---

## Features

- Upload a CSV file with date (`DD-MM-YYYY`) and target columns.  
- Validate date format and enforce data granularity (daily/weekly/monthly/yearly).  
- Interactive historical data plotting.  
- Specify the length of a full seasonality cycle (in days/weeks/months/years).  
- Choose a future forecasting horizon.  
- Generate and visualize model forecasts with confidence intervals.  

---

## Project Description

Forecast Engine is designed for data scientists, analysts, and hobbyists who need a quick, illustrative tool to:

1. **Inspect** uploaded time-series data for formatting and completeness.  
2. **Resample** data to uniform intervals and identify missing periods.  
3. **Visualize** historical trends and seasonality interactively.  
4. **Configure** and **fit** a Prophet model with custom seasonal components.  
5. **Forecast** future values for any specified horizon with auto-plotted results.  

It can be extended to include additional regressors, multiple seasonalities, or alternative forecasting backends.

---

## Getting Started

### Prerequisites

- Python 3.10+  
- Git (optional, to clone the repo)  

### Installation

1. Clone this repository (or download the ZIP):

   ```bash
   git clone https://github.com/your-username/forecast_engine.git
   cd forecast_engine
   ```

2. Create and activate a virtual environment (recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install Python dependencies:

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

### Running the App

The simplest way to launch Forecast Engine:

```bash
sh app.sh
```

This will install any missing dependencies and start the Streamlit server on port 8501.  
Then open your browser at `http://localhost:8501`.

Alternatively, run manually:

```bash
streamlit run main.py --server.port 8501
```

### Using a Dev Container

This project includes a VS Code Dev Container configuration:

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop) and the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).  
2. In VS Code, open the repository and choose **Reopen in Container**.  
3. Once built, dependencies (Python 3.10 + tools) are pre-installed.  
4. Run the app:

   ```bash
   streamlit run main.py
   ```

---

## Usage

1. **Upload** your CSV file via the file uploader.  
2. **Select** the date column (must be in `DD-MM-YYYY` format).  
3. **Select** the target/value column to forecast.  
4. **Choose** data granularity (daily/weekly/monthly/yearly).  
5. **Generate** the historical data plot.  
6. **Specify**:
   - Number of smallest units per full seasonal cycle (e.g., 12 months for annual seasonality).  
   - Forecast horizon in the same units.  
7. **Generate** the future forecast plot.  

All steps feature on-the-fly validation; incorrect formats or missing intervals will prompt actionable feedback.

---

## Configuration

- `.streamlit/config.toml`: Streamlit UI theming, upload size, and error-detail settings.  
- `app.sh`: Convenience script to install dependencies and launch the app.  
- Dev Container files (`.devcontainer/`): Dockerfile and config for an isolated development environment.

---

## File Structure

```
.
├── .devcontainer/            # VS Code dev container setup
│   ├── Dockerfile
│   └── devcontainer.json
├── .streamlit/               # Streamlit configuration
│   └── config.toml
├── forecast_engine/          # Source package
│   └── src/
│       └── utils.py          # CSV reader, validators, model-fitting
├── app.sh                    # Shell script to install & run
├── LICENSE                   # MIT License
├── main.py                   # Streamlit app entry point
└── requirements.txt          # Python dependencies
```

---

## Contributing

Contributions are welcome! Please fork the repo, create a feature branch, and submit a pull request.  
For bug reports or feature requests, open an issue on GitHub.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.