def to_camel_case(name: str) -> str:
    return ''.join([i.capitalize() for i in name.split('_')])


if __name__ == '__main__':
    assert to_camel_case("my_function_name") == "MyFunctionName"
    assert to_camel_case("i_phone") == "IPhone"
    assert to_camel_case("this_function_is_empty") == "ThisFunctionIsEmpty"
    assert to_camel_case("name") == "Name"
    print("OK")
