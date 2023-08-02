from scanner import Scanner
from tokens import TokenType

class Parser:

    def __init__(self, text) -> None:
        self.curr = None
        self.scanner = Scanner(text)
        self.advance()

    def advance(self):
        self.curr = self.scanner.scan()
    
    def parse(self) -> bool:
        e = self.expr()
        if self.curr is not None:
            return False
        return e
    
    def expr(self) -> bool:
        if self.curr is None:
            return False
        if not self.term():
            return False
        if self.curr is None:
            return True
        if self.curr.token_type in (TokenType.AND, TokenType.OR):
            self.advance()
            return self.expr()
        return True

    def term(self) -> bool:
        if self.curr is None:
            return False
        if self.curr.token_type in (TokenType.TRUE, TokenType.FALSE):
            self.advance()
            return True
        if self.curr.token_type == TokenType.NOT:
            self.advance()
            return self.term()
        if self.curr.token_type == TokenType.LPAREN:
            self.advance()
            if not self.expr():
                return False
            if self.curr is None:
                return False
            if self.curr.token_type != TokenType.RPAREN:
                return False
            self.advance()
            return True
        return False

        