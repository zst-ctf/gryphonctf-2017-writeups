import re


def xor(bytestr, key):
    # convert hex-string to integer-bytes
    bytestr = list(map(lambda x: int(x.strip(), 16), bytestr))
    # remove null chars
    bytestr = list(filter(None, bytestr))
    # xor it!
    characters = list(map(lambda x: chr(x ^ key), bytestr))

    return ''.join(characters)


def find_hex_from_dsm(dump):
    return re.findall(r'.+? \$0x(.*),.+\)', dump.strip())


def find_hex_from_db(dump):
    return re.findall(r'.+?0x(..) ;.+', dump.strip())


def main():

    hexes = find_hex_from_dsm('''
    08048b01         movb       $0x7c, var_110E(%ebp)
    08048b08         movb       $0x50, var_110D(%ebp)
    08048b0f         movb       $0x4a, var_110C(%ebp)
    08048b16         movb       $0x53, var_110B(%ebp)
    08048b1d         movb       $0x5b, var_110A(%ebp)
    08048b24         movb       $0x51, var_1109(%ebp)
    08048b2b         movb       $0x18, var_1108(%ebp)
    08048b32         movb       $0x4b, var_1107(%ebp)
    08048b39         movb       $0x0, var_1106(%ebp)
    ''')
    print( xor(hexes, 0x3F) )

    hexes = find_hex_from_dsm('''
    08048b40         movb       $0x3d, var_1114(%ebp)
    08048b47         movb       $0x14, var_1113(%ebp)
    08048b4e         movb       $0xe, var_1112(%ebp)
    08048b55         movb       $0x15, var_1111(%ebp)
    08048b5c         movb       $0x1f, var_1110(%ebp)
    08048b63         movb       $0x0, var_110F(%ebp)
    ''')
    print( xor(hexes, 0x7B) )


    hexes = find_hex_from_dsm('''
    08048b6a         movb       $0x49, var_1105(%ebp)
    08048b71         movb       $0x42, var_1104(%ebp)
    08048b78         movb       $0x4b, var_1103(%ebp)
    08048b7f         movb       $0x5e, var_1102(%ebp)
    08048b86         movb       $0x4, var_1101(%ebp)
    08048b8d         movb       $0x4c, var_1100(%ebp)
    08048b94         movb       $0x58, var_10FF(%ebp)
    08048b9b         movb       $0x4f, var_10FE(%ebp)
    08048ba2         movb       $0x4f, var_10FD(%ebp)
    08048ba9         movb       $0x44, var_10FC(%ebp)
    08048bb0         movb       $0x45, var_10FB(%ebp)
    08048bb7         movb       $0x4e, var_10FA(%ebp)
    08048bbe         movb       $0x4f, var_10F9(%ebp)
    08048bc5         movb       $0x4, var_10F8(%ebp)
    08048bcc         movb       $0x49, var_10F7(%ebp)
    08048bd3         movb       $0x45, var_10F6(%ebp)
    08048bda         movb       $0x47, var_10F5(%ebp)
    08048be1         movb       $0x0, var_10F4(%ebp)
    ''')
    print( xor(hexes, 0x2A) )

    """
    08048be8         leal       var_10DF(%ebp), %eax
    08048bee         movl       $0x8049860, %ebx
    """
    hexes = find_hex_from_db("""
    08049860         db  0x57 ; 'W'                                                 ; DATA XREF=_sys_construct+260
    08049861         db  0x51 ; 'Q'
    08049862         db  0x47 ; 'G'
    08049863         db  0x50 ; 'P'
    08049864         db  0x22 ; '"'
    08049865         db  0x45 ; 'E'
    08049866         db  0x41 ; 'A'
    08049867         db  0x56 ; 'V'
    08049868         db  0x44 ; 'D'
    08049869         db  0x5d ; ']'
    0804986a         db  0x4b ; 'K'
    0804986b         db  0x46 ; 'F'
    0804986c         db  0x33 ; '3'
    0804986d         db  0x32 ; '2'
    0804986e         db  0x56 ; 'V'
    0804986f         db  0x5d ; ']'
    08049870         db  0x27 ; '''
    08049871         db  0x71 ; 'q'
    08049872         db  0x22 ; '"'
    08049873         db  0x45 ; 'E'
    08049874         db  0x41 ; 'A'
    08049875         db  0x56 ; 'V'
    08049876         db  0x44 ; 'D'
    08049877         db  0x5d ; ']'
    08049878         db  0x4b ; 'K'
    08049879         db  0x46 ; 'F'
    0804987a         db  0x33 ; '3'
    0804987b         db  0x32 ; '2'
    0804987c         db  0x56 ; 'V'
    0804987d         db  0x5d ; ']'
    0804987e         db  0x27 ; '''
    0804987f         db  0x71 ; 'q'
    08049880         db  0x22 ; '"'
    08049881         db  0x45 ; 'E'
    08049882         db  0x41 ; 'A'
    08049883         db  0x56 ; 'V'
    08049884         db  0x44 ; 'D'
    08049885         db  0x5d ; ']'
    08049886         db  0x4b ; 'K'
    08049887         db  0x46 ; 'F'
    08049888         db  0x33 ; '3'
    08049889         db  0x32 ; '2'
    0804988a         db  0x56 ; 'V'
    0804988b         db  0x5d ; ']'
    0804988c         db  0x27 ; '''
    0804988d         db  0x71 ; 'q'
    0804988e         db  0x22 ; '"'
    0804988f         db  0x38 ; '8'
    08049890         db  0x45 ; 'E'
    08049891         db  0x41 ; 'A'
    08049892         db  0x56 ; 'V'
    08049893         db  0x44 ; 'D'
    08049894         db  0x5d ; ']'
    08049895         db  0x4b ; 'K'
    08049896         db  0x46 ; 'F'
    08049897         db  0x33 ; '3'
    08049898         db  0x32 ; '2'
    08049899         db  0x56 ; 'V'
    0804989a         db  0x5d ; ']'
    0804989b         db  0x27 ; '''
    0804989c         db  0x71 ; 'q'
    0804989d         db  0x08 ; '.'
    0804989e         db  0x4c ; 'L'
    0804989f         db  0x4b ; 'K'
    080498a0         db  0x41 ; 'A'
    080498a1         db  0x49 ; 'I'
    080498a2         db  0x22 ; '"'
    080498a3         db  0x45 ; 'E'
    080498a4         db  0x41 ; 'A'
    080498a5         db  0x56 ; 'V'
    080498a6         db  0x44 ; 'D'
    080498a7         db  0x5d ; ']'
    080498a8         db  0x4b ; 'K'
    080498a9         db  0x46 ; 'F'
    080498aa         db  0x33 ; '3'
    080498ab         db  0x32 ; '2'
    080498ac         db  0x56 ; 'V'
    080498ad         db  0x5d ; ']'
    080498ae         db  0x27 ; '''
    080498af         db  0x71 ; 'q'
    080498b0         db  0x08 ; '.'
    080498b1         db  0x00 ; '.'
    """)
    print( xor(hexes, 0x02) )


    '''
    08048c1e         leal       var_108D(%ebp), %eax
    08048c24         movl       $0x80498c0, %ebx
    '''
    hexes = find_hex_from_db("""
    080498c0         db  0x35 ; '5'                                                 ; DATA XREF=_sys_construct+314
    080498c1         db  0x30 ; '0'
    080498c2         db  0x36 ; '6'
    080498c3         db  0x31 ; '1'
    080498c4         db  0x5f ; '_'
    080498c5         db  0x5c ; '\'
    080498c6         db  0x18 ; '.'
    080498c7         db  0x0d ; '.'
    080498c8         db  0x06 ; '.'
    080498c9         db  0x0f ; '.'
    080498ca         db  0x17 ; '.'
    080498cb         db  0x10 ; '.'
    080498cc         db  0x11 ; '.'
    080498cd         db  0x1c ; '.'
    080498ce         db  0x0b ; '.'
    080498cf         db  0x19 ; '.'
    080498d0         db  0x75 ; 'u'
    080498d1         db  0x2f ; '/'
    080498d2         db  0x2d ; '-'
    080498d3         db  0x36 ; '6'
    080498d4         db  0x29 ; ')'
    080498d5         db  0x32 ; '2'
    080498d6         db  0x2c ; ','
    080498d7         db  0x38 ; '8'
    080498d8         db  0x5f ; '_'
    080498d9         db  0x5c ; '\'
    080498da         db  0x18 ; '.'
    080498db         db  0x0d ; '.'
    080498dc         db  0x06 ; '.'
    080498dd         db  0x0f ; '.'
    080498de         db  0x17 ; '.'
    080498df         db  0x10 ; '.'
    080498e0         db  0x11 ; '.'
    080498e1         db  0x1c ; '.'
    080498e2         db  0x0b ; '.'
    080498e3         db  0x19 ; '.'
    080498e4         db  0x5f ; '_'
    080498e5         db  0x45 ; 'E'
    080498e6         db  0x36 ; '6'
    080498e7         db  0x5f ; '_'
    080498e8         db  0x3e ; '>'
    080498e9         db  0x32 ; '2'
    080498ea         db  0x5f ; '_'
    080498eb         db  0x3e ; '>'
    080498ec         db  0x31 ; '1'
    080498ed         db  0x5f ; '_'
    080498ee         db  0x36 ; '6'
    080498ef         db  0x3b ; ';'
    080498f0         db  0x4e ; 'N'
    080498f1         db  0x4f ; 'O'
    080498f2         db  0x2b ; '+'
    080498f3         db  0x5f ; '_'
    080498f4         db  0x28 ; '('
    080498f5         db  0x37 ; '7'
    080498f6         db  0x30 ; '0'
    080498f7         db  0x5f ; '_'
    080498f8         db  0x2d ; '-'
    080498f9         db  0x2a ; '*'
    080498fa         db  0x31 ; '1'
    080498fb         db  0x2c ; ','
    080498fc         db  0x5f ; '_'
    080498fd         db  0x3d ; '='
    080498fe         db  0x36 ; '6'
    080498ff         db  0x31 ; '1'
    08049900         db  0x3e ; '>'
    08049901         db  0x2d ; '-'
    08049902         db  0x36 ; '6'
    08049903         db  0x3a ; ':'
    08049904         db  0x2c ; ','
    08049905         db  0x5f ; '_'
    08049906         db  0x38 ; '8'
    08049907         db  0x36 ; '6'
    08049908         db  0x29 ; ')'
    08049909         db  0x3a ; ':'
    0804990a         db  0x31 ; '1'
    0804990b         db  0x5f ; '_'
    0804990c         db  0x2b ; '+'
    0804990d         db  0x30 ; '0'
    0804990e         db  0x5f ; '_'
    0804990f         db  0x32 ; '2'
    08049910         db  0x3a ; ':'
    08049911         db  0x5f ; '_'
    08049912         db  0x36 ; '6'
    08049913         db  0x31 ; '1'
    08049914         db  0x3b ; ';'
    08049915         db  0x36 ; '6'
    08049916         db  0x2c ; ','
    08049917         db  0x3c ; '<'
    08049918         db  0x2d ; '-'
    08049919         db  0x36 ; '6'
    0804991a         db  0x32 ; '2'
    0804991b         db  0x36 ; '6'
    0804991c         db  0x31 ; '1'
    0804991d         db  0x3e ; '>'
    0804991e         db  0x2b ; '+'
    0804991f         db  0x3a ; ':'
    08049920         db  0x33 ; '3'
    08049921         db  0x26 ; '&'
    08049922         db  0x5e ; '^'
    08049923         db  0x5f ; '_'
    08049924         db  0x32 ; '2'
    08049925         db  0x30 ; '0'
    08049926         db  0x3c ; '<'
    08049927         db  0x34 ; '4'
    08049928         db  0x5f ; '_'
    08049929         db  0x32 ; '2'
    0804992a         db  0x3a ; ':'
    0804992b         db  0x3a ; ':'
    0804992c         db  0x3a ; ':'
    0804992d         db  0x5e ; '^'
    0804992e         db  0x5e ; '^'
    0804992f         db  0x5e ; '^'
    08049930         db  0x75 ; 'u'
    08049931         db  0x00 ; '.'
    08049932         db  0x00 ; '.'
    08049933         db  0x00 ; '.'
    """)
    print( xor(hexes, 0x7F) )


    hexes = find_hex_from_dsm('''
    08048c54         movb       $0x5d, var_10F3(%ebp)
    08048c5b         movb       $0x76, var_10F2(%ebp)
    08048c62         movb       $0x7c, var_10F1(%ebp)
    08048c69         movb       $0x38, var_10F0(%ebp)
    08048c70         movb       $0x77, var_10EF(%ebp)
    08048c77         movb       $0x7e, var_10EE(%ebp)
    08048c7e         movb       $0x38, var_10ED(%ebp)
    08048c85         movb       $0x37, var_10EC(%ebp)
    08048c8c         movb       $0x56, var_10EB(%ebp)
    08048c93         movb       $0x59, var_10EA(%ebp)
    08048c9a         movb       $0x55, var_10E9(%ebp)
    08048ca1         movb       $0x5d, var_10E8(%ebp)
    08048ca8         movb       $0x4b, var_10E7(%ebp)
    08048caf         movb       $0x38, var_10E6(%ebp)
    08048cb6         movb       $0x74, var_10E5(%ebp)
    08048cbd         movb       $0x71, var_10E4(%ebp)
    08048cc4         movb       $0x6b, var_10E3(%ebp)
    08048ccb         movb       $0x6c, var_10E2(%ebp)
    08048cd2         movb       $0x36, var_10E1(%ebp)
    08048cd9         movb       $0x0, var_10E0(%ebp)
    ''')
    print( xor(hexes, 0x18) )

if __name__ == '__main__':
    main()