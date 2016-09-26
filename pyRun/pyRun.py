# coding=utf-8


what_to_execute = {
    "instructions": [("LOAD_VALUE", 0),
                     ("STORE_NAME", 0),
                     ("LOAD_VALUE", 1),
                     ("STORE_NAME", 1),
                     ("LOAD_NAME", 0),
                     ("LOAD_NAME", 1),
                     ("ADD_TWO_VALUES", None),
                     ("PRINT_ANSWER", None),
    ],
    "numbers": [1, 2],
    "names": ['a', 'b']
}


class Interpreter(object):

    def __init__(self):
        self.stack = []
        self.environment = {}

    def STORE_NAME(self, name):
        val = self.stack.pop()
        self.environment[name] = val

    def LOAD_NAME(self, name):
        val = self.environment[name]
        self.stack.append(val)

    def LOAD_VALUE(self, number):
        self.stack.append(number)

    def PRINT_ANSWER(self):
        answer = self.stack.pop()
        print(answer)

    def ADD_TWO_VALUES(self):
        first_num = self.stack.pop()
        second_num = self.stack.pop()
        total = first_num + second_num
        self.stack.append(total)

    def parse_argument(self, instruction, argument, what_to_execute):
        numbers = ["LOAD_VALUE"]
        names = ["LOAD_NAME", "STORE_NAME"]

        arg = argument
        if instruction in numbers:
            arg = what_to_execute['numbers'][argument]
        elif instruction in names:
            arg = what_to_execute['names'][argument]

        return arg

    def run_code(self, what_to_execute):
        # 指令列表
        instructions = what_to_execute['instructions']

        for each_step in instructions:
            instruction, arg = each_step
            arg = self.parse_argument(instruction, arg, what_to_execute)

            if instruction == 'LOAD_VALUE':
                self.LOAD_VALUE(arg)

            elif instruction == 'ADD_TWO_VALUES':
                self.ADD_TWO_VALUES()

            elif instruction == 'PRINT_ANSWER':
                self.PRINT_ANSWER()

            elif instruction == "STORE_NAME":
                self.STORE_NAME(arg)

            elif instruction == "LOAD_NAME":
                self.LOAD_NAME(arg)

    def execute(self, what_to_execute):
        instructions = what_to_execute["instructions"]
        for each_step in instructions:
            instruction, arg = each_step
            arg = self.parse_argument(instruction, arg, what_to_execute)
            bytecode_method = getattr(self, instruction)
            if arg is None:
                bytecode_method()
            else:
                bytecode_method(arg)


# run
interpreter = Interpreter()
interpreter.execute(what_to_execute)
