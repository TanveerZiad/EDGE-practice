"""
Command-line interface handling for the Weather CLI App.
"""

def parse_args(args):
    """
    Parse command-line arguments.
    
    Args:
        args: List of command-line arguments
        
    Returns:
        dict: Dictionary containing parsed arguments
    """
    parsed_args = {}
    
    if not args or '-h' in args or '--help' in args:
        parsed_args['help'] = True
        return parsed_args
    
    # Simple parsing: assume first argument is the location
    if args:
        parsed_args['location'] = ' '.join(args)
    
    return parsed_args

def display_help():
    """Display help information."""
    print("""
Weather CLI App
--------------
A simple command-line application to get current weather information.

Usage:
  python main.py [location]
  
Options:
  -h, --help    Show this help message and exit
  
Examples:
  python main.py "New York"
  python main.py Tokyo
  python main.py "San Francisco, CA"
    """)