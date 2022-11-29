module.exports = { helloFlow };

async function helloFlow(page) {
  await page.goto('https://betsspace.com/');
  await page.getByRole('link', { name: 'All Cushions' }).click();
  await page.getByRole('link', { name: 'Joseph Cush' }).click();
  await page.getByRole('button', { name: 'Add to cart' }).click();
}
