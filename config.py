CHROME_DRIVER_PATH = "D:/APP/Chrome/chromedriver/chromedriver.exe"

def get_driver_path():
    import os
    if os.path.exists(CHROME_DRIVER_PATH):
        return CHROME_DRIVER_PATH
    return None
