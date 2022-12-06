// Run in windows powershell by "artillery run artillery_betsspace.yml"

module.exports = { helloFlow };

async function helloFlow(page) {
    // Go to https:www.betsspace.com
    await page.goto('https://www.betsspace.com');
    // Click header tab "all cushions"
    await page.get_by_role("link", name="All Cushions").click()
    // Click first entry
    await page.click("#Collection > ul > li:nth-child(1) > div > a")
    // Click add to cart
    await page.get_by_role("button", name="Add to cart").click()
}