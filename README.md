# Weather CLI App

A simple command-line application to get current weather information for any location.

## Features

- Get current weather information for any location
- View temperature, conditions, humidity, wind speed, and more
- Clean, easy-to-read output format

## Usage

Run the application using:

```bash
python main.py [location]
```

Examples:

```bash
python main.py "New York"
python main.py Tokyo
python main.py "San Francisco, CA"
```

To display help:

```bash
python main.py --help
```

## Project Structure

- `main.py`: Entry point of the application
- `cli.py`: Command-line interface handling
- `weather_api.py`: Weather API interaction (mock implementation)
- `formatter.py`: Formatting utilities for displaying weather data

## Note

This application currently uses mock data. In a real-world scenario, you would integrate with a weather API service.