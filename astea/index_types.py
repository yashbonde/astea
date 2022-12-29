import ast as A
from enum import Enum

class IndexTypes(Enum):
  """
  This is our list of index types, these can be used to search through things in the AST. Here's some description on
  what each of these mean. There are a few special ones for convinience:
  - FILE: which means that the current location is the file itself, also can be considered as ast.Module
  - DOCSTRING: which is a special type of expression that is a docstring, is defined to use a different parsing logic
  """
  FUNCTION = A.FunctionDef
  CLASS = A.ClassDef
  VARIABLE = A.Name
  IMPORT = A.Import
  IMPORT_FROM = A.ImportFrom
  ASSIGN = A.Assign
  EXPRESSION = A.Expr
  IF = A.If
  FILE = "file"
  DOCSTRING = "__doc__"

  def all():
    """returns all the valid index types"""
    return [
      IndexTypes.FUNCTION,
      IndexTypes.CLASS,
      IndexTypes.VARIABLE,
      IndexTypes.IMPORT,
      IndexTypes.IMPORT_FROM,
      IndexTypes.ASSIGN,
      IndexTypes.EXPRESSION,
      IndexTypes.IF,
      IndexTypes.FILE
    ]
