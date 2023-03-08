import websocket
import json
import http.client

# Ayarları buradan yap
host = "localhost"
http_port = 8080
ws_port = 8080
deviceid = "IRT28123456"
password = "password"
language = "tr"
# Ayarları buradan yap

def cmd_get_device_info(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    device_info = '{"model":"IRT28M","communication":{"rs232":1,"ethernet":true,"wifi":false},"SAM":false,"display":{"type":0},"keyboard":{"type":null},"audio":{"type":0},"outputs":{"relay":1,"MOSFET":1},"inputs":{"digitalinput":2}}'
    data = json.loads(device_info)
    resp['data'] = data
    return json.dumps(resp)

def cmd_get_app_version(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    device_info = '{"version":"10.05.01"}'
    data = json.loads(device_info)
    resp['data'] = data
    return json.dumps(resp)

def cmd_get_linux_version(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    device_info = '{"version":"dfgdf 10.05.01"}'
    data = json.loads(device_info)
    resp['data'] = data
    return json.dumps(resp)

def cmd_get_device_status(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    device_info = '{"status":"1"}'
    data = json.loads(device_info)
    resp['data'] = data
    return json.dumps(resp)

def cmd_sys_reboot(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    #device_info = '{"version":"dfgdf 10.05.01"}'
    #data = json.loads(device_info)
    #resp['data'] = data
    return json.dumps(resp)

def cmd_sys_shutdown(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    #device_info = '{"version":"dfgdf 10.05.01"}'
    #data = json.loads(device_info)
    #resp['data'] = data
    return json.dumps(resp)

def cmd_set_datetime(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    #device_info = '{"version":"dfgdf 10.05.01"}'
    #data = json.loads(device_info)
    #resp['data'] = data
    return json.dumps(resp)    

def cmd_get_uptime(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    device_info = '{"uptime":"1"}'
    data = json.loads(device_info)
    resp['data'] = data
    return json.dumps(resp)

def cmd_get_device_setting(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    device_info = {"deviceid": "TT78954366","name": "Ana Giriş 1","language": "tr"}
    data = json.loads(device_info)
    resp['data'] = data
    return json.dumps(resp)

def cmd_set_device_setting(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    #device_info = '{"version":"dfgdf 10.05.01"}'
    #data = json.loads(device_info)
    #resp['data'] = data
    resp['data'] = data
    return json.dumps(resp)

def cmd_set_auth_key_setting(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    #device_info = '{"version":"dfgdf 10.05.01"}'
    #data = json.loads(device_info)
    #resp['data'] = data
    resp['data'] = data
    return json.dumps(resp)

def cmd_get_card_reader_setting(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    device_info = {{"mode":"uid","user_data_sector":2,"access_data_sector":3,"canteen_data_sector":4,"user_data_file_id":"desfire v.b. için nasıl olmalı siz daha iyi bilirisniz","access_data_file_id":"desfire v.b. için nasıl olmalı siz daha iyi bilirisniz","canteen_data_file_id":"desfire v.b. için nasıl olmalı siz daha iyi bilirisniz"}}
    data = json.loads(device_info)
    resp['data'] = data
    return json.dumps(resp) 

def cmd_set_card_reader_setting(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    #device_info = '{"version":"dfgdf 10.05.01"}'
    #data = json.loads(device_info)
    #resp['data'] = data
    resp['data'] = data
    return json.dumps(resp)   

def cmd_get_face_reader_setting(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    device_info = {{"mode":"uid","user_data_sector":2,"access_data_sector":3,"canteen_data_sector":4,"user_data_file_id":"desfire v.b. için nasıl olmalı siz daha iyi bilirisniz","access_data_file_id":"desfire v.b. için nasıl olmalı siz daha iyi bilirisniz","canteen_data_file_id":"desfire v.b. için nasıl olmalı siz daha iyi bilirisniz"}}
    data = json.loads(device_info)
    resp['data'] = data
    return json.dumps(resp) 

def cmd_set_face_reader_setting(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    #device_info = '{"version":"dfgdf 10.05.01"}'
    #data = json.loads(device_info)
    #resp['data'] = data
    resp['data'] = data
    return json.dumps(resp)

def cmd_get_fp_reader_setting(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    device_info = {{"mode":"uid","user_data_sector":2,"access_data_sector":3,"canteen_data_sector":4,"user_data_file_id":"desfire v.b. için nasıl olmalı siz daha iyi bilirisniz","access_data_file_id":"desfire v.b. için nasıl olmalı siz daha iyi bilirisniz","canteen_data_file_id":"desfire v.b. için nasıl olmalı siz daha iyi bilirisniz"}}
    data = json.loads(device_info)
    resp['data'] = data
    return json.dumps(resp) 

def cmd_set_fp_reader_setting(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    #device_info = '{"version":"dfgdf 10.05.01"}'
    #data = json.loads(device_info)
    #resp['data'] = data
    resp['data'] = data
    return json.dumps(resp)

def cmd_get_qr_reader_setting(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    device_info = {{"mode":"uid","user_data_sector":2,"access_data_sector":3,"canteen_data_sector":4,"user_data_file_id":"desfire v.b. için nasıl olmalı siz daha iyi bilirisniz","access_data_file_id":"desfire v.b. için nasıl olmalı siz daha iyi bilirisniz","canteen_data_file_id":"desfire v.b. için nasıl olmalı siz daha iyi bilirisniz"}}
    data = json.loads(device_info)
    resp['data'] = data
    return json.dumps(resp) 

def cmd_set_qr_reader_setting(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    #device_info = '{"version":"dfgdf 10.05.01"}'
    #data = json.loads(device_info)
    #resp['data'] = data
    resp['data'] = data
    return json.dumps(resp)

def cmd_get_network_setting(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    device_info = {{"eth": {"DHCP": "false","ip": "192.168.1.221","subnet_mask": "255.255.255.255","default_gateway": "192.168.1.1","primary_dns": "","secondary_dns": ""},"wifi": {"DHCP": "false","ip": "192.168.1.221","subnet_mask": "255.255.255.255","default_gateway": "192.168.1.1","primary_dns": "","secondary_dns": ""}}}
    data = json.loads(device_info)
    resp['data'] = data
    return json.dumps(resp) 

def cmd_set_network_setting(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    #device_info = '{"version":"dfgdf 10.05.01"}'
    #data = json.loads(device_info)
    #resp['data'] = data
    resp['data'] = data
    return json.dumps(resp) 

def cmd_get_server_comunication_setting(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    device_info = {"sync_protocol": 1,"http_host": "192.168.1.225/api","ws_host": "192.168.1.225/api","password": "123abc","SSL": "true","auto_trx_event": {"mode": 1,"sync_ınterval": 10},"auto_sys_info_event": {"mode": 1,"sync_ınterval": 10}}
    data = json.loads(device_info)
    resp['data'] = data
    return json.dumps(resp) 

def cmd_set_server_comunication_setting(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    #device_info = '{"version":"dfgdf 10.05.01"}'
    #data = json.loads(device_info)
    #resp['data'] = data
    resp['data'] = data
    return json.dumps(resp) 

def cmd_get_output_setting(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    device_info = {"brightness": 10,"contrast": 60,"brightness_mode": 1,"drain_output_1_norm_high": "true","drain_output_1_norm_high": "false","relay_1_mode": 1,"relay_1_mode": 2,"volume": 10}
    data = json.loads(device_info)
    resp['data'] = data
    return json.dumps(resp) 

def cmd_set_output_setting(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    #device_info = '{"version":"dfgdf 10.05.01"}'
    #data = json.loads(device_info)
    #resp['data'] = data
    resp['data'] = data
    return json.dumps(resp)

def cmd_get_verification_source_setting(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    device_info = {"card": {"mode": 2,"enable_online_on_undefiined": "false","enable_offline_on_timeout": "false"},"qr": {"mode": 2,"enable_online_on_undefiined": "false","enable_offline_on_timeout": "false"},"face": {"mode": 2,"enable_online_on_undefiined": "false","enable_offline_on_timeout": "false"},"fp": {"mode": 2,"enable_online_on_undefiined": "false","enable_offline_on_timeout": "false"}}
    data = json.loads(device_info)
    resp['data'] = data
    return json.dumps(resp) 

def cmd_set_verification_source_setting(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    #device_info = '{"version":"dfgdf 10.05.01"}'
    #data = json.loads(device_info)
    #resp['data'] = data
    resp['data'] = data
    return json.dumps(resp)   
        
def cmd_get_capacity_setting(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    device_info = {{"max_user_count": 50000,"max_event_rec_count": 50000,"max_event_rec_days": 90,"max_trans_rec_count": 50000,"max_trans_rec_days": 90,"sys_info_period": 300,"hw_info_period": 300}}
    data = json.loads(device_info)
    resp['data'] = data
    return json.dumps(resp)

def cmd_get_application_setting(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    device_info = {"application_type": "access","enable_bell_ring": "false","bell_ring_output": 0,"bell_ring_on_device": "false","bell_ring_volume": 1,"enable_out_of_service": "false","out_of_service_output": 0,"time_zone_enable": "true","def_verification_mode": 1,"re_verification_timeout": 0,"reader_direction": 1,"restricted_zone_no": 1,"input_1": {"input_type": 1,"timeout": 5},"input_2": {"input_type": 1,"timeout": 5}}
    data = json.loads(device_info)
    resp['data'] = data
    return json.dumps(resp) 

def cmd_set_application_setting(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    #device_info = '{"version":"dfgdf 10.05.01"}'
    #data = json.loads(device_info)
    #resp['data'] = data
    resp['data'] = data
    return json.dumps(resp)

def cmd_get_apb_setting(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    device_info = {"type": 1,"duration": 10}
    data = json.loads(device_info)
    resp['data'] = data
    return json.dumps(resp) 

def cmd_set_apb_setting(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    #device_info = '{"version":"dfgdf 10.05.01"}'
    #data = json.loads(device_info)
    #resp['data'] = data
    resp['data'] = data
    return json.dumps(resp)

def cmd_get_screen_message(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    device_info = {"id":1,"screen_type":2,"default_screen_type":1,"line_1":{"text":"Başarılı Geçiş","font_name":"tt","font_color":"formata karar verelim","background_color":""},"line_2":{"text":"test 1","font_name":"tt","font_color":"formata karar verelim","background_color":""},"line_3":{"text":"test 1","font_name":"tt","font_color":"formata karar verelim","background_color":""},"footer":{"text":"test 1","font_name":"tt","font_color":"formata karar verelim","background_color":""},"icon_id":"","screen_duration":10,"infinite":"false","tr_out_1_duration":10,"tr_out_2_duration":10,"rl_1_duration":10,"rl_2_duration":10,"sound_duration":10,"is_blink":"true","audio_id":"","next_id":100}
    data = json.loads(device_info)
    resp['data'] = data
    return json.dumps(resp) 

def cmd_set_screen_message(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    #device_info = '{"version":"dfgdf 10.05.01"}'
    #data = json.loads(device_info)
    #resp['data'] = data
    resp['data'] = data
    return json.dumps(resp)

def cmd_get_screen_message_all(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    device_info = {"id":1,"screen_type":2,"default_screen_type":1,"line_1":{"text":"Başarılı Geçiş","font_name":"tt","font_color":"formata karar verelim","background_color":""},"line_2":{"text":"test 1","font_name":"tt","font_color":"formata karar verelim","background_color":""},"line_3":{"text":"test 1","font_name":"tt","font_color":"formata karar verelim","background_color":""},"footer":{"text":"test 1","font_name":"tt","font_color":"formata karar verelim","background_color":""},"icon_id":"","screen_duration":10,"infinite":"false","tr_out_1_duration":10,"tr_out_2_duration":10,"rl_1_duration":10,"rl_2_duration":10,"sound_duration":10,"is_blink":"true","audio_id":"","next_id":100}
    data = json.loads(device_info)
    resp['data'] = data
    return json.dumps(resp) 

def cmd_set_screen_message_all(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    #device_info = '{"version":"dfgdf 10.05.01"}'
    #data = json.loads(device_info)
    #resp['data'] = data
    resp['data'] = data
    return json.dumps(resp)

def cmd_get_time_zone_all(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    device_info = {"id":1,"name":"Tam geçiş","details":[{"day_of_week":1,"times":[{"start_time":"09:00","end_time":"12:00","verification_mode":1},{"start_time":"13:00","end_time":"18:00","verification_mode":2}]},{"day_of_week":2,"times":[{"start_time":"09:00","end_time":"12:00","verification_mode":1},{"start_time":"13:00","end_time":"18:00","verification_mode":2}]}]}
    data = json.loads(device_info)
    resp['data'] = data
    return json.dumps(resp) 

def cmd_set_time_zone_all(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    #device_info = '{"version":"dfgdf 10.05.01"}'
    #data = json.loads(device_info)
    #resp['data'] = data
    resp['data'] = data
    return json.dumps(resp)

def cmd_get_time_zone(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    device_info = {"id":1,"name":"Tam geçiş","details":[{"day_of_week":1,"times":[{"start_time":"09:00","end_time":"12:00","verification_mode":1},{"start_time":"13:00","end_time":"18:00","verification_mode":2}]},{"day_of_week":2,"times":[{"start_time":"09:00","end_time":"12:00","verification_mode":1},{"start_time":"13:00","end_time":"18:00","verification_mode":2}]}]}
    data = json.loads(device_info)
    resp['data'] = data
    return json.dumps(resp) 

def cmd_set_time_zone(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    #device_info = '{"version":"dfgdf 10.05.01"}'
    #data = json.loads(device_info)
    #resp['data'] = data
    resp['data'] = data
    return json.dumps(resp)  

def cmd_get_out_of_service_all(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    device_info = {"id":1,"name":"Tam geçiş","details":[{"day_of_week":1,"times":[{"start_time":"09:00","end_time":"12:00","verification_mode":1},{"start_time":"13:00","end_time":"18:00","verification_mode":2}]},{"day_of_week":2,"times":[{"start_time":"09:00","end_time":"12:00","verification_mode":1},{"start_time":"13:00","end_time":"18:00","verification_mode":2}]}]}
    data = json.loads(device_info)
    resp['data'] = data
    return json.dumps(resp) 

def cmd_set_out_of_service_all(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    #device_info = '{"version":"dfgdf 10.05.01"}'
    #data = json.loads(device_info)
    #resp['data'] = data
    resp['data'] = data
    return json.dumps(resp)

def cmd_get_out_of_service(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    device_info = {"id":1,"name":"Tam geçiş","details":[{"day_of_week":1,"times":[{"start_time":"09:00","end_time":"12:00","verification_mode":1},{"start_time":"13:00","end_time":"18:00","verification_mode":2}]},{"day_of_week":2,"times":[{"start_time":"09:00","end_time":"12:00","verification_mode":1},{"start_time":"13:00","end_time":"18:00","verification_mode":2}]}]}
    data = json.loads(device_info)
    resp['data'] = data
    return json.dumps(resp) 

def cmd_set_out_of_service(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    #device_info = '{"version":"dfgdf 10.05.01"}'
    #data = json.loads(device_info)
    #resp['data'] = data
    resp['data'] = data
    return json.dumps(resp)

def cmd_get_bell_all(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    device_info = {"id":1,"name":"Tam geçiş","details":[{"day_of_week":1,"times":[{"start_time":"09:00","end_time":"12:00","verification_mode":1},{"start_time":"13:00","end_time":"18:00","verification_mode":2}]},{"day_of_week":2,"times":[{"start_time":"09:00","end_time":"12:00","verification_mode":1},{"start_time":"13:00","end_time":"18:00","verification_mode":2}]}]}
    data = json.loads(device_info)
    resp['data'] = data
    return json.dumps(resp) 

def cmd_set_bell_all(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    #device_info = '{"version":"dfgdf 10.05.01"}'
    #data = json.loads(device_info)
    #resp['data'] = data
    resp['data'] = data
    return json.dumps(resp)

def cmd_get_bell(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    device_info = {"id":1,"name":"Tam geçiş","details":[{"day_of_week":1,"times":[{"start_time":"09:00","end_time":"12:00","verification_mode":1},{"start_time":"13:00","end_time":"18:00","verification_mode":2}]},{"day_of_week":2,"times":[{"start_time":"09:00","end_time":"12:00","verification_mode":1},{"start_time":"13:00","end_time":"18:00","verification_mode":2}]}]}
    data = json.loads(device_info)
    resp['data'] = data
    return json.dumps(resp) 

def cmd_set_bell(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    #device_info = '{"version":"dfgdf 10.05.01"}'
    #data = json.loads(device_info)
    #resp['data'] = data
    resp['data'] = data
    return json.dumps(resp)

def cmd_get_holiday_all(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    device_info = [{"id":1,"name":"Zafer bayramı","start_dt":"2022-09-30 00:00:00","end_dt":"2022-09-30 23:59:59"},{"id":2,"name":"Cumhuriyet bayramı","start_dt":"2022-10-28 13:00:00","end_dt":"2022-10-29 23:59:59"}]
    data = json.loads(device_info)
    resp['data'] = data
    return json.dumps(resp) 

def cmd_set_holiday_all(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    #device_info = '{"version":"dfgdf 10.05.01"}'
    #data = json.loads(device_info)
    #resp['data'] = data
    resp['data'] = data
    return json.dumps(resp)

def cmd_remove_time_zone(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    #device_info = '{"version":"dfgdf 10.05.01"}'
    #data = json.loads(device_info)
    #resp['data'] = data
    resp['data'] = data
    return json.dumps(resp)

def cmd_remove_time_zone_all(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    #device_info = '{"version":"dfgdf 10.05.01"}'
    #data = json.loads(device_info)
    #resp['data'] = data
    resp['data'] = data
    return json.dumps(resp)

def cmd_remove_out_of_service(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    #device_info = '{"version":"dfgdf 10.05.01"}'
    #data = json.loads(device_info)
    #resp['data'] = data
    resp['data'] = data
    return json.dumps(resp)

def cmd_remove_out_of_service_all(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    #device_info = '{"version":"dfgdf 10.05.01"}'
    #data = json.loads(device_info)
    #resp['data'] = data
    resp['data'] = data
    return json.dumps(resp) 

def cmd_remove_bell(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    #device_info = '{"version":"dfgdf 10.05.01"}'
    #data = json.loads(device_info)
    #resp['data'] = data
    resp['data'] = data
    return json.dumps(resp)

def cmd_remove_bell_all(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    #device_info = '{"version":"dfgdf 10.05.01"}'
    #data = json.loads(device_info)
    #resp['data'] = data
    resp['data'] = data
    return json.dumps(resp)

def cmd_get_black_list(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    device_info = [{"id":1,"name":"Zafer bayramı","start_dt":"2022-09-30 00:00:00","end_dt":"2022-09-30 23:59:59"},{"id":2,"name":"Cumhuriyet bayramı","start_dt":"2022-10-28 13:00:00","end_dt":"2022-10-29 23:59:59"}]
    data = json.loads(device_info)
    resp['data'] = data
    return json.dumps(resp) 

def cmd_set_black_list(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    #device_info = '{"version":"dfgdf 10.05.01"}'
    #data = json.loads(device_info)
    #resp['data'] = data
    resp['data'] = data
    return json.dumps(resp) 

def cmd_remove_black_list(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    #device_info = '{"version":"dfgdf 10.05.01"}'
    #data = json.loads(device_info)
    #resp['data'] = data
    resp['data'] = data
    return json.dumps(resp) 

def cmd_get_black_list_all(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    device_info = [{"id":1,"name":"Zafer bayramı","start_dt":"2022-09-30 00:00:00","end_dt":"2022-09-30 23:59:59"},{"id":2,"name":"Cumhuriyet bayramı","start_dt":"2022-10-28 13:00:00","end_dt":"2022-10-29 23:59:59"}]
    data = json.loads(device_info)
    resp['data'] = data
    return json.dumps(resp) 

def cmd_set_black_list_all(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    #device_info = '{"version":"dfgdf 10.05.01"}'
    #data = json.loads(device_info)
    #resp['data'] = data
    resp['data'] = data
    return json.dumps(resp) 

def cmd_remove_black_list_all(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    #device_info = '{"version":"dfgdf 10.05.01"}'
    #data = json.loads(device_info)
    #resp['data'] = data
    resp['data'] = data
    return json.dumps(resp) 

def cmd_get_user(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    device_info = [{"id":1,"fullname":"Ozan Güçlü","password":"122465","start_date":"2022-01-01","expire_date":"2028-12-31","birth_date":"1977-01-30","access_enabled":"false","time_zone_enabled":"false","time_zone_id":1,"apb_enabled":"false","verify_online":"false","permited_in_emergency":"false","flx_text_1":"text 1","flx_text_2":"text 2","flx_text_3":"text 1","verification_mode":1,"uniqueids":["455466","6546546456"],"profile_photo":"base64(resim)"},{"id":2,"name":"Cumhuriyet bayramı","start_dt":"2022-10-28 13:00:00","end_dt":"2022-10-29 23:59:59"}]
    data = json.loads(device_info)
    resp['data'] = data
    return json.dumps(resp) 

def cmd_set_user(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    #device_info = '{"version":"dfgdf 10.05.01"}'
    #data = json.loads(device_info)
    #resp['data'] = data
    resp['data'] = data
    return json.dumps(resp) 

def cmd_remove_user(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    #device_info = '{"version":"dfgdf 10.05.01"}'
    #data = json.loads(device_info)
    #resp['data'] = data
    resp['data'] = data
    return json.dumps(resp) 

def cmd_get_user_all(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    device_info = [{"id":1,"fullname":"Ozan Güçlü","password":"122465","start_date":"2022-01-01","expire_date":"2028-12-31","birth_date":"1977-01-30","access_enabled":"false","time_zone_enabled":"false","time_zone_id":1,"apb_enabled":"false","verify_online":"false","permited_in_emergency":"false","flx_text_1":"text 1","flx_text_2":"text 2","flx_text_3":"text 1","verification_mode":1,"uniqueids":["455466","6546546456"],"profile_photo":"base64(resim)"}]
    data = json.loads(device_info)
    resp['data'] = data
    return json.dumps(resp) 

def cmd_set_user_all(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    #device_info = '{"version":"dfgdf 10.05.01"}'
    #data = json.loads(device_info)
    #resp['data'] = data
    resp['data'] = data
    return json.dumps(resp) 

def cmd_remove_user_all(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    #device_info = '{"version":"dfgdf 10.05.01"}'
    #data = json.loads(device_info)
    #resp['data'] = data
    resp['data'] = data
    return json.dumps(resp)  

def cmd_get_black_list_cnt(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    device_info = {"count":"1"}
    data = json.loads(device_info)
    resp['data'] = data
    return json.dumps(resp)

def cmd_get_user_cnt(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    device_info = {"count":"1"}
    data = json.loads(device_info)
    resp['data'] = data
    return json.dumps(resp) 

def cmd_get_user_list(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    device_info = {{"user_ids":[1,2]}}
    data = json.loads(device_info)
    resp['data'] = data
    return json.dumps(resp)

def cmd_get_user_uniqueid(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    device_info = {{["1","2"]}}
    data = json.loads(device_info)
    resp['data'] = data
    return json.dumps(resp) 

def cmd_set_user_uniqueid(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    #device_info = '{"version":"dfgdf 10.05.01"}'
    #data = json.loads(device_info)
    #resp['data'] = data
    resp['data'] = data
    return json.dumps(resp) 

def cmd_remove_user_uniqueid(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    #device_info = '{"version":"dfgdf 10.05.01"}'
    #data = json.loads(device_info)
    #resp['data'] = data
    resp['data'] = data
    return json.dumps(resp)  

def cmd_remove_user_uniqueid_all(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    #device_info = '{"version":"dfgdf 10.05.01"}'
    #data = json.loads(device_info)
    #resp['data'] = data
    resp['data'] = data
    return json.dumps(resp) 

def cmd_get_user_photo_profile(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    device_info = [{"id":1,"fullname":"Ozan Güçlü"}]
    data = json.loads(device_info)
    resp['data'] = data
    return json.dumps(resp) 

def cmd_set_user_photo_profile(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    #device_info = '{"version":"dfgdf 10.05.01"}'
    #data = json.loads(device_info)
    #resp['data'] = data
    resp['data'] = data
    return json.dumps(resp) 

def cmd_remove_user_photo_profile(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    #device_info = '{"version":"dfgdf 10.05.01"}'
    #data = json.loads(device_info)
    #resp['data'] = data
    resp['data'] = data
    return json.dumps(resp) 

def cmd_get_user_time_zone(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    device_info = [{"time_zone":{"date":"2022-09-22","times":[{"start_time":"12:12:12","end_time":"13:13:13","verification_mode":1},{"start_time":"16:12:12","end_time":"17:13:13","verification_mode":1}]}}]
    data = json.loads(device_info)
    resp['data'] = data
    return json.dumps(resp)

def cmd_set_user_time_zone(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    #device_info = '{"version":"dfgdf 10.05.01"}'
    #data = json.loads(device_info)
    #resp['data'] = data
    resp['data'] = data
    return json.dumps(resp) 

def cmd_remove_user_time_zone(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    #device_info = '{"version":"dfgdf 10.05.01"}'
    #data = json.loads(device_info)
    #resp['data'] = data
    resp['data'] = data
    return json.dumps(resp) 


def cmd_get_user_time_zone_all(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    device_info = [{"time_zone":{"date":"2022-09-22","times":[{"start_time":"12:12:12","end_time":"13:13:13","verification_mode":1},{"start_time":"16:12:12","end_time":"17:13:13","verification_mode":1}]}}]
    data = json.loads(device_info)
    resp['data'] = data
    return json.dumps(resp)

def cmd_set_user_time_zone_all(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    #device_info = '{"version":"dfgdf 10.05.01"}'
    #data = json.loads(device_info)
    #resp['data'] = data
    resp['data'] = data
    return json.dumps(resp) 

def cmd_remove_user_time_zone_all(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    #device_info = '{"version":"dfgdf 10.05.01"}'
    #data = json.loads(device_info)
    #resp['data'] = data
    resp['data'] = data
    return json.dumps(resp)


def cmd_get_trx(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    device_info = [{"user_id":1,"uniqueid":"45487ef","record_type":1,"trx_dt":"2022-09-21 10:10:10","io_type":0,"doorno":1,"turnstile_turn":"false","is_online":"false","verification_mode":1},{"user_id":1,"uniqueid":"45487ef","record_type":1,"trx_dt":"2022-09-21 10:11:10","io_type":1,"doorno":1,"turnstile_turn":"false","is_online":"false","verification_mode":1}]
    data = json.loads(device_info)
    resp['data'] = data
    return json.dumps(resp)

def cmd_transfer_trx(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    device_info = [{"user_id":1,"uniqueid":"45487ef","record_type":1,"trx_dt":"2022-09-21 10:10:10","io_type":0,"doorno":1,"turnstile_turn":"false","is_online":"false","verification_mode":1},{"user_id":1,"uniqueid":"45487ef","record_type":1,"trx_dt":"2022-09-21 10:11:10","io_type":1,"doorno":1,"turnstile_turn":"false","is_online":"false","verification_mode":1}]
    data = json.loads(device_info)
    resp['data'] = data
    return json.dumps(resp)

def cmd_get_device_event(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    device_info = [{"user_id":1,"uniqueid":"45487ef","record_type":1,"trx_dt":"2022-09-21 10:10:10","io_type":0,"doorno":1,"turnstile_turn":"false","is_online":"false","verification_mode":1},{"user_id":1,"uniqueid":"45487ef","record_type":1,"trx_dt":"2022-09-21 10:11:10","io_type":1,"doorno":1,"turnstile_turn":"false","is_online":"false","verification_mode":1}]
    data = json.loads(device_info)
    resp['data'] = data
    return json.dumps(resp) 

def cmd_transfer_device_event(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    device_info = [{"user_id":1,"uniqueid":"45487ef","record_type":1,"trx_dt":"2022-09-21 10:10:10","io_type":0,"doorno":1,"turnstile_turn":"false","is_online":"false","verification_mode":1},{"user_id":1,"uniqueid":"45487ef","record_type":1,"trx_dt":"2022-09-21 10:11:10","io_type":1,"doorno":1,"turnstile_turn":"false","is_online":"false","verification_mode":1}]
    data = json.loads(device_info)
    resp['data'] = data
    return json.dumps(resp) 

def cmd_remote_enroll(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    device_info = [{"user_id":1,"uniqueid":"45487ef","record_type":1,"trx_dt":"2022-09-21 10:10:10","io_type":0,"doorno":1,"turnstile_turn":"false","is_online":"false","verification_mode":1},{"user_id":1,"uniqueid":"45487ef","record_type":1,"trx_dt":"2022-09-21 10:11:10","io_type":1,"doorno":1,"turnstile_turn":"false","is_online":"false","verification_mode":1}]
    data = json.loads(device_info)
    resp['data'] = data
    return json.dumps(resp)


def on_message(ws, message):
    print(message)
    command = json.loads(message)
    if ("method" in command):
        if (command.get('method') == "get_device_info"):
            res = cmd_get_device_info(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "get_app_version"):
            res = cmd_get_app_version(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "get_linux_version"):
            res = cmd_get_linux_version(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "get_device_status"):
            res = cmd_get_device_status(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "sys_reboot"):
            res = cmd_sys_reboot(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "sys_shutdown"):
            res = cmd_sys_shutdown(command.get('requestid'), command.get('command.data')) 
        elif(command.get('method') == "set_date_time"):
            res = cmd_set_datetime(command.get('requestid'), command.get('command.data')) 
        elif(command.get('method') == "get_uptime"):
            res = cmd_get_uptime(command.get('requestid'), command.get('command.data')) 
        elif(command.get('method') == "get_device_setting"):
            res = cmd_get_device_setting(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "set_device_setting"):
            res = cmd_set_device_setting(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "set_auth_key_setting"):
            res = cmd_set_auth_key_setting(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "get_card_reader_setting"):
            res = cmd_get_card_reader_setting(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "set_card_reader_setting"):
            res = cmd_set_card_reader_setting(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "get_face_reader_setting"):
            res = cmd_get_face_reader_setting(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "set_face_reader_setting"):
            res = cmd_set_face_reader_setting(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "get_fp_reader_setting"):
            res = cmd_get_fp_reader_setting(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "set_fp_reader_setting"):
            res = cmd_set_fp_reader_setting(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "get_qr_reader_setting"):
            res = cmd_get_qr_reader_setting(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "set_qr_reader_setting"):
            res = cmd_set_qr_reader_setting(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "get_network_setting"):
            res = cmd_get_network_setting(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "set_network_setting"):
            res = cmd_set_network_setting(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "get_server_comunication_setting"):
            res = cmd_get_server_comunication_setting(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "set_server_comunication_setting"):
            res = cmd_set_server_comunication_setting(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "get_output_setting"):
            res = cmd_get_output_setting(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "set_output_setting"):
            res = cmd_set_output_setting(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "get_capacity_setting"):
            res = cmd_get_capacity_setting(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "get_verification_source_setting"):
            res = cmd_get_verification_source_setting(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "set_verification_source_setting"):
            res = cmd_set_verification_source_setting(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "get_application_setting"):
            res = cmd_get_application_setting(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "set_application_setting"):
            res = cmd_set_application_setting(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "get_apb_setting"):
            res = cmd_get_apb_setting(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "set_apb_setting"):
            res = cmd_set_apb_setting(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "get_screen_message"):
            res = cmd_get_screen_message(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "set_screen_message"):
            res = cmd_set_screen_message(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "get_screen_message_all"):
            res = cmd_get_screen_message_all(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "set_screen_message_all"):
            res = cmd_set_screen_message_all(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "get_time_zone"):
            res = cmd_get_time_zone(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "set_time_zone"):
            res = cmd_set_time_zone(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "remove_time_zone"):
            res = cmd_remove_time_zone(command.get('requestid'), command.get('command.data'))    
        elif(command.get('method') == "get_time_zone_all"):
            res = cmd_get_time_zone_all(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "remove_time_zone_all"):
            res = cmd_remove_time_zone_all(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "set_time_zone_all"):
            res = cmd_set_time_zone_all(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "get_out_of_service"):
            res = cmd_get_out_of_service(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "set_out_of_service"):
            res = cmd_set_out_of_service(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "remove_out_of_service"):
            res = cmd_remove_out_of_service(command.get('requestid'), command.get('command.data'))    
        elif(command.get('method') == "get_out_of_service_all"):
            res = cmd_get_out_of_service_all(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "set_out_of_service_all"):
            res = cmd_set_out_of_service_all(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "remove_out_of_service_all"):
            res = cmd_remove_out_of_service_all(command.get('requestid'), command.get('command.data'))    
        elif(command.get('method') == "get_bell"):
            res = cmd_get_bell(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "set_bell"):
            res = cmd_set_bell(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "remove_bell"):
            res = cmd_remove_bell(command.get('requestid'), command.get('command.data'))    
        elif(command.get('method') == "get_bell_all"):
            res = cmd_get_bell_all(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "set_bell_all"):
            res = cmd_set_bell_all(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "remove_bell_all"):
            res = cmd_set_bell_all(command.get('requestid'), command.get('command.data'))    
        elif(command.get('method') == "get_holiday_all"):
            res = cmd_get_holiday_all(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "set_holiday_all"):
            res = cmd_set_holiday_all(command.get('requestid'), command.get('command.data')) 
        elif(command.get('method') == "get_user_all"):
            res = cmd_get_user_all(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "set_user_all"):
            res = cmd_set_user_all(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "get_user"):
            res = cmd_get_user(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "set_user"):
            res = cmd_set_user(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "remove_user_all"):
            res = cmd_remove_user_all(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "remove_user"):
            res = cmd_remove_user(command.get('requestid'), command.get('command.data')) 
        elif(command.get('method') == "get_black_list"):
            res = cmd_get_black_list(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "set_black_list"):
            res = cmd_set_black_list(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "remove_black_list"):
            res = cmd_remove_black_list(command.get('requestid'), command.get('command.data')) 
        elif(command.get('method') == "get_black_list_count"):
            res = cmd_get_black_list_cnt(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "get_user_list"):
            res = cmd_get_user_list(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "get_user_uniqueid"):
            res = cmd_get_user_uniqueid(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "set_user_uniqueid"):
            res = cmd_set_user_uniqueid(command.get('requestid'), command.get('command.data')) 
        elif(command.get('method') == "remove_user_uniqueid"):
            res = cmd_remove_user_uniqueid(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "get_user_photo_profile"):
            res = cmd_get_user_photo_profile(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "set_user_photo_profile"):
            res = cmd_set_user_photo_profile(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "remove_user_photo_profile"):
            res = cmd_remove_user_photo_profile(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "get_user_time_zone"):
            res = cmd_get_user_time_zone(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "set_user_time_zone"):
            res = cmd_set_user_time_zone(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "remove_user_time_zone"):
            res = cmd_remove_user_time_zone(command.get('requestid'), command.get('command.data')) 
        elif(command.get('method') == "get_user_time_zone_all"):
            res = cmd_get_user_time_zone_all(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "set_user_time_zone_all"):
            res = cmd_set_user_time_zone_all(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "remove_user_time_zone_all"):
            res = cmd_remove_user_time_zone_all(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "get_trx"):
            res = cmd_get_trx(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "transfer_trx"):
            res = cmd_transfer_trx(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "get_device_event"):
            res = cmd_get_device_event(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "transfer_device_event"):
            res = cmd_transfer_device_event(command.get('requestid'), command.get('command.data'))
        elif(command.get('method') == "remote_enroll"):
            res = cmd_remote_enroll(command.get('requestid'), command.get('command.data'))                                                                
       
        else:
            res = "Invalid Command"
        ws.send(res)


def on_error(ws, error):
    print(error)


def on_close(ws, close_status_code, close_msg):
    print("Disconnected")


def on_open(ws):
    print("Connected")

conn = http.client.HTTPConnection(host, http_port)
payload = ''
headers = {
    'jwtdeviceid': deviceid,
    'jwtpassword': password,
    'jwtlanguage': language
}
    
conn.request("POST", "/api/login", payload, headers)
res = conn.getresponse()
if res.status == 200:
    data = json.loads(res.read())
    print(data)
websocket.enableTrace(False)
ws = websocket.WebSocketApp("ws://" + host + ":" + str(ws_port) + "?token=" + data['token'],
                            on_open=on_open,
                            on_message=on_message,
                            on_error=on_error,
                            on_close=on_close)

ws.run_forever(reconnect=5)
