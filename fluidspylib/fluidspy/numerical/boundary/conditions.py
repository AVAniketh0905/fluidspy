class BC:
    def __init__(self, type):
        self.type = type

    def apply(self, state, *args):
        if self.type == "constant":
            return self.constant(state, *args)
        elif self.type == "insulated":
            return self.insulated(state)
        else:
            raise ValueError(f"Unknown boundary condition type: {self.type}")

    def constant(self, state, *args):
        if len(args) != 2:
            raise ValueError(
                f"Constant boundary condition requires 2 arguments, but {len(args)} were given."
            )
        state[0] = args[0]
        state[-1] = args[-1]

        return state

    def insulated(self, state):
        state[0] = state[1]
        state[-1] = state[-2]
        return state
