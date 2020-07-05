from rest import pi_rest
from rest.pi_rest import HandlerException

@pi_rest.json_return
def test_json_return(text: str):
  return {'result': text}

@pi_rest.exception_handler(exceptions=HandlerException)
def test_exception_handler(text: str):
  if not isinstance(text, str):
      raise HandlerException(message="Invalid parameter")
  else:
    return "TEXT is String"

@pi_rest.exception_handler(exceptions=HandlerException, f_return=lambda text : f"Exception {text}", params=["rendering"])
def test_exception_handler_with_return_func(text: str):
  if not isinstance(text, str):
      raise HandlerException(message="Invalid parameter")
  else:
    return "TEXT is String"

@pi_rest.exception_handler(exceptions=HandlerException, f_return=lambda text : f"Exception {text}", params=["rendering"])
@pi_rest.json_return
def test_compine_handler_and_json_return(text: str):
  if not isinstance(text, str):
      raise HandlerException(message="Invalid parameter")
  else:
    return {"result": "A JSON STRING"}

if __name__ == '__main__':
    json = test_json_return("TEST JSON RETURN")
    print(json)
    print(f"ASSERT AS STRING {isinstance(json, (str,))}")
    print(f"ASSERT AS DICT {isinstance(json, (dict,))}\n")

    handler = test_exception_handler(None)
    print(handler)
    print(f"ASSERT AS STRING {isinstance(handler, (str,))}")
    print(f"ASSERT AS EXCEPTION {isinstance(json, (HandlerException,))}\n")

    handler_with_return_func = test_exception_handler_with_return_func(None)
    print(handler_with_return_func)
    print(f"ASSERT AS STRING {isinstance(handler_with_return_func, (str,))}")
    print(f"ASSERT AS EXCEPTION {isinstance(handler_with_return_func, (HandlerException,))}\n")

    handler_compine_return_json = test_compine_handler_and_json_return("")
    print(handler_compine_return_json)
    print(f"ASSERT AS STRING {isinstance(handler_compine_return_json, (str,))}")
    print(f"ASSERT AS DICT {isinstance(handler_compine_return_json, (dict,))}\n")

    handler_compine_return_json = test_compine_handler_and_json_return(None)
    print(handler_compine_return_json)
    print(f"ASSERT AS STRING {isinstance(handler_compine_return_json, (str,))}")
    print(f"ASSERT AS DICT {isinstance(handler_compine_return_json, (dict,))}")