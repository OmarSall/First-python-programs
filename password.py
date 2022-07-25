def foo(password):
    if isinstance(password, str):
        if len(password) >= 8:
            return True
        else:
            return False
    else:
        return False

print(foo("mypass"))
print(foo("mylongpass"))
print(foo(456))