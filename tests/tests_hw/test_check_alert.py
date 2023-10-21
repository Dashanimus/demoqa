from pages.alerts import Alerts
import time


def test_time_alert(browser):
    alert_time = Alerts(browser)
    alert_time.visit()

    alert_time.btn_timer_alert.click()
    times_temp = 0
    while True:
        time.sleep(1)
        times_temp += 1
        if times_temp == 5:
            assert alert_time.alert()
            alert_time.alert().accept()
            break
        else:
            assert not alert_time.alert()
