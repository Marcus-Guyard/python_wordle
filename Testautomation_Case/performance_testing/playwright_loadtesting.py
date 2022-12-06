
import json

def add_to_cart_load_test(page) -> None:
    client = page.context.new_cdp_session(page)
    client.send('Performance.enable')
    page.goto("https://betsspace.com/")
    page.get_by_role("link", name="All Cushions").click()
    page.get_by_role("link", name="Joseph Cush").click()
    page.get_by_role("button", name="Add to cart").click()

    performanceMetrics = client.send('Performance.getMetrics')

    path = "D:\PycharmProjects\Testautomation_Case\performance_testing\performance_metrics.json"
    with open(path, 'w') as f:
        json.dump(performanceMetrics['metrics'], f, indent=2)
        f.close()
