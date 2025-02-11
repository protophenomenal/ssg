
from textnode import *

dummy_test = TextNode("Testing text nodes", TextType.CODE, "https://www.rewers.xyz")

def main():
    return print(f"{dummy_test.__repr__()}")

main()