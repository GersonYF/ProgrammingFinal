import utime
import sys
from MQ135 import MQ135

now_time = utime.time()
filename = f"mq_sensor_log-{now_time}.csv"

# Create header row in new CSV file
csv = open(filename, 'w')
csv.write("Timestamp,Raw_value_MQ135,ACETON,TOLUENO,ALCOHOL,CO2,NH4,CO\n")
csv.close

try:
    print("Press CTRL+C to abort.\n")
    
    mq135 = MQ135()

    while True:
        perc135 = mq135.MQPercentage()
        
        print("Medición MQ1350")
        print(
            f"""
                Raw Value: {perc135["RAW_VALUE"]}
                Acetona: {perc135["ACETON"]} ppm
                Tolueno: {perc135["TOLUENO"]} ppm
                Alcohol: {perc135["ALCOHOL"]} ppm
                CO2:	 {perc135["CO2"]} ppm
                NH4:	 {perc135["NH4"]} ppm
                CO:		 {perc135["CO"]} ppm
            """
        )
        
        # Write values to csv file
        timestamp = str(utime.time())
        entry = f"{timestamp}, {perc135['RAW_VALUE']}, {perc135['ACETON']}, {perc135['TOLUENO']}, {perc135['ALCOHOL']}, {perc135['CO2']}, {perc135['NH4']}, {perc135['CO']}\n"

        # Log (append) entry into file
        csv = open(filename, 'a')
        try:
            csv.write(entry)
        finally:
            csv.close()
        
        
        utime.sleep(58)


# Reset by pressing CTRL + C
except KeyboardInterrupt:
    print("Medida detenida por el usuario")
    
    #print csv
    csv = open(filename, 'r')
    print(csv.read())
    csv.close()

except Exception as e:
    print(f"\nError generado: {e}")
