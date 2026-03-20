import ast
import operator as op
import math

# /c:/Users/mavar/Desktop/slejndro/operadores/hola.py
# Calculadora simple (entrada de expresiones)

# Operadores permitidos
BINOPS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Mod: op.mod,
    ast.Pow: op.pow,
    ast.FloorDiv: op.floordiv,
}
UNARYOPS = {ast.UAdd: lambda x: x, ast.USub: op.neg}

# Funciones y constantes permitidas
NAMES = {
    "pi": math.pi,
    "e": math.e,
    "tau": math.tau,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "sqrt": math.sqrt,
    "log": math.log,
    "log10": math.log10,
    "exp": math.exp,
    "abs": abs,
    "round": round,
    "fact": math.factorial,
}

def eval_node(node):
    if isinstance(node, ast.Expression):
        return eval_node(node.body)
    if isinstance(node, ast.Constant):  # numbers in Python 3.8+
        if isinstance(node.value, (int, float)):
            return node.value
        raise ValueError("Valor no numérico")
    if isinstance(node, ast.BinOp):
        left = eval_node(node.left)
        right = eval_node(node.right)
        op_type = type(node.op)
        if op_type in BINOPS:
            return BINOPS[op_type](left, right)
        raise ValueError(f"Operador no permitido: {op_type}")
    if isinstance(node, ast.UnaryOp):
        operand = eval_node(node.operand)
        op_type = type(node.op)
        if op_type in UNARYOPS:
            return UNARYOPS[op_type](operand)
        raise ValueError("Operador unario no permitido")
    if isinstance(node, ast.Call):
        if not isinstance(node.func, ast.Name):
            raise ValueError("Llamada inválida")
        fname = node.func.id
        if fname not in NAMES or not callable(NAMES[fname]):
            raise ValueError(f"Función no permitida: {fname}")
        args = [eval_node(a) for a in node.args]
        return NAMES[fname](*args)
    if isinstance(node, ast.Name):
        if node.id in NAMES and not callable(NAMES[node.id]):
            return NAMES[node.id]
        raise ValueError(f"Nombre no permitido: {node.id}")
    raise ValueError(f"Nodo no permitido: {type(node)}")

def evaluate(expr):
    expr = expr.strip()
    if not expr:
        raise ValueError("Expresión vacía")
    tree = ast.parse(expr, mode="eval")
    return eval_node(tree)

def print_help():
    print("Calculadora: escribe expresiones aritméticas.")
    print("Operadores: + - * / ** % //  (paréntesis soportados)")
    print("Funciones: sin, cos, tan, sqrt, log, log10, exp, abs, round, fact")
    print("Constantes: pi, e, tau")
    print("Comandos: 'q', 'quit', 'exit' para salir; 'h' o 'help' para ayuda.")

def main():
    print("Calculadora (ayuda: 'h' o 'help', salir: 'q')")
    while True:
        try:
            s = input(">>> ").strip()
            if not s:
                continue
            if s.lower() in {"q", "quit", "exit"}:
                break
            if s.lower() in {"h", "help"}:
                print_help()
                continue
            result = evaluate(s)
            print(result)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()