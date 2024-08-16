from flytekit import task, dynamic, workflow
from dataclasses import dataclass
from mashumaro.mixins.json import DataClassJSONMixin


@dataclass
class IntWrapper(DataClassJSONMixin):
    x: int

@task
def get_int() -> int:
    return 3

@task
def get_wrapped_int() -> IntWrapper:
    return IntWrapper(x=3)

@task 
def sum_list(input_list: list[int]) -> int:
    return sum(input_list)


@dataclass
class StrWrapper(DataClassJSONMixin):
    x: str

@task
def get_str() -> str:
    return "5"

@task
def get_wrapped_str() -> StrWrapper:
    return StrWrapper(x="3")

@task 
def concat_list(input_list: list[str]) -> str:
    return "".join(input_list)



@workflow
def convert_list_workflow1() -> int:
    """Here's a simple workflow that takes a list of strings and returns a dataclass with that list."""
    promised_int = get_int()
    joined_list = [4, promised_int]
    return sum_list(input_list=joined_list)

@workflow
def convert_list_workflow2() -> int:
    wrapped_int = get_wrapped_int()
    joined_list = [4, wrapped_int.x]
    return sum_list(input_list=joined_list)

@workflow
def convert_list_workflow3() -> str:
    """Here's a simple workflow that takes a list of strings and returns a dataclass with that list."""
    promised_str = get_str()
    joined_list = ["4", promised_str]
    return concat_list(input_list=joined_list)

@workflow
def convert_list_workflow4() -> str:
    wrapped_str = get_wrapped_str()
    joined_list = ["4", wrapped_str.x]
    return concat_list(input_list=joined_list)


if __name__ == "__main__":
    print("Run 1")
    print(convert_list_workflow1())
    print("Run 2")
    print(convert_list_workflow2())
    print("Run 3")
    print(convert_list_workflow3())
    print("Run 4")
    print(convert_list_workflow4())
