
def labo1():
        from collections import Counter
        print("Introducir texto a descifrar")
        texto ="RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE. AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE"
        Alfabeto="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        Frecuencia="EAOLSNDRUITCPMYQBHGFVJÑZXKW"
        contador = Counter(texto) #para la frecuencia
        apariciones=dict()
        for caracter in Alfabeto: #para que no aparezcan . , ...
            apariciones[caracter]=contador[caracter]
    
        apariciones_ordenadas=dict(sorted(apariciones.items(), key=lambda item:item[1],reverse=True)) #apariciones de las letras en orden decreciente
        keys=apariciones_ordenadas.keys()
        #print(len(keys))
        Frecuencia_texto=""
        for pos in range(len(keys)):
            Frecuencia_texto=Frecuencia_texto+[*apariciones_ordenadas.keys()][pos]
       
        print(Frecuencia)
        print(Frecuencia_texto)
            
        #Intercambiar letras
        textoDescifrado = texto.maketrans(Frecuencia_texto, Frecuencia)
        print(texto.translate(textoDescifrado))
        
labo1()         