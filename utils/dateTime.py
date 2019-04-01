from datetime import datetime, timedelta

print(result)

def returnTime():
    currentUtcTime = datetime.utcnow()
    result = currentUtcTime + timedelta(hours=11)
    
    return result