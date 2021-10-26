class ParseTable:

    def __init__(self):
        self.stacks = []
        self.tokens = []
        self.methods = []

    def add(self, stack, token, method):
        self.stacks.append([s for s in stack])
        self.tokens.append(token.value)
        self.methods.append(method)
