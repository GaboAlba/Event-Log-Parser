# event.System.EventRecordID
from winevt import EventLog
query = EventLog.Query("System","Event/System[Level<=1]")
for event in query :
    #print(event.xml)
    print(event.System.TimeCreated['SystemTime'] + ',' + event.System.Provider['Name'] + ',' + event.System.EventRecordID.cdata)