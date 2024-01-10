#ifndef CONNECT_APRIL_H
#define CONNECT_APRIL_H

#include <jansson.h>

json_t* recv_request(void);
void send_response(json_t* response);

#endif // CONNECT_APRIL_H

