def test_function():
    global inner_function

    def inner_function():
        print(f"Я в области видимости функции test_function")

    return inner_function()


test_function()

inner_function()
