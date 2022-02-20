import os
import sys

# Setup paths so that our system can import directly from source
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(1, '../')
sys.path.insert(1, '../sample/')