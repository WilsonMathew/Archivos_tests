from scanner import Scanner
from expr_parser import Parser

def main():
    correct = ["true", "false", "true and false", "false or true", "(true)", "not (true)"]
    incorrect = ["true and", "false or", "(true", ")","()","true and not", "false or not"]
    inputs = correct + incorrect

    for input_text in inputs:
        s = Scanner(input_text)
        tokens = s.scanAll()
        print(tokens)

        p = Parser(input_text)
        ok = p.parse()
        if ok: 
            print(f'"{input_text}" is a correct boolean expression')
        else:
            print(f'"{input_text}" is NOT a correct boolean expression')
        print()


    # Test for lexical analyzer
    #s = Scanner("true or false")
    #tokens = s.scanAll()
    #print(tokens)

if __name__ == '__main__':
    main()