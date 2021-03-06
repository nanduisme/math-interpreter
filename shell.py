import json
import os

from mathew.lexer import Lexer
from mathew.parser import Parser
from mathew.interpreter import Interpreter


def run(text):
    tokens = Lexer(text).make_toks()
    if tokens.error:
        return tokens

    nodes = Parser(tokens.node).parser()
    if nodes.error:
        return nodes

    res = Interpreter().visit(nodes.node)
    if not res.error:
        with open("info.json", "w") as f:
            json.dump({"r": res.node}, f)

    return res


if __name__ == "__main__":
    os.system("clear|cls")
    print("Mathew - Math interpreter\n")

    while True:
        text = input("> ").strip()
        if not text:
            continue

        if text in {"clear", "c"}:
            os.system("clear|cls")
            print("Mathew - Math interpreter\n")
            continue

        elif text in {"exit", "quit", "q"}:
            os.system("clear|cls")
            break

        res = run(text)

        if res.error:
            print(res.error, "\n")
            continue

        print(res.node, "\n")
