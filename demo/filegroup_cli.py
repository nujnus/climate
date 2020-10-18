import requests
import json

from climate.cliui_decorators import edit_ui 
from climate.cliui_decorators import read_ui
from climate.cliui_decorators import confirm_ui
from climate.cliui_decorators import list_ui
from climate.cliui_decorators import checkbox_ui
from climate.cliui import BaseCliUI


class FileGroupCli(BaseCliUI):

# meta的部分
  baseurl = "http://127.0.0.1:8080"
  urls = {"update": "/app_demo_2EC6E023F4/api_FileGroup2Set/{}/",
          "get":    "/app_demo_2EC6E023F4/api_FileGroup2Set/{}/",
          "list":    "/app_demo_2EC6E023F4/api_FileGroup2Set/",
          "create":  "/app_demo_2EC6E023F4/api_FileGroup2Set/",
          "delete":  "/app_demo_2EC6E023F4/api_FileGroup2Set/{}",}

  template_for_create = """
{
    "description": "",
    "name": ""
}

"""
  def _get_token(self):
    username = "nujnus"
    password =  "123"
    
    url = r'http://localhost:8080/api/token/'
    data = {"username": username, "password": password}
    header = {"Content-Type": "application/json"}
    r = requests.post(url, headers=header, json=data)
    
    self.token_pair = json.loads(r.text)
    self.refresh_token = self.token_pair["refresh"]
    self.access_token = self.token_pair["access"]
    return  self.token_pair



  @list_ui(message="<menu_after_read>",
        update="update_option_selected",
        delete="delete_option_selected",
        back="back_option_selected")
  def menu_after_read(self):
    return []


  @list_ui(message="<menu_after_checked>", Back="back_option_selected")
  def menu_after_checked(self):
    return []

  @list_ui(message="<menu_after_start>",
        show_list="list_option_selected",
        create="create_option_selected",
        Back=None,
        item_selected="item_selected")
  def menu_after_start(self):
    return []


  @list_ui(message="<list>",
        out="list_out",
        checkbox="checkbox",
        back="back_option_selected",
        item_selected="item_selected"
  )
  def list(self):
    url = (self.baseurl+self.urls["list"])
    result = requests.get(url).json()[:5]
    return  [{"id": x["id"],  "group_name": x["name"]} for x in result]

  @checkbox_ui(message="<read>", items_checked="items_checked", nothing_checked="nothing_checked", out="checkbox_out")
  def list_checkbox(self):
    url = (self.baseurl+self.urls["list"])
    result = requests.get(url).json()[:5]
    return  [{"id": x["id"],  "group_name": x["name"]} for x in result]


  @read_ui(message="<read>", item_has_read="item_has_read", out="read_out")
  def read(self, id=None):
    url = (self.baseurl+self.urls["get"]).format(str(id))
    get_result = requests.get(url).json()
    get_result_string = json.dumps(get_result, indent=4, sort_keys=True)
    return get_result_string


  @edit_ui(message="<edit_for_update>", out="edit_out", edit_done="edit_done")
  def edit_for_update(self, content=None):
    assert type(content) == str, "type of content must be string"
    return content


  @confirm_ui(message="<update>", yes="update_committed", no="update_canceled")
  def update(self, id=None):
    url = (self.baseurl+self.urls["update"]).format(str(id))
    header = {"Content-Type": "application/json"}
    result = requests.put(url, headers=header, data=data).json()
    print(result)


  @confirm_ui(message="<delete>", yes="delete_committed", no="delete_canceled")
  def delete(self, id=None):
    url = (self.baseurl+self.urls["delete"]).format(str(id))
    result = requests.delete(url)
    print(str(result))

  @edit_ui(message="<edit_for_create>", out="edit_for_create_out", edit_done="edit_done")
  def edit_for_create(self, content=None):
    return content

  @confirm_ui(message="<create>", yes="create_committed", no="create_canceled")
  def create(self, data):
    url = (self.baseurl+self.urls["create"]).format(str(id))
    header = {"Content-Type": "application/json"}
    result = requests.post(url, headers=header, data=data).json()
    print(result)

