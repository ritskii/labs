import json
import base64
from functools import wraps

def require_role(role):
    def decorator(func):
        @wraps(func)
        def wrapper(user_role, *args, **kwargs):
            if user_role != role:
                return f"Access denied: required role {role}"
            return func(user_role, *args, **kwargs)
        return wrapper
    return decorator

def validate_types(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__
        for (name, value) in list(zip(func.__code__.co_varnames, args)):
            if name in annotations and not isinstance(value, annotations[name]):
                return f"Type error: {name} must be {annotations[name].__name__}"
        return func(*args, **kwargs)
    return wrapper

def as_html(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<html><body>{result}</body></html>"
    return wrapper

def check_answer(correct):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result == correct
        return wrapper
    return decorator

def to_json(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result)
    return wrapper

def add_author(name):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, dict):
                result["author"] = name
            return result
        return wrapper
    return decorator

def discount(percent):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result * (1 - percent/100)
        return wrapper
    return decorator

def encrypt_base64(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return base64.b64encode(str(result).encode()).decode()
    return wrapper

def safe_run(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return f"Error: {e}"
    return wrapper

def clean_input(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        new_args = [a.strip().lower() if isinstance(a, str) else a for a in args]
        new_kwargs = {k: (v.strip().lower() if isinstance(v, str) else v) for k, v in kwargs.items()}
        return func(*new_args, **new_kwargs)
    return wrapper


@require_role("admin")
def secret_data(user_role):
    return "Top secret"

print(secret_data("admin"))
print(secret_data("user"))


@validate_types
def add(x: int, y: int):
    return x + y

print(add(2, 3))
print(add("2", 3))


@as_html
def greet(name):
    return f"Hello, {name}"

print(greet("World"))


@check_answer(42)
def answer():
    return 42

print(answer())


@to_json
def get_data():
    return {"item": "apple", "price": 10}

print(get_data())


@add_author("Ivan")
def product():
    return {"name": "Book", "price": 100}

print(product())


@discount(20)
def price():
    return 200

print(price())


@encrypt_base64
def message():
    return "Hello World"

print(message())


@safe_run
def divide(x, y):
    return x / y

print(divide(10, 2))
print(divide(10, 0))


@clean_input
def echo(text):
    return text

print(echo("   HeLLo   "))
