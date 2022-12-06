from locust import HttpUser, SequentialTaskSet, task, between


class User(HttpUser):
    @task
    class SequenceOfTasks(SequentialTaskSet):
        wait_time = between(1, 5)

        @task
        def mainPage(self):
            self.client.get("/")
            self.client.get("https://api.demoblaze.com/entries")

        @task
        def clickProduct(self):
            self.client.get("/prod.html?idp_=1")
            self.client.options("https://api.demoblaze.com/check")
            self.client.options("https://api.demoblaze.com/view")
            self.client.post("https://api.demoblaze.com/check", json={"token": "YWFhYTE2MzA5NDU="})
            self.client.post("https://api.demoblaze.com/view", json={"id": "1"})

        @task
        def addToCart(self):
            self.client.options("https://api.demoblaze.com/addtocart")
            self.client.post("https://api.demoblaze.com/addtocart",
                             json={"id": "fb3d5d23-f88c-80d9-a8de-32f1b6034bfd", "cookie": "YWFhYTE2MzA5NDU=",
                                   "prod_id": 1, "flag": 'true'})

        @task
        def viewCart(self):
            self.client.get("/cart")
