import os
from astea import Astea, IndexTypes

folder, file = os.path.split(__file__)
test_file = os.path.join(folder, "test.py")
print(test_file)

tea = Astea(fname = test_file)
print(tea)
print(len(tea.index) == 1, len(tea.index))

foo = tea.index[0]
print(foo)
print(len(foo.index) == 3, foo.index, )
print(foo.docstring() == "Foo doc", foo.docstring())
