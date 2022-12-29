import ast as A
from typing import List
from hashlib import sha256 as _hash

def sha256(x: str):
  return _hash(x.encode()).hexdigest()

def get_code_section(node: A.AST, code_lines: List[str]):
  """generic function to return the code section for a node"""
  if type(code_lines) == str:
    code_lines = code_lines.splitlines()
  else:
    assert type(code_lines) == list and type(code_lines[0]) == str
  sl, so, el, eo = node.lineno, node.col_offset, node.end_lineno, node.end_col_offset
  code = ""
  if sl == el:
    code = code_lines[sl-1][so:eo]
  else:
    for i in range(sl - 1, el, 1):
      if i == sl - 1:
        code += code_lines[i][so:]
      elif i == el - 1:
        code += "\n" + code_lines[i][:eo]
      else:
        code += "\n" + code_lines[i]
  return code

