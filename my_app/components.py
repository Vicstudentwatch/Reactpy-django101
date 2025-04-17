from reactpy import component, html

@component
def hello_world(user:str):
  return html.h1(f"Hello {user}")