from transitions import State

states = []


def state(name):
    def state_decorator(f):
        states.append(State(name=name, on_enter=[f.__name__]))

        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)

        return wrapper

    return state_decorator
