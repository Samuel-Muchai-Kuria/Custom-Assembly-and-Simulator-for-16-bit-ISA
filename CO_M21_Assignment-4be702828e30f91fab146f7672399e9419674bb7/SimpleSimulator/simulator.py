#keep this file
#co assembler
#groupwork


import sys

Inst = sys.stdin.read()

typeofopcode = {"ty_A":["00000","00001","00110","01010","01011","01100"],
                "ty_B":["00010","01000","01001"],
                "ty_C":["00011","00111","01101","01110"],
                "ty_D":["00100","00101",],
                "ty_E":["01111","10000","10001","10010"],
                "ty_F":"10011"}

register_file= {"000":0,
       "001":0,
       "010":0,
       "011":0,
       "100":0,
       "101":0,
       "110":0,
       "111":0}
MEM=[]
instr=[]
pc=[]
def initialization():
        for line in Inst:
                instruction =[]
                opc=line[:5] # list should contain first five values
                if opc in typeofopcode["ty_A"]: #checks if its a typeA to know how many arg it will take
                        rega=line[7:10]
                        regb=line[10:13]
                        regc=line[13:16]
                  
                        instruction.append(opc, rega, regb, regc)
                        MEM.append(instruction)
                         #if opc is intype_A[0]:# add
                       # register_file[rega]=register_file[regb]+ register_file[regc]
                if opc in typeofopcode["ty_B"]:
                        rega=line[7:10]
                        imm_value=line[9:16]

                        instruction.append(opc,rega,imm_value)
                        MEM.append(instruction)
                
                if opc in typeofopcode["ty_C"]:
                        rega=line[11:13]
                        regb=line[14:16]
                        unused=line[6:10]

                        instruction.append(opc,unused,rega,regb)
                        MEM.append(instruction)

                if opc in typeofopcode["ty_D"]:
                        rega=line[6:8]
                        mem_address=line[9:16]

                        instruction.append(opc,rega,mem_address)
                        MEM.append(instruction)
                if opc in typeofopcode["ty_E"]:
                        unused=line[6:8]
                        mem_address=line[9:16]

                        instruction.append(opc,unused,mem_address)
                        MEM.append(instruction)

                if opc in typeofopcode["ty_F"]:
                        unused=line[6:16]

                        instruction.append(opc,unused)
                        MEM.append(instruction)

def execute(instruction):
        op_code=instruction[0]
        opcodeA=typeofopcode["ty_A"]
        opcodeB=typeofopcode["ty_B"]
        opcodeC=typeofopcode["ty_C"]
        opcodeD=typeofopcode["ty_D"]
        opcodeE=typeofopcode["ty_E"]
        opcodeF=typeofopcode["ty_F"]
        if op_code is opcodeA[0]: #add
                register_file[instruction[1]]=register_file[instruction[2]] + register_file[instruction[3]]
        
        if op_code is opcodeA[1]: #sub
                register_file[instruction[1]]=register_file[instruction[2]] - register_file[instruction[3]]
        
        if op_code is opcodeA[2]: #mul
                register_file[instruction[1]]=register_file[instruction[2]] * register_file[instruction[3]]

        if op_code is opcodeA[3]: #xor bitwise
                register_file[instruction[1]]=register_file[instruction[2]] ^ register_file[instruction[3]]


        if op_code is opcodeA[4]: #or
                register_file[instruction[1]]=register_file[instruction[2]] | register_file[instruction[3]]

        if op_code is opcodeA[5]: #and
                register_file[instruction[1]]=register_file[instruction[2]] & register_file[instruction[3]]

        if op_code is opcodeB[0]: #move imm
                register_file[instruction[1]]=imm_value 

        if op_code is opcodeB[1]: #right shift 
                register_file[instruction[1]]=register_file[instruction[1]]>> imm_value # need to check

        
        if op_code is opcodeB[2]: #left shift
                register_file[instruction[1]]=register_file[instruction[1]]<< imm_value #need to check

        if op_code is opcodeC[0]: # move registers
                register_file[instruction[1]]=register_file[instruction[2]]
        
        if op_code is opcodeC[1]: #division
                register_file["000"]=register_file[instruction[1]] / register_file[instruction[2]] # edit needed to store quotent
                register_file["001"]=register_file[instruction[1]] // register_file[instruction[2]] #edit needed to store remainder
        if op_code is opcodeC[2]: #invert
                register_file[instruction[1]]= ~ register_file[instruction[2]]

        if op_code is opcodeC[3]: #comparator and set the flag register
                if register_file[instruction[1]]==register_file[instruction[2]]:
                        register_file["111"] += 1 #flag register

        if op_code is opcodeD[0]: #load
                register_file[instruction[1]]= mem_address # need to access mem_address from first function

        if op_code is opcodeD[1]: #store
                mem_address=register_file[instruction[1]] #check mem_address again
        
        if op_code is opcodeE[0]: #jump unconditional to mem_adrress same as memory address
                pc =get_decimal(mem_address)

        if op_code is opcodeE[1]: #jump if less than Jump to mem_addr if the less than flag is set (less than flag = 1),
                pc= get_decimal(mem_address)                                    # where mem_addr is a memory
                                                         
        if op_code is opcodeE[2]: #jump if greater than
                pc=get_decimal(mem_address)
        if op_code is opcodeE[3]: #jump if equal 
                pc =get_decimal(mem_address)
        if op_code is opcodeF: #halt instruction
               exit()


def registerfile(register_file):
        #regfile=register_file[]
        for reg in register_file:
                if register_file[reg] is "000":
                        print(register_file[reg])

                if register_file[reg] is "0001":
                        print(register_file[reg])

                if register_file[reg] is "010":
                        print(register_file[reg])

                if register_file[reg] is "011":
                        print(register_file[reg])

                if register_file[reg] is "100":
                        print(register_file[reg])

                if register_file[reg] is "101":
                        print(register_file[reg])
                        
                if register_file[reg] is "110":
                        print(register_file[reg])

                if register_file[reg] is "111": #flag
                        print(register_file[reg])

def engine():
        pass