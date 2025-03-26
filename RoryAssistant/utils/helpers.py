import psutil

def get_open_browsers():
    browsers = ["chrome", "firefox", "edge", "safari", "brave"]
    open_browsers = []
    for process in psutil.process_iter(['name']):
        for browser in browsers:
            if browser in process.info['name'].lower() and browser not in open_browsers:
                open_browsers.append(browser)
    return open_browsers