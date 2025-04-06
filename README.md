# Power_monitoring_system
* Power monitor system ,using STM 32 wb with the monitoring and the estimate levels.
* It also has a local ML model written in C , that predicts the consumption.
![image](https://github.com/user-attachments/assets/3bbf5f9d-a40b-4ef4-a811-a12806682e57)
Current sensor connected to pin AO -> ADC1 IN1
Voltage sensor connected to pin A1 --> ADC1 IN2

# Setup:
![1743954292348](https://github.com/user-attachments/assets/5e0cbd79-a1f6-4c72-9d6b-ae4d34b7799d)
* A variac is used for transforming the input AC value to a stepped down value with quantization at 2 4 6 8 10 12.
* Output dc voltage --> tested with multimeter.
1. Stm32 nucleo
2. dht 11 for moisture levels
3. voltage sensor and current sensor
4. A custom voltage source (VCC) generated from scratch (as a store bought one is very expensive)
   ( Ill add the assemby for the source as well ;) )
5. Multimeter
6. LCD display
7. Raspberry pi 4B (optional)
 *  Final set up of the components connected:
   ![1743954292330](https://github.com/user-attachments/assets/03ee648e-27ff-4ee0-aaad-58514c441d54)

## Serial Output:
![image width=50%](https://github.com/user-attachments/assets/dff2e7af-2b8a-4a9a-91bd-becc1ddfc7e2)

## Issues,Todo:
1. Output of the Voltage source --> Takes rounded values.
2. Should set up lcd
3. direct connection to cloud (must be set up) -->Used esp01 for connection to cloud (thinkspeak) using AT commands and it's not working for now.
   
# MQTT client in STM32 :
1. https://medium.com/@alirezabeigimech/mqtt-and-lwip-on-stm32-1-tcp-client-75d67e67ab65
2. https://medium.com/@alirezabeigimech/sudo-nano-etc-mosquitto-mosquitto-conf-6dfbb0045779
3. https://www.youtube.com/watch?v=uBc6TSgYrW4
4. https://community.st.com/t5/stm32-mcus-products/implementing-mqtt-in-stm32f407g/td-p/703538
5. https://community.st.com/t5/stm32-mcus-products/stm32-mqtt-support/td-p/335451
6. https://community.st.com/t5/stm32-mcus-products/mqtt-using-stm32l0/m-p/394298
7. https://www.openstm32.org/forumthread8465
8. https://docs.wiznet.io/Product/iEthernet/W5500/overview

# and ...
I took wayy more time than what I had promised due to un forseen conditions



