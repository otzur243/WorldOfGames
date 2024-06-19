from bs4 import BeautifulSoup
from urllib3 import PoolManager
from Utils import BAD_RETURN_CODE


# test our web service.
# get the application URL as an input,
# open a browser to that URL,
# select the score element in our web page,
# check that it is a number between 0 and 1000 and return a boolean value if it’s true or not
def test_scores_service(url):
    try:
        response = PoolManager().request("GET", url)
        if response.status != 200:
            raise (BaseException(response.reason))
        span = BeautifulSoup(response.data, "html.parser").find("div", id="score")
        return span and span.get_text().isdigit() and 0 <= int(span.get_text()) <= 1000
    except BaseException as e:
        print(f"\nAn error occurred: {e}")
        return False


# call our tests function.
# The main function will return -1 as an OS exit code if the tests failed and 0 if they passed.
def main_function():
    print("\nTest Execution Started")
    is_pass = test_scores_service('http://127.0.0.1:5000')
    if is_pass:
        print("\nSUCCESS\n\nTest Execution Finished")
        return 0
    print("\nFAILED\n\nTest Execution Finished")
    return BAD_RETURN_CODE


print(main_function())
