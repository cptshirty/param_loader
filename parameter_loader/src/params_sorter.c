
// Generated with praram_loader on 2024-08-14


#include "params_sorter.h"


// this function is used to assign string to a parameter and then write its value to the parameter

uint8_t sort_param(char *buffer)
{
    retval = 0;
    char* var = 0;    
    char* val = 0;    
    var = strtok(buffer," "); // get the param name
    val = strtok(NULL," "); // get the value of the param
if(strcmp(var,"BLINK_DELAY")==0)    {
    retval = 1;
    PARAM_BLINK_DELAY = atoi(val);
    
    }
else if(strcmp(var,"BUZZER_TONE")==0)    {
    retval = 1;
    PARAM_BUZZER_TONE = atoi(val);
    
    }
else    {
    
    }
    


}
