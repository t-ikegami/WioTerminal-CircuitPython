from ..Struct import Struct 

# tcpip_adapter.get_ip_info
Struct.define("ip_info", """
uint8[4] ip;
uint8[4] netmask;
uint8[4] gw;
""", padding = 4)

# wifi.get_reconnect_data
Struct.define("fast_reconnect", """
char[36] psk_essid;
char[65] psk_passphrase;
char[40] wpa_global_PSK;
uint32 channel;
uint32 security_type;
uint32 offer_ip;
""", padding = 4)

# wifi.get_ap_info
Struct.define("rtw_bss_info", """
uint32 version;
uint32 length;
char[6] BSSID;
uint16 beacon_period;
uint16 capability;
uint8 SSID_len;
char[32] SSID;
uint8 channel;
uint16 atim_window;
uint8 dtim_period;
int16 RSSI;
uint8 n_cap;
uint32 nbss_cap;
char[16] basic_mcs;
uint16 ie_offset;
uint32 ie_length;
""", padding = 4)

# wifi.scan_get_ap_records
# no padding???
Struct.define("rtw_scan_result", """
uint8 SSID_len;
char[33] SSID;
char[6] BSSID;
int16 signal_strength;
uint32 bss_type;
uint32 security;
uint32 wps_type;
uint32 channel;
uint32 band;
""")

# lwip.bind
Struct.define("sockaddr_in", """
uint8    sin_len;
uint8    sin_family;
uint16   sin_port;
uint8[4] sin_addr;
char[8]  sin_zero;
""", padding = 4)

# setsockopt
Struct.define("ip_mreq", """
uint8[4] imr_multiaddr;
uint8[4] imr_interface;
""", padding = 4)

# select
Struct.define("fd_set", """
uint16 set;
""")

# select
Struct.define("timeval", """
int32 tv_sec;
int32 tv_usec;
""")

    
