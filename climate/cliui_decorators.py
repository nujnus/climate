def edit_ui(**edit_kwargs):
  def edit_decorator(f):
    def wrapper(*args, **kwargs):
      edit_result = f(*args, **kwargs)
      obj = args[0]
      obj._edit_ui(content=edit_result, **edit_kwargs)
    return wrapper
  return edit_decorator

def read_ui(**read_kwargs):
  def read_decorator(f):
    def wrapper(*args, **kwargs):
      read_content = f(*args, **kwargs)
      obj = args[0]
      obj._read_ui(item = read_content, **read_kwargs)
    return wrapper
  return read_decorator


def confirm_ui(**confirm_kwargs):
  def confirm_decorator(f):
    def wrapper(*args, **kwargs):
      obj = args[0]
      obj._confirm_ui(f, args, kwargs, **confirm_kwargs)
    return wrapper
  return confirm_decorator

def list_ui(**menu_kwargs):
  def list_decorator(f):
    def wrapper(*args, **kwargs):
      List = f(*args, **kwargs)
      obj = args[0]
      obj._list_ui(List, **menu_kwargs)
    return wrapper
  return list_decorator


def checkbox_ui(**checkbox_kwargs):
  def checkbox_decorator(f):
    def wrapper(*args, **kwargs):
      List = f(*args, **kwargs)
      obj = args[0]
      obj._checkbox_ui(List, **checkbox_kwargs)
    return wrapper
  return checkbox_decorator

