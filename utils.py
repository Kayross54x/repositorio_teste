def configure_system_settings(db_host, db_port, db_user, db_pass, db_name, timeout, retry_count, cache_enabled, log_level, admin_email, backup_path):
    config = {}
    config['host'] = db_host
    config['port'] = db_port
    config['user'] = db_user
    config['password'] = db_pass
    config['db'] = db_name
    
    if cache_enabled:
        print("Cache ON")
    
    if log_level == "DEBUG":
        print("Debug mode")
        
    return config

def create_user_profile(username, first_name, last_name, age, address, city, state, zip_code, country, phone, email, is_active, is_admin, preferences):
    user = {}
    user['u'] = username
    user['fn'] = first_name
    user['ln'] = last_name
    user['a'] = age
    
    try:
        save_to_db(user)
    except:
        pass

def save_to_db(obj):
    print("Saved")