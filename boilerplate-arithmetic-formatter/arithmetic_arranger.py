def arithmetic_arranger(problems, answers=False):
    # Verifique se há muitos problemas fornecidos à função. O limite é cinco.
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = ''
    # Lista de lista, contendo os operandos e o operador de cada problema.
    splitted = [problem.split(' ') for problem in problems]
    # Lista contendo os primeiros operandos
    first_operand = [problem[0] for problem in splitted]
    # Lista com os operadores
    operator = [problem[1] for problem in splitted]
    # Lista com os segundos operandos
    second_operand = [problem[2] for problem in splitted]
    # Verifica se o primeiro operando é o maior numero do problema e retorna True, caso contrario False
    longest = [True if len(first) >= len(second) else False for first, second in zip(first_operand, second_operand)]

    # Os operadores apropriados que a função aceitará são adição e subtração. A multiplicação e a divisão retornarão um
    # erro
    if '*' in operator or '/' in operator:
        return "Error: Operator must be '+' or '-'."

    # Verifica se cada número (operando) contém apenas dígitos
    if (not all(el.isdigit() for el in first_operand)) or (not all(el.isdigit() for el in second_operand)):
        return "Error: Numbers must only contain digits."

    # Verifica se cada operando possui no máximo quatro dígitos de largura.
    if (not all(len(el) <= 4 for el in first_operand)) or (not all(len(el) <= 4 for el in second_operand)):
        return "Error: Numbers cannot be more than four digits."
    """
    Formata os problemas passados seguindo as seguintes regras:
    - Deve haver um único espaço entre o operador e o maior dos dois operandos, o operador estará na mesma linha do 
    segundo operando, ambos os operandos estarão na mesma ordem fornecida (o primeiro será o de cima e o segundo será o 
    baixo).
    - Os números devem ser alinhados à direita.
    - Deve haver quatro espaços entre cada problema.
    - Deve haver traços na parte inferior de cada problema. Os traços devem percorrer toda a extensão de cada problema 
    individualmente.
    """
    # Formata o primeiro operando de cada problema
    for i, el in enumerate(first_operand):
        if longest[i]:
            arranged_problems = arranged_problems + el.rjust(len(el) + 2, " ") + (
                ' ' * 4 if i < len(first_operand) - 1 else '')
        else:
            arranged_problems = arranged_problems + el.rjust(len(second_operand[i]) + 2, " ") + (
                ' ' * 4 if i < len(first_operand) - 1 else '')

    arranged_problems = arranged_problems + '\n'

    # Formata o segundo operando de cada problema justamente com o operador
    for i, el in enumerate(second_operand):
        if longest[i]:
            arranged_problems = arranged_problems + operator[i] + ' ' + el.rjust(len(first_operand[i]), " ") + (
                ' ' * 4 if i < len(second_operand) - 1 else '')
        else:
            arranged_problems = arranged_problems + operator[i] + ' ' + el + (
                ' ' * 4 if i < len(second_operand) - 1 else '')

    arranged_problems = arranged_problems + '\n'

    # Formata os traços abaixo de cada problema
    for i, _ in enumerate(problems):
        if longest[i]:
            arranged_problems = arranged_problems + '-' * (2 + len(first_operand[i])) + (
                ' ' * 4 if i < len(problems) - 1 else '')
        else:
            arranged_problems = arranged_problems + '-' * (2 + len(second_operand[i])) + (
                ' ' * 4 if i < len(problems) - 1 else '')

    # Se answers for True, então o resultado de cada problema é calculado e adicionado ao arranjo dos problemas
    # formatado.
    if answers:
        arranged_problems = arranged_problems + '\n'
        results = [str(int(x) + int(y)) if '+' == op else str(int(x) - int(y)) for op, x, y in
                   zip(operator, first_operand, second_operand)]

        for i, el in enumerate(results):
            if longest[i]:
                arranged_problems = arranged_problems + el.rjust(2 + len(first_operand[i]), " ") + (
                    ' ' * 4 if i < len(results) - 1 else '')
            else:
                arranged_problems = arranged_problems + el.rjust(2 + len(second_operand[i]), " ") + (
                    ' ' * 4 if i < len(results) - 1 else '')

    return arranged_problems
