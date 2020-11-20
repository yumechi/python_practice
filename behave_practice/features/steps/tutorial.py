from behave import given, when, then, step


@given("we have behave installed")
def installed(context):
    pass


@when("we implement a test")
def a_test(context):
    assert True is not False


@then("behave will test it for us!")
def it_for_us(context):
    assert context.failed is False


@step("we enjoy test!")
def enjoy_test(context):
    assert bool(42) is not False
    assert bool(0) is False
