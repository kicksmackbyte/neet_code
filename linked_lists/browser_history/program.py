'''

# Prompt


You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.

Implement the BrowserHistory class:

    * BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
    * void visit(string url) Visits url from the current page. It clears up all the forward history.
    * string back(int steps) Move steps back in history.
        - If you can only return x steps in the history and steps > x, you will return only x steps.
        - Return the current url after moving back in history at most steps.
    * string forward(int steps) Move steps forward in history.
        - If you can only forward x steps in the history and steps > x, you will forward only x steps.
        - Return the current url after forwarding in history at most steps.


# Constraints

* 1 <= homepage.length <= 20
* 1 <= url.length <= 20
* 1 <= steps <= 100
* homepage and url consist of  '.' or lower case English letters.
* At most 5000 calls will be made to visit, back, and forward.


'''

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.position = 0


    def print(self):

        print(f'Position: {self.position}')
        for h in self.history:
            print(h)

        print()


    def visit(self, url: str) -> None:
        self.position += 1

        self.history = self.history[:self.position]
        self.history.append(url)


    def back(self, steps: int) -> str:

        position = max(0, self.position - steps)
        self.position = position

        return self.history[self.position]


    def forward(self, steps: int) -> str:

        position = min(len(self.history)-1, self.position + steps)
        self.position = position

        return self.history[self.position]



obj = BrowserHistory('leetcode.com')
obj.print()

obj.visit('google.com')
obj.print()

obj.visit('facebook.com')
obj.print()

obj.visit('youtube.com')
obj.print()


obj.back(1)
obj.print()

obj.back(1)
obj.print()


obj.forward(1)
obj.print()


obj.visit('linkedin.com')
obj.print()


obj.forward(2)
obj.print()

obj.back(2)
obj.print()

obj.back(7)
obj.print()

