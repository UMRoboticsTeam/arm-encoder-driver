#ifndef ENCODER_INTERFACE
#define ENCODER_INTERFACE

#include <cstring>
#include <iostream> 
#include "./SerialCAN/Includes/SerialCAN.h"

static CSerialCAN mySerialCAN = CSerialCAN(); 

class Interface{
private: 
	CANAPI_OpMode_t opmode = {}; 
	CANAPI_Bitrate_t bitrate = {};  
	CANAPI_Return_t ret_val= 0; 
	CANAPI_Message_t message; 
	char serial_port[32]; 
	static volatile int exception_flag;
public: 
	Interface(uint32_t baudrate_param = CANBTR_INDEX_250K , uint32_t opmode_param = CANMODE_DEFAULT, const char* serial_port_param = "/dev/ttyS3");
	CANAPI_Return_t initialize_channel(); 
	void begin_read_loop(const char type ='e', int timeout = 0); // e-all messages (default), a-angles only, t-temperature only
	CANAPI_Return_t teardown_channel(); 
	void static signal_handler(int signal); 
}; 



#endif