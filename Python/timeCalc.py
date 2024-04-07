#Convert milliseconds in time

inputTimeInMs = int(input("Put the time in milliseconds: "))

hours = (inputTimeInMs // 1000) // (60 * 60)
minutes = ((inputTimeInMs // 1000) - hours * 60 * 60) // 60
seconds = (inputTimeInMs // 1000) - hours * 60 * 60 - minutes * 60
milliseconds = inputTimeInMs - ((hours * 3600000) + (minutes * 60000) + (seconds * 1000))
outputTime = f"Time in milliseconds:{inputTimeInMs}, Hours:{hours}, Minutes:{minutes}, Seconds:{seconds}, Milliseconds:{milliseconds}."

print(outputTime)