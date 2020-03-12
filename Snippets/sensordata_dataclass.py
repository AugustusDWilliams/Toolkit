from dataclasses import dataclass

@dataclass
class SensorData:
    sensor_class = "usb"
    comport_dict = dict()
    comport = ""
    sn = ""
    gas_id = ""
    sensor_type = ""
    msg_ids = ['sn', "gas_id", "sensor_type", "decimal",
    "low_alarm", "high_alarm", "pos_peak", "neg_peak",
    "zero_offset_high", "zero_offset_low", "span_low_limit", "span_high_limit", "zero_value2", "adc_zero", "neg_limit", "fw_version", "hw_version", "life_counter"]

    def reset(self):
        self.comport_dict = dict()
        self.comport = ""
        self.sn = ""
        self.gas_id = ""
        self.sensor_type = ""
