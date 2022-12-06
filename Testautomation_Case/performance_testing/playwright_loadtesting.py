from test_betsspace_classes import BetsspaceHeader

import json


def add_to_cart_load_test(page) -> None:
    client = page.context.new_cdp_session(page)
    client.send('Performance.enable')
    driver = BetsspaceHeader(page)
    driver.home_page()
    driver.click_all_cushions()
    driver.nav_product_page()
    driver.add_product_to_cart()

    performanceMetrics = client.send('Performance.getMetrics')

    path = "D:\PycharmProjects\Testautomation_Case\performance_testing\performance_metrics.json"
    with open(path, 'w') as f:
        json.dump(performanceMetrics['metrics'], f, indent=2)
        f.close()
