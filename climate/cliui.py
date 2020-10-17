import inquirer
import json

class BaseCliUI(object):

  def _edit_ui(self, message="?", out=None, content="", edit_done="edit_done"):
    edit_questions = [inquirer.Editor('edit', message=message, default=content)] 
    answers = inquirer.prompt(edit_questions)
    data = answers["edit"]
    assert out != None, "<parameter:out> is required"
    self.store[out] = data
    getattr(self, edit_done)()


  def _list_ui(self, items, message="?", out=None, item_selected="item_selected", **kwargs):
    choices = [ key for key  in kwargs]
    list_and_choices = items + choices
    questions = [
      inquirer.List('menu',
                    message=message,
                    choices= list_and_choices,
                    carousel=True  #这个不错
                ),]
    answers = inquirer.prompt(questions)
    menu_option_trigger_dict = kwargs
    selected = answers['menu']
    if selected in choices:
      trigger = menu_option_trigger_dict[selected]
      if trigger == None:
        return 0
      else:
        getattr(self, trigger)()
    else: #for items:
      assert out != None, "<parameter:out> is required"
      self.store[out] = selected
      trigger = item_selected
      getattr(self, trigger)()


  def _checkbox_ui(self, items, message="?", out=None, items_checked="items_checked", nothing_checked="nothing_checked"):
    questions = [
      inquirer.Checkbox('checkbox',
               message=message,
               choices=items, 
      ),]
    checkbox_answers = inquirer.prompt(questions)
    if checkbox_answers["checkbox"] == []:
      getattr(self, nothing_checked)()
    else:
      self.store[out] = checkbox_answers["checkbox"]
      getattr(self, items_checked)()


  def _confirm_ui(self, task_function, args, kwargs, message="?", yes="committed", no="canceled"):
    confirm_questions = [inquirer.Confirm('yesorno', message=message),]
    confirm = inquirer.prompt(confirm_questions)

    if confirm["yesorno"]:
      task_function(*args, **kwargs)
      getattr(self, yes)()
    else:
      getattr(self, no)()


  def _read_ui(self, message="?", out=None, item="", item_has_read="item_has_read"):
    assert out != None, "<parameter:out> is required"
    print(message)
    print(item)
    self.store[out] = item 
    self.item_has_read()
