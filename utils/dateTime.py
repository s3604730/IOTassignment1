from datetime import datetime, timedelta

def returnTime():
    currentUtcTime = datetime.utcnow()
    result = currentUtcTime + timedelta(hours=11)
    
    return result

print(returnTime())