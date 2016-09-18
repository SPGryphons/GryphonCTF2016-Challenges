# Bin-2
The source code is in generate folder

## Question Text
Patch me if you can!
It's easy.

## Setup Guide
1. Compile from the source code
2. Pull the exe file out

## Solution
1. Search for important strings such as 'QR demands'

2.Put important breakpoints at the bolded addresses. Either nop it or make the flag not jumpable.

**002E2152**  |. /75 64         jnz short ConsoleA.002E21B8
002E2154  |. |83FF 0D       cmp edi,0xD
**002E2157**  |. |72 5F         jb short ConsoleA.002E21B8
002E2159  |. |77 5D         ja short ConsoleA.002E21B8
002E215B  |. |BA D0953000   mov edx,ConsoleA.003095D0                ;  Congratz M8 here's your flag
002E2160  |. |E8 1B0D0000   call ConsoleA.std::operator<<<std::char_>
002E2165  |. |50            push eax
002E2166  |. |E8 05100000   call ConsoleA.std::endl<char,std::char_t>
002E216B  |. |0F2805 A09630>movaps xmm0,dqword ptr ds:[_xmm__GetCurr>
002E2172  |. |8D55 D4       lea edx,[local.11]
002E2175  |. |8D4D BC       lea ecx,[local.17]
002E2178  |. |C745 E4 04000>mov [local.7],_Init_thread_epochointersr>
002E217F  |. |0F1145 D4     movups dqword ptr ss:[ebp-0x2C],xmm0
002E2183  |. |C745 E8 03000>mov [local.6],0x3
002E218A  |. |C745 EC 03000>mov [local.5],0x3
002E2191  |. |E8 7AFEFFFF   call ConsoleA.decode_initializeroy_handl>
002E2196  |. |8BD1          mov edx,ecx
002E2198  |. |E8 83100000   call ConsoleA.std::operator<<<char,std::>
002E219D  |. |50            push eax
002E219E  |. |E8 CD0F0000   call ConsoleA.std::endl<char,std::char_t>
002E21A3  |. |BA F0953000   mov edx,ConsoleA.003095F0                ;  Please encapsulate the flag with GCTF{}
002E21A8  |. |E8 D30C0000   call ConsoleA.std::operator<<<std::char_>
002E21AD  |. |50            push eax
002E21AE  |. |E8 BD0F0000   call ConsoleA.std::endl<char,std::char_t>
002E21B3  |. |83C4 0C       add esp,0xC
002E21B6  |. |EB 13         jmp short ConsoleA.002E21CB
002E21B8  |> \BA 18963000   mov edx,ConsoleA.00309618                ;  oops,try harder? you can do it? believe in yourself? just do it? oops? oops? oops?

3. Get the flag and encapsulate it!