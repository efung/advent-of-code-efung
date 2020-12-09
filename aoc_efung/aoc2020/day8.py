from aocd import data
import re


def cpu(instrs):
    pc = 0
    acc = 0
    executed_addresses = set()

    while (pc != len(instrs)) and (pc not in executed_addresses):
        # Fetch
        instr = instrs[pc]
        # Decode
        m = re.match('(\w+) ([+-]\d+)', instr)
        op = m.group(1)
        arg = int(m.group(2))
        # Execute
        executed_addresses.add(pc)
        if op == 'nop':
            pc += 1
        elif op == 'acc':
            acc += arg
            pc += 1
        elif op == 'jmp':
            pc += arg

    #print("Stopping when pc=={}, acc=={}, executed_addresses={}".format(pc, acc, executed_addresses))

    if (pc == len(instrs)):
        return ('term', acc)
    else:
        return ('infloop', acc)


def part_a(data):
    instrs = [s for s in data.split('\n') if s != '']
    (reason, acc) = cpu(instrs)
    assert reason == 'infloop'
    return str(acc)

def part_b(data):
    instrs = [s for s in data.split('\n') if s != '']
    for pc in range(0, len(instrs)):
        if instrs[pc].startswith('jmp'):
            instrs_new = instrs.copy()
            instrs_new[pc] = instrs_new[pc].replace('jmp', 'nop')
            (reason, acc) = cpu(instrs_new)
            if reason == 'term':
                #print("Repair at pc={} changing jmp to nop".format(pc))
                return str(acc)

    for pc in range(0, len(instrs)):
        if instrs[pc].startswith('nop'):
            instrs_new = instrs.copy()
            instrs_new[pc] = instrs_new[pc].replace('nop', 'jmp')
            (reason, acc) = cpu(instrs_new)
            if reason == 'term':
                #print("Repair at pc={} changing nop to jmp".format(pc))
                return str(acc)


test_data = """\
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""

if __name__ == "__main__":
    assert part_a(test_data) == "5"
    assert part_b(test_data) == "8"
    print(part_a(data))
    print(part_b(data))
