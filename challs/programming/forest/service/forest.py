#!/usr/bin/python

from keystone import *
from unicorn import *
from unicorn.x86_const import *
import random
import ctypes
import sys
from select import select

FLAG = file("flag").read()

registers = {'eax': UC_X86_REG_EAX, 'rax': UC_X86_REG_RAX,
             'ebx': UC_X86_REG_EBX, 'rbx': UC_X86_REG_RBX,
             'ecx': UC_X86_REG_ECX, 'rcx': UC_X86_REG_RCX,
             'edx': UC_X86_REG_EDX, 'rdx': UC_X86_REG_RDX,
             'esi': UC_X86_REG_ESI, 'rsi': UC_X86_REG_RSI,
             'edi': UC_X86_REG_EDI, 'rdi': UC_X86_REG_RDI
             }

e_reg = ['eax', 'ebx', 'ecx', 'edx', 'esi', 'edi']
r_reg = ['rax', 'rbx', 'rcx', 'rdx', 'rsi', 'rdi']

def pg_reg_reg(op, allowed_reg):
    register_dest = random.choice(allowed_reg)
    register_src = random.choice(allowed_reg)
    instruction = "%s %s, %s" % (op, register_dest, register_src)
    return (set([register_dest]), instruction)

def pg_reg_immediate(op, bitlen=24):
    register = random.choice(registers.keys())
    immediate = random.randrange(0, 2**bitlen)
    instruction = "%s %s, %s" % (op, register, hex(immediate).replace("L", ""))
    return (set([register]), instruction)

def g_increment():
    register = random.choice(registers.keys())
    instruction = "inc %s" % register
    return (set([register]), instruction)

def g_mov_immediate():
    return pg_reg_immediate("mov", bitlen=64)

def g_mov_reg():
    return pg_reg_reg("mov", random.choice([e_reg, r_reg]))

def g_xor_reg():
    return pg_reg_reg("xor", random.choice([e_reg, r_reg]))

def g_xor_immediate():
    return pg_reg_immediate("xor")

def g_add_reg():
    return pg_reg_reg("add", random.choice([e_reg, r_reg]))

def g_add_immediate():
    return pg_reg_immediate("add")

def g_sub_reg():
    return pg_reg_reg("sub", random.choice([e_reg, r_reg]))

def g_sub_immediate():
    return pg_reg_immediate("sub")

def generate_sample(num):
    cases = [g_increment, g_mov_immediate, g_mov_reg, g_xor_reg,
             g_xor_immediate, g_add_reg, g_add_immediate, g_sub_reg,
             g_sub_immediate]
    instructions = []
    registers = set()
    for i in range(num):
        register, instruction = random.choice(cases)()
        registers.update(register)
        instructions.append(instruction)
    return (registers, instructions)

def write(data, sep="\n"):
    sys.stdout.write(data + sep)
    sys.stdout.flush()

def readline(prompt):
    timeout = 10
    write(prompt, sep="")
    rlist, _, _ = select([sys.stdin], [], [], timeout)
    if rlist:
        s = sys.stdin.readline()
        return s
    else:
        write("Times up!")
        exit()

def emulate(bytecode, chosen_register):
    code = "".join(map(chr, bytecode))
    mu = Uc(UC_ARCH_X86, UC_MODE_64)
    ADDRESS = 0x1000000
    mu.mem_map(ADDRESS, 1 * 1024 * 1024)
    mu.mem_write(ADDRESS, code)
    mu.emu_start(ADDRESS, ADDRESS + len(code))
    reg = mu.reg_read(registers[chosen_register])
    return reg

def main():
    write("================================")
    write("Come closer and see")
    write("See into the trees")
    write("Find the girl")
    write("If you can")
    write("================================")
    write("Please solve assembly based captcha")
    write("Muahahahaahahaha")
    write("Assume all registers start with 0")
    write("Please present your answers as unsigned 64 bit decimal integers")

    ks = Ks(KS_ARCH_X86, KS_MODE_64)

    for i in range(100):
        write("==== %d/100 ====" % (i + 1))
        registers, instructions = generate_sample(5 + i)
        bytecode, count = ks.asm("\n".join(instructions))
        chosen_register = random.choice(list(registers))
        result = emulate(bytecode, chosen_register)
        result = ctypes.c_uint64(result).value
        write("\n".join(instructions))
        data = readline("%s: " % chosen_register)

        try:
            submission = int(data)
        except:
            write("Bad input")
            exit()

        if submission == result:
            write("Correct!")
        else:
            write("Wrong!")
            exit()

    write("Congratulations, here's your flag: %s" % FLAG)

if __name__ == '__main__':
    main()
