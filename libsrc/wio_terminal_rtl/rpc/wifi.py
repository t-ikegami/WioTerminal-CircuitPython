from . import MTYPE_INVOKE, perform_request
from ..Codec import Codec

# rpc_wifi_connect(in string ssid, in string password @nullable, uint32 security_type,int32 key_id, uint32 semaphore) -> int32
def connect(ssid, password, security_type, key_id, semaphore) :
    codec = Codec(14, 1, MTYPE_INVOKE, "I{}b{}IiI", "i")
    return perform_request(codec, ssid, password, security_type, key_id, semaphore)

# rpc_wifi_connect_bssid(in binary bssid, in string ssid @nullable, in string password, uint32 security_type, int32 key_id, uint32 semaphore) -> int32
def connect_bssid(bssid, ssid, password, security_type, key_id, semaphore) :
    codec = Codec(14, 2, MTYPE_INVOKE, "I{}b{}I{}IiI", "i")
    return perform_request(codec, bssid, ssid, password, security_type, key_id, semaphore)

# rpc_wifi_disconnect() -> int32
def disconnect() :
    codec = Codec(14, 3, MTYPE_INVOKE, "", "i")
    return perform_request(codec)

# rpc_wifi_is_connected_to_ap() -> int32
def is_connected_to_ap() :
    codec = Codec(14, 4, MTYPE_INVOKE, "", "i")
    return perform_request(codec)

# rpc_wifi_is_up(uint32 itf) -> int32
def is_up(itf) :
    codec = Codec(14, 5, MTYPE_INVOKE, "I", "i")
    return perform_request(codec, itf)

# rpc_wifi_is_ready_to_transceive(uint32 itf) -> int32
def is_ready_to_transceive(itf) :
    codec = Codec(14, 6, MTYPE_INVOKE, "I", "i")
    return perform_request(codec, itf)

# rpc_wifi_set_mac_address(in binary mac) -> int32
def set_mac_address(mac) :
    codec = Codec(14, 7, MTYPE_INVOKE, "I{}", "i")
    return perform_request(codec, mac)

# rpc_wifi_get_mac_address(out uint8[18] mac) -> int32
def get_mac_address() :
    codec = Codec(14, 8, MTYPE_INVOKE, "", "18si")
    return perform_request(codec)

# rpc_wifi_enable_powersave() -> int32
def enable_powersave() :
    codec = Codec(14, 9, MTYPE_INVOKE, "", "i")
    return perform_request(codec)

# rpc_wifi_resume_powersave() -> int32
def resume_powersave() :
    codec = Codec(14, 10, MTYPE_INVOKE, "", "i")
    return perform_request(codec)

# rpc_wifi_disable_powersave() -> int32
def disable_powersave() :
    codec = Codec(14, 11, MTYPE_INVOKE, "", "i")
    return perform_request(codec)

# rpc_wifi_btcoex_set_bt_on() -> void
def btcoex_set_bt_on() :
    codec = Codec(14, 12, MTYPE_INVOKE, "", "")
    return perform_request(codec)

# rpc_wifi_btcoex_set_bt_off() -> void
def btcoex_set_bt_off() :
    codec = Codec(14, 13, MTYPE_INVOKE, "", "")
    return perform_request(codec)

# rpc_wifi_get_associated_client_list(out binary client_list_buffer, uint16 buffer_length) -> int32
def get_associated_client_list(buffer_length) :
    codec = Codec(14, 14, MTYPE_INVOKE, "H", "I{}i")
    return perform_request(codec, buffer_length)

# rpc_wifi_get_ap_bssid(out uint8[6] bssid) -> int32
def get_ap_bssid() :
    codec = Codec(14, 15, MTYPE_INVOKE, "", "6si")
    return perform_request(codec)

# rpc_wifi_get_ap_info(out binary ap_info, out uint32 security) -> int32
def get_ap_info() :
    codec = Codec(14, 16, MTYPE_INVOKE, "", "I{}Ii")
    return perform_request(codec)

# rpc_wifi_set_country(uint32 country_code) -> int32
def set_country(country_code) :
    codec = Codec(14, 17, MTYPE_INVOKE, "I", "i")
    return perform_request(codec, country_code)

# rpc_wifi_get_sta_max_data_rate(out uint8 inidata_rate) -> int32
def get_sta_max_data_rate() :
    codec = Codec(14, 18, MTYPE_INVOKE, "", "Bi")
    return perform_request(codec)

# rpc_wifi_get_rssi(out int32 pRSSI) -> int32
def get_rssi() :
    codec = Codec(14, 19, MTYPE_INVOKE, "", "ii")
    return perform_request(codec)

# rpc_wifi_set_channel(int32 channel) -> int32
def set_channel(channel) :
    codec = Codec(14, 20, MTYPE_INVOKE, "i", "i")
    return perform_request(codec, channel)

# rpc_wifi_get_channel(out int32 channel) -> int32
def get_channel() :
    codec = Codec(14, 21, MTYPE_INVOKE, "", "ii")
    return perform_request(codec)

# rpc_wifi_change_channel_plan(uint8 channel_plan) -> int32
def change_channel_plan(channel_plan) :
    codec = Codec(14, 22, MTYPE_INVOKE, "B", "i")
    return perform_request(codec, channel_plan)

# rpc_wifi_register_multicast_address(uint8[6] mac) -> int32
def register_multicast_address(mac) :
    codec = Codec(14, 23, MTYPE_INVOKE, "6s", "i")
    return perform_request(codec, mac)

# rpc_wifi_unregister_multicast_address(uint8[6] mac) -> int32
def unregister_multicast_address(mac) :
    codec = Codec(14, 24, MTYPE_INVOKE, "6s", "i")
    return perform_request(codec, mac)

# rpc_wifi_rf_on() -> int32
def rf_on() :
    codec = Codec(14, 25, MTYPE_INVOKE, "", "i")
    return perform_request(codec)

# rpc_wifi_rf_off() -> int32
def rf_off() :
    codec = Codec(14, 26, MTYPE_INVOKE, "", "i")
    return perform_request(codec)

# rpc_wifi_on(uint32 mode) -> int32
def on(mode) :
    codec = Codec(14, 27, MTYPE_INVOKE, "I", "i")
    return perform_request(codec, mode)

# rpc_wifi_off() -> int32
def off() :
    codec = Codec(14, 28, MTYPE_INVOKE, "", "i")
    return perform_request(codec)

# rpc_wifi_set_mode(uint32 mode) -> int32
def set_mode(mode) :
    codec = Codec(14, 29, MTYPE_INVOKE, "I", "i")
    return perform_request(codec, mode)

# rpc_wifi_off_fastly() -> int32
def off_fastly() :
    codec = Codec(14, 30, MTYPE_INVOKE, "", "i")
    return perform_request(codec)

# rpc_wifi_set_power_mode(uint8 ips_mode, uint8 lps_mode) -> int32
def set_power_mode(ips_mode, lps_mode) :
    codec = Codec(14, 31, MTYPE_INVOKE, "BB", "i")
    return perform_request(codec, ips_mode, lps_mode)

# rpc_wifi_set_tdma_param(uint8 slot_period, uint8 rfon_period_len_1, uint8 rfon_period_len_2, uint8 rfon_period_len_3) -> int32
def set_tdma_param(slot_period, rfon_period_len_1, rfon_period_len_2, rfon_period_len_3) :
    codec = Codec(14, 32, MTYPE_INVOKE, "BBBB", "i")
    return perform_request(codec, slot_period, rfon_period_len_1, rfon_period_len_2, rfon_period_len_3)

# rpc_wifi_set_lps_dtim(uint8 dtim) -> int32
def set_lps_dtim(dtim) :
    codec = Codec(14, 33, MTYPE_INVOKE, "B", "i")
    return perform_request(codec, dtim)

# rpc_wifi_get_lps_dtim(out uint8 dtim) -> int32
def get_lps_dtim() :
    codec = Codec(14, 34, MTYPE_INVOKE, "", "Bi")
    return perform_request(codec)

# rpc_wifi_set_lps_thresh(uint8 mode) -> int32
def set_lps_thresh(mode) :
    codec = Codec(14, 35, MTYPE_INVOKE, "B", "i")
    return perform_request(codec, mode)

# rpc_wifi_set_lps_level(uint8 lps_level) -> int32
def set_lps_level(lps_level) :
    codec = Codec(14, 36, MTYPE_INVOKE, "B", "i")
    return perform_request(codec, lps_level)

# rpc_wifi_set_mfp_support(uint8 value) -> int32
def set_mfp_support(value) :
    codec = Codec(14, 37, MTYPE_INVOKE, "B", "i")
    return perform_request(codec, value)

# rpc_wifi_start_ap(in string ssid, in string password @nullable, uint32 security_type, int32 channel) -> int32
def start_ap(ssid, password, security_type, channel) :
    codec = Codec(14, 38, MTYPE_INVOKE, "I{}b{}Ii", "i")
    return perform_request(codec, ssid, password, security_type, channel)

# rpc_wifi_start_ap_with_hidden_ssid(in string ssid, in string password @nullable, uint32 security_type, int32 channel) -> int32
def start_ap_with_hidden_ssid(ssid, password, security_type, channel) :
    codec = Codec(14, 39, MTYPE_INVOKE, "I{}b{}Ii", "i")
    return perform_request(codec, ssid, password, security_type, channel)

# rpc_wifi_set_pscan_chan(binary channel_list,uint8 pscan_config) -> int32
def set_pscan_chan(channel_list, pscan_config) :
    codec = Codec(14, 40, MTYPE_INVOKE, "I{}B", "i")
    return perform_request(codec, channel_list, pscan_config)

# rpc_wifi_get_setting(string ifname,out binary pSetting) -> int32
def get_setting(ifname) :
    codec = Codec(14, 41, MTYPE_INVOKE, "I{}", "I{}i")
    return perform_request(codec, ifname)

# rpc_wifi_set_network_mode(uint32 mode) -> int32
def set_network_mode(mode) :
    codec = Codec(14, 42, MTYPE_INVOKE, "I", "i")
    return perform_request(codec, mode)

# rpc_wifi_get_network_mode(out uint32 pmode) -> int32
def get_network_mode() :
    codec = Codec(14, 43, MTYPE_INVOKE, "", "Ii")
    return perform_request(codec)

# rpc_wifi_set_wps_phase(uint8 is_trigger_wps) -> int32
def set_wps_phase(is_trigger_wps) :
    codec = Codec(14, 44, MTYPE_INVOKE, "B", "i")
    return perform_request(codec, is_trigger_wps)

# rpc_wifi_restart_ap(in binary ssid, in binary password, uint32 security_type, int32 channel) -> int32
def restart_ap(ssid, password, security_type, channel) :
    codec = Codec(14, 45, MTYPE_INVOKE, "I{}I{}Ii", "i")
    return perform_request(codec, ssid, password, security_type, channel)

# rpc_wifi_config_autoreconnect(uint8 mode, uint8 retry_times, uint16 timeout) -> int32
def config_autoreconnect(mode, retry_times, timeout) :
    codec = Codec(14, 46, MTYPE_INVOKE, "BBH", "i")
    return perform_request(codec, mode, retry_times, timeout)

# rpc_wifi_set_autoreconnect(uint8 mode) -> int32
def set_autoreconnect(mode) :
    codec = Codec(14, 47, MTYPE_INVOKE, "B", "i")
    return perform_request(codec, mode)

# rpc_wifi_get_autoreconnect(out uint8 mode) -> int32
def get_autoreconnect() :
    codec = Codec(14, 48, MTYPE_INVOKE, "", "Bi")
    return perform_request(codec)

# rpc_wifi_get_last_error() -> int32
def get_last_error() :
    codec = Codec(14, 49, MTYPE_INVOKE, "", "i")
    return perform_request(codec)

# rpc_wifi_add_custom_ie(in binary cus_ie) -> int32
def add_custom_ie(cus_ie) :
    codec = Codec(14, 50, MTYPE_INVOKE, "I{}", "i")
    return perform_request(codec, cus_ie)

# rpc_wifi_update_custom_ie(in binary cus_ie, int32 ie_index) -> int32
def update_custom_ie(cus_ie, ie_index) :
    codec = Codec(14, 51, MTYPE_INVOKE, "I{}i", "i")
    return perform_request(codec, cus_ie, ie_index)

# rpc_wifi_del_custom_ie() -> int32
def del_custom_ie() :
    codec = Codec(14, 52, MTYPE_INVOKE, "", "i")
    return perform_request(codec)

# rpc_wifi_set_indicate_mgnt(int32 enable) -> void
def set_indicate_mgnt(enable) :
    codec = Codec(14, 53, MTYPE_INVOKE, "i", "")
    return perform_request(codec, enable)

# rpc_wifi_get_drv_ability(out uint32 ability) -> int32
def get_drv_ability() :
    codec = Codec(14, 54, MTYPE_INVOKE, "", "Ii")
    return perform_request(codec)

# rpc_wifi_set_channel_plan(uint8 channel_plan) -> int32
def set_channel_plan(channel_plan) :
    codec = Codec(14, 55, MTYPE_INVOKE, "B", "i")
    return perform_request(codec, channel_plan)

# rpc_wifi_get_channel_plan(out uint8 channel_plan) -> int32
def get_channel_plan() :
    codec = Codec(14, 56, MTYPE_INVOKE, "", "Bi")
    return perform_request(codec)

# rpc_wifi_enable_forwarding() -> int32
def enable_forwarding() :
    codec = Codec(14, 57, MTYPE_INVOKE, "", "i")
    return perform_request(codec)

# rpc_wifi_disable_forwarding() -> int32
def disable_forwarding() :
    codec = Codec(14, 58, MTYPE_INVOKE, "", "i")
    return perform_request(codec)

# rpc_wifi_set_ch_deauth(uint8 enable) -> int32
def set_ch_deauth(enable) :
    codec = Codec(14, 59, MTYPE_INVOKE, "B", "i")
    return perform_request(codec, enable)

# rpc_wifi_get_band_type() -> uint8
def get_band_type() :
    codec = Codec(14, 60, MTYPE_INVOKE, "", "B")
    return perform_request(codec)

# rpc_wifi_set_tx_pause_data(uint32 NewState) -> int32
def set_tx_pause_data(NewState) :
    codec = Codec(14, 61, MTYPE_INVOKE, "I", "i")
    return perform_request(codec, NewState)

# rpc_wifi_get_reconnect_data(out binary wifi_info) -> int32
def get_reconnect_data() :
    codec = Codec(14, 62, MTYPE_INVOKE, "", "I{}i")
    return perform_request(codec)

# rpc_wifi_clear_reconnect_data() -> int32
def clear_reconnect_data() :
    codec = Codec(14, 63, MTYPE_INVOKE, "", "i")
    return perform_request(codec)

# rpc_wifi_scan_start() -> int32
def scan_start() :
    codec = Codec(14, 64, MTYPE_INVOKE, "", "i")
    return perform_request(codec)

# rpc_wifi_is_scaning() -> bool
def is_scaning() :
    codec = Codec(14, 65, MTYPE_INVOKE, "", "b")
    return perform_request(codec)

# rpc_wifi_scan_get_ap_records(uint16 number, out binary _scanResult) -> int32
def scan_get_ap_records(number) :
    codec = Codec(14, 66, MTYPE_INVOKE, "H", "I{}i")
    return perform_request(codec, number)

# rpc_wifi_scan_get_ap_num() -> uint16
def scan_get_ap_num() :
    codec = Codec(14, 67, MTYPE_INVOKE, "", "H")
    return perform_request(codec)

