import ast
import builtins
import types

class CallCollector(ast.NodeVisitor):
    def __init__(self):
        self.calls = []
        self._current = []
        self._in_call = False

    def visit_Call(self, node):
        self._current = []
        self._in_call = True
        self.generic_visit(node)

    def visit_Attribute(self, node):
        if self._in_call:
            self._current.append(node.attr)
        self.generic_visit(node)

    def visit_Name(self, node):
        if self._in_call:
            self._current.append(node.id)
            self.calls.append('.'.join(self._current[::-1]))
            # Reset the state
            self._current = []
            self._in_call = False
        self.generic_visit(node)


f = open("Analysis/parse.py",'r')
f2 = open("Analysis/inbuilt_functions.txt",'r')
tree = ast.parse(f.read())
cc = CallCollector()
cc.visit(tree)
l = cc.calls
dictionary = {i:l.count(i) for i in set(l)}
builtin_function_names = []

for line in f2.readlines():
    builtin_function_names.append(line[:-1])
# print(builtin_function_names)

for key in dictionary.copy():
    if(key[key.rfind('.')+1:] in builtin_function_names or key in builtin_function_names):
        del dictionary[key]
# print(builtin_function_names)
# print(builtins.dict_keys())
dictionary = dict(sorted(dictionary.items(), key=lambda item: -item[1]))
print(dictionary)
