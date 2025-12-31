import base64
import uuid
from pathlib import Path

def generate_short_id6():
    uid = uuid.uuid4()
    
    uid_bytes = uid.bytes 
    
    b64 = base64.b64encode(uid_bytes).decode('utf-8')
    
    return b64.replace('=', '').replace('/', 'B').replace('+', 'A')[:6] 
