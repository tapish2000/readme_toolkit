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

f = open("./input.py",'r')
tree = ast.parse(f.read())
cc = CallCollector()
cc.visit(tree)
l = cc.calls
l = set(l)
builtin_function_names = [name for name, obj in vars(builtins).items() 
                          if isinstance(obj, types.BuiltinFunctionType)]
# ans = []
# for name in l:
#     if(name not in builtin_function_names):
#         ans.append(name)
print(builtin_function_names)
# print(builtins.dict_keys())