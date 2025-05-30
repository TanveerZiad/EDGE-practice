#!/usr/bin/env python3
"""
Simple Weather CLI App
A command-line application that displays weather information for a given location.
"""

import sys
from cli import parse_args, display_help
from weather_api import fetch_weather
from formatter import format_weather_data

def main():
    """Main entry point of the application."""
    args = parse_args(sys.argv[1:])
    
    if args.get('help'):
        display_help()
        return
    
    location = args.get('location')
    if not location:
        print("Error: Please provide a location.")
        display_help()
        return
    
    try:
        weather_data = fetch_weather(location)
        if weather_data:
            formatted_output = format_weather_data(weather_data)
            print(formatted_output)
        else:
            print(f"Error: Could not retrieve weather data for '{location}'.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()