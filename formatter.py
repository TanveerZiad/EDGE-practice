"""
Formatting utilities for displaying weather data.
"""

def format_weather_data(weather_data):
    """
    Format weather data for display.
    
    Args:
        weather_data: Dictionary containing weather information
        
    Returns:
        str: Formatted weather information
    """
    location_info = weather_data.get('location', {})
    current_info = weather_data.get('current', {})
    
    location_name = location_info.get('name', 'Unknown Location')
    country = location_info.get('country', '')
    local_time = location_info.get('localtime', '')
    
    temperature_c = current_info.get('temp_c', 'N/A')
    temperature_f = current_info.get('temp_f', 'N/A')
    condition = current_info.get('condition', {}).get('text', 'Unknown')
    humidity = current_info.get('humidity', 'N/A')
    wind_speed = current_info.get('wind_kph', 'N/A')
    wind_direction = current_info.get('wind_dir', '')
    feels_like_c = current_info.get('feelslike_c', 'N/A')
    feels_like_f = current_info.get('feelslike_f', 'N/A')
    uv_index = current_info.get('uv', 'N/A')
    
    # Build the formatted output
    separator = "-" * 40
    
    formatted_output = f"""
{separator}
Weather for {location_name}, {country}
{separator}
Local Time: {local_time}
Condition: {condition}

Temperature: {temperature_c}°C ({temperature_f}°F)
Feels Like: {feels_like_c}°C ({feels_like_f}°F)
Humidity: {humidity}%
Wind: {wind_speed:.1f} km/h {wind_direction}
UV Index: {uv_index:.1f}
{separator}
"""
    
    return formatted_output