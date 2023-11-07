import sys
from Interfaces import Interface
import msvcrt

# Changing console encoding 
desired_encoding = 'utf-8'
sys.stdout.reconfigure(encoding=desired_encoding)
sys.stdin.reconfigure(encoding=desired_encoding)
sys.stderr.reconfigure(encoding=desired_encoding)

Interface.start()