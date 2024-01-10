#ifndef CONNECT_APRIL_H
#define CONNECT_APRIL_H

#include <nlohmann/json.hpp>

class April {
public:
    static nlohmann::json recv_request();
    static void send_response(const nlohmann::json& response);
};

#endif // CONNECT_APRIL_H

