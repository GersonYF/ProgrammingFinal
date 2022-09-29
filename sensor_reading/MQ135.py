#########################################################################
# Code adapted from # https://github.com/tutRPi/Raspberry-Pi-Gas-Sensor-MQ
#########################################################################

from machine import ADC
import utime
import math

class MQ135:
    ######################### Hardware Related #########################
    MQ_PIN                       = 26        # define which analog input channel you are going to use (MCP3008)
    RL_VALUE                     = 5         # define the load resistance on the board, in kilo ohms
    RO_CLEAN_AIR_FACTOR          = 9.83      # RO_CLEAR_AIR_FACTOR=(Sensor resistance in clean air)/RO,
                                             # which is derived from the chart in datasheet
                                            
    ######################### Software Related #########################
    CALIBRATION_SAMPLE_TIMES     = 50        # define how many samples you are going to take in the calibration phase
    CALIBRATION_SAMPLE_INTERVAL  = 500       # define the time interval(in milisecond) between each samples in the
                                             # cablibration phase
    READ_SAMPLE_INTERVAL         = 50        # define the time interval(in milisecond) between each samples in
    READ_SAMPLE_TIMES            = 5         # define how many samples you are going to take in normal operation 
                                             # normal operation

    FACTOR_16 = 3.3/65535
                                            
    ######################### Application Related ######################
    GAS_ACETON                   = 0
    GAS_TOLUENO                  = 1
    GAS_ALCOHOL                  = 2
    GAS_CO2                      = 3
    GAS_NH4                      = 4
    GAS_CO                       = 5
    
    def __init__(self, Ro=10, analog_pin=26):
        self.Ro = Ro
        self.MQ_PIN = analog_pin
        
        self.ADC_value = ADC(self.MQ_PIN)
         
        self.ACETONCurve = [1.0,0.18,-0.32] # two points are taken from the curve. 
                                            # with these two points, a line is formed which is "approximately equivalent"
                                            # to the original curve. 
                                            # data format:{ x, y, slope}; point1: (lg10, 0.18), point2: (lg200, -0.24) 
        self.TOLUENOCurve = [1.0,0.2,-0.30] # two points are taken from the curve. 
                                            # with these two points, a line is formed which is "approximately equivalent" 
                                            # to the original curve.
                                            # data format:[ x, y, slope]; point1: (lg10, 0.2), point2: (lg200, -0.19)
        self.AlcoholCurve = [1.0,0.28,-0.32] # two points are taken from the curve. 
                                            # with these two points, a line is formed which is "approximately equivalent" 
                                            # to the original curve.
                                            # data format:[ x, y, slope]; point1: (lg10, 0.28), point2: (lg200, -0.14)
        self.CO2Curve = [1.0,0.38,-0.37]       # two points are taken from the curve. 
                                            # with these two points, a line is formed which is "approximately equivalent" 
                                            # to the original curve.
                                            # data format:[ x, y, slope]; point1: (lg10, 0.38), point2: (lg200, -0.10)
        self.NH4Curve = [1.0,0.42,-0.42]     # two points are taken from the curve. 
                                            # with these two points, a line is formed which is "approximately equivalent" 
                                            # to the original curve.
                                            # data format:[ x, y, slope]; point1: (lg10, 0.42), point2: (lg200, -0.12)
        self.COCurve = [1.0,0.45,-0.26]     # two points are taken from the curve. 
                                            # with these two points, a line is formed which is "approximately equivalent" 
                                            # to the original curve.
                                            # data format:[ x, y, slope]; point1: (lg10, 0.45), point2: (lg200,  0.11)
                                            
        print("Calibrando MQ-135...")
        self.Ro = self.MQ135_Calibration()
        print("Calibración de MQ-135 completa...")
        print("MQ-135 Ro=%f kohm" % self.Ro)
        print("\n")
     
    @property
    def adc_voltage_value(self):
        return self.ADC_value.read_u16() * self.FACTOR_16
         
    ######################### MQCalibration ####################################
    # Input:   mq_pin - analog channel
    # Output:  Ro of the sensor
    # Remarks: This function assumes that the sensor is in clean air. It use  
    #          MQResistanceCalculation to calculates the sensor resistance in clean air 
    #          and then divides it with RO_CLEAN_AIR_FACTOR. RO_CLEAN_AIR_FACTOR is about 
    #          3.6, which differs slightly between different sensors.
    ############################################################################ 
    def MQ135_Calibration(self):
        val = 0.0
        for i in range(self.CALIBRATION_SAMPLE_TIMES):          # take multiple samples
            val += self.MQResistanceCalculation(self.adc_voltage_value)
            utime.sleep(self.CALIBRATION_SAMPLE_INTERVAL/1000.0)
            
        val = val/self.CALIBRATION_SAMPLE_TIMES                 # calculate the average value
        val = val/self.RO_CLEAN_AIR_FACTOR                      # divided by RO_CLEAN_AIR_FACTOR yields the Ro 
                                                                # according to the chart in the datasheet 
        return val
    
    ######################### MQResistanceCalculation #########################
    # Input:   raw_adc - raw value read from adc, which represents the voltage
    # Output:  the calculated sensor resistance
    # Remarks: The sensor and the load resistor forms a voltage divider. Given the voltage
    #          across the load resistor and its resistance, the resistance of the sensor
    #          could be derived.
    ############################################################################ 
    def MQResistanceCalculation(self, raw_adc):
        
        if raw_adc == 0:
            raw_adc = 1
            
        return float(self.RL_VALUE * (65472.0-raw_adc) / float(raw_adc))
    
    #########################  MQRead ##########################################
    # Input:   mq_pin - analog channel
    # Output:  Rs of the sensor
    # Remarks: This function use MQResistanceCalculation to caculate the sensor resistenc (Rs).
    #          The Rs changes as the sensor is in the different consentration of the target
    #          gas. The sample times and the time interval between samples could be configured
    #          by changing the definition of the macros.
    ############################################################################ 
    def MQRead(self):
        rs = 0.0
        raw_value = 0.0
        for i in range(self.READ_SAMPLE_TIMES):
            raw_value += self.adc_voltage_value
            rs += self.MQResistanceCalculation(self.adc_voltage_value)
            utime.sleep(self.READ_SAMPLE_INTERVAL/1000.0)

        rs = rs / self.READ_SAMPLE_TIMES
        raw_value = raw_value / self.READ_SAMPLE_TIMES

        return rs, raw_value
    
    def MQPercentage(self):
        val = {}
        read, raw_value = self.MQRead()
        val["ACETON"]   = self.MQGetGasPercentage(read/self.Ro, self.GAS_ACETON)
        val["TOLUENO"]  = self.MQGetGasPercentage(read/self.Ro, self.GAS_TOLUENO)
        val["ALCOHOL"]  = self.MQGetGasPercentage(read/self.Ro, self.GAS_ALCOHOL)
        val["CO2"]      = self.MQGetGasPercentage(read/self.Ro, self.GAS_CO2)
        val["NH4"]      = self.MQGetGasPercentage(read/self.Ro, self.GAS_NH4)
        val["CO"]       = self.MQGetGasPercentage(read/self.Ro, self.GAS_CO)
        val["RAW_VALUE"]= raw_value
        return val
     
    #########################  MQGetGasPercentage ##############################
    # Input:   rs_ro_ratio - Rs divided by Ro
    #          gas_id      - target gas type
    # Output:  ppm of the target gas
    # Remarks: This function passes different curves to the MQGetPercentage function which 
    #          calculates the ppm (parts per million) of the target gas.
    ############################################################################ 
    def MQGetGasPercentage(self, rs_ro_ratio, gas_id):
        gas_calculations = {
            self.GAS_ACETON: self.MQGetPercentage(rs_ro_ratio, self.ACETONCurve),
            self.GAS_TOLUENO: self.MQGetPercentage(rs_ro_ratio, self.TOLUENOCurve),
            self.GAS_ALCOHOL: self.MQGetPercentage(rs_ro_ratio, self.AlcoholCurve),
            self.GAS_CO2	: self.MQGetPercentage(rs_ro_ratio, self.CO2Curve),
            self.GAS_NH4	: self.MQGetPercentage(rs_ro_ratio, self.NH4Curve),
            self.GAS_CO		: self.MQGetPercentage(rs_ro_ratio, self.COCurve)
        }
        
        return 0 if gas_id not in gas_calculations else gas_calculations[gas_id]
    
    #########################  MQGetPercentage #################################
    # Input:   rs_ro_ratio - Rs divided by Ro
    #          pcurve      - pointer to the curve of the target gas
    # Output:  ppm of the target gas
    # Remarks: By using the slope and a point of the line. The x(logarithmic value of ppm) 
    #          of the line could be derived if y(rs_ro_ratio) is provided. As it is a 
    #          logarithmic coordinate, power of 10 is used to convert the result to non-logarithmic 
    #          value.
    ############################################################################ 
    def MQGetPercentage(self, rs_ro_ratio, pcurve):
        # This is the natural natural logarithm -> log(rs_ro_ratio)
        return (math.pow(10,(((math.log(rs_ro_ratio)-pcurve[1])/ pcurve[2]) + pcurve[0])))
