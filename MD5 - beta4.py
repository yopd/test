import hashlib
import os
import binascii

print('')
print('Programmed by K 맑은삶')
print('')

print('기저대역이 다른 펌웨어도 찾습니다! 단, 반드시 찾는다고 보장하진 못합니다', end='\n')
print('\n')

firm_h = input('MD5로 인코딩 된 텍스트를 입력하세요: ')

firm_v = ''
firm_vh = ''
fv = ''

while firm_vh != firm_h:
    if firm_vh == firm_h:
        break

    print('\n')
    print('---------------------PDA---------------------')
    print('예측하고 싶은 펌웨어의 PDA 값을 입력하세요')
    print('')
    model = input('기기명을 입력해주세요 (ex: G977N) : ')
    edi_pda = input('국가코드를 (또는 에디션 이름) 입력해주세요 (ex: KS) : ')
    bootloader = input('부트로더 버전을 입력해주세요 (ex: 4) : ')
    major = input('메이저 버전을 입력해주세요 (ex: D) : ')
    year = input('빌드 된 연도를 입력해주세요 (ex: 2020년일 경우 T) : ')
    month = input('빌드 된 월을 입력해주세요 (ex: 10월일 경우 J) :')
    print('---------------------------------------------')
    print('\n')

    print('---------------------CSC---------------------')
    print('예측하고 싶은 펌웨어의 CSC 값을 입력하세요')
    print('')
    edi_csc = input('OKR, OKT 등 예측하고 싶은 종류의 펌웨어의 값을 입력하세요: ')
    print('---------------------------------------------')
    print('\n')

    print('---------------------PHONE---------------------')
    print('예측하고 싶은 펌웨어의 PHONE 값을 입력하세요')
    print('')
    edi_phone = input('KS, KO, KR 등 예측하고 싶은 펌웨어의 값을 입력하세요: ')
    major_phone = input('기저대역의 메이저 버전을 입력해주세요 (ex: D) : ')
    month_phone = input('기저대역이 빌드 된 월을 입력해주세요 (ex: 10월일 경우 J) : ')
    print('-----------------------------------------------')
    print('\n')

    b_count = '0'
    b_count_phone = '1'

    for i in range(0, 9):
        if firm_vh == firm_h:
            break
        b_count = b_count.encode()
        b_count = binascii.hexlify(b_count).decode()
        b_count = int(b_count, 16) + 1
        b_count = hex(b_count)[2:].upper()
        b_count = str(b_count).encode()
        b_count = binascii.unhexlify(b_count).decode()
        # print(b_count)

        firm_pda = model + edi_pda + 'U' + bootloader + major + year + month + b_count
        firm_csc = model + edi_csc + bootloader + major + year + month + b_count
        firm_phone = model + edi_phone + 'U' + bootloader + major_phone + year + month_phone + b_count_phone
        firm_v = firm_pda + '/' + firm_csc + '/' + firm_phone
        firm_vh = hashlib.md5(firm_v.encode()).hexdigest()
        # print(firm_v)

        if firm_vh == firm_h:
            break

        firm_v = firm_pda + '.DM/' + firm_csc + '/' + firm_phone
        firm_vh = hashlib.md5(firm_v.encode()).hexdigest()
        # print(firm_v)

        if firm_vh == firm_h:
            break

        firm_v = firm_pda + '.BDM/' + firm_csc + '/' + firm_phone
        firm_vh = hashlib.md5(firm_v.encode()).hexdigest()
        # print(firm_v)

        if firm_vh == firm_h:
            break

        b_count_phone = '0'
        for j in range(0, 9):
            b_count_phone = b_count_phone.encode()
            b_count_phone = binascii.hexlify(b_count_phone).decode()
            b_count_phone = int(b_count_phone, 16) + 1
            b_count_phone = hex(b_count_phone)[2:].upper()
            b_count_phone = str(b_count_phone).encode()
            b_count_phone = binascii.unhexlify(b_count_phone).decode()
            # print(b_count_phone)

            firm_pda = model + edi_pda + 'U' + bootloader + major + year + month + b_count
            firm_csc = model + edi_csc + bootloader + major + year + month + b_count
            firm_phone = model + edi_phone + 'U' + bootloader + major_phone + year + month_phone + b_count_phone
            firm_v = firm_pda + '/' + firm_csc + '/' + firm_phone
            firm_vh = hashlib.md5(firm_v.encode()).hexdigest()
            # print(firm_v)

            if firm_vh == firm_h:
                break

            firm_v = firm_pda + '.DM/' + firm_csc + '/' + firm_phone
            firm_vh = hashlib.md5(firm_v.encode()).hexdigest()
            # print(firm_v)

            if firm_vh == firm_h:
                break

            firm_v = firm_pda + '.BDM/' + firm_csc + '/' + firm_phone
            firm_vh = hashlib.md5(firm_v.encode()).hexdigest()
            # print(firm_v)

            if firm_vh == firm_h:
                break

    b_count = '@'
    for i in range(0, 26):
        if firm_vh == firm_h:
            break
        b_count = b_count.encode()
        b_count = binascii.hexlify(b_count).decode()
        b_count = int(b_count, 16) + 1
        b_count = hex(b_count)[2:].upper()
        b_count = str(b_count).encode()
        b_count = binascii.unhexlify(b_count).decode()
        # print(b_count)

        firm_pda = model + edi_pda + 'U' + bootloader + major + year + month + b_count
        firm_csc = model + edi_csc + bootloader + major + year + month + b_count
        firm_phone = model + edi_phone + 'U' + bootloader + major_phone + year + month_phone + b_count_phone
        firm_v = firm_pda + '/' + firm_csc + '/' + firm_phone
        firm_vh = hashlib.md5(firm_v.encode()).hexdigest()
        # print(firm_v)

        if firm_vh == firm_h:
            break

        firm_v = firm_pda + '.DM/' + firm_csc + '/' + firm_phone
        firm_vh = hashlib.md5(firm_v.encode()).hexdigest()
        # print(firm_v)

        if firm_vh == firm_h:
            break

        firm_v = firm_pda + '.BDM/' + firm_csc + '/' + firm_phone
        firm_vh = hashlib.md5(firm_v.encode()).hexdigest()
        # print(firm_v)

        if firm_vh == firm_h:
            break

        b_count_phone = '0'
        for j in range(0, 9):
            if firm_vh == firm_h:
                break
            b_count_phone = b_count_phone.encode()
            b_count_phone = binascii.hexlify(b_count_phone).decode()
            b_count_phone = int(b_count_phone, 16) + 1
            b_count_phone = hex(b_count_phone)[2:].upper()
            b_count_phone = str(b_count_phone).encode()
            b_count_phone = binascii.unhexlify(b_count_phone).decode()
            # print(b_count_phone)

            firm_pda = model + edi_pda + 'U' + bootloader + major + year + month + b_count
            firm_csc = model + edi_csc + bootloader + major + year + month + b_count
            firm_phone = model + edi_phone + 'U' + bootloader + major_phone + year + month_phone + b_count_phone
            firm_v = firm_pda + '/' + firm_csc + '/' + firm_phone
            firm_vh = hashlib.md5(firm_v.encode()).hexdigest()
            # print(firm_v)

            if firm_vh == firm_h:
                break

            firm_v = firm_pda + '.DM/' + firm_csc + '/' + firm_phone
            firm_vh = hashlib.md5(firm_v.encode()).hexdigest()
            # print(firm_v)

            if firm_vh == firm_h:
                break

            firm_v = firm_pda + '.BDM/' + firm_csc + '/' + firm_phone
            firm_vh = hashlib.md5(firm_v.encode()).hexdigest()
            # print(firm_v)

            if firm_vh == firm_h:
                break

    b_count = '@'
    for i in range(0, 26):
        if firm_vh == firm_h:
            break
        b_count = b_count.encode()
        b_count = binascii.hexlify(b_count).decode()
        b_count = int(b_count, 16) + 1
        b_count = hex(b_count)[2:].upper()
        b_count = str(b_count).encode()
        b_count = binascii.unhexlify(b_count).decode()
        # print(b_count)

        firm_pda = model + edi_pda + 'U' + bootloader + major + year + month + b_count
        firm_csc = model + edi_csc + bootloader + major + year + month + b_count
        firm_phone = model + edi_phone + 'U' + bootloader + major_phone + year + month_phone + b_count_phone
        firm_v = firm_pda + '/' + firm_csc + '/' + firm_phone
        firm_vh = hashlib.md5(firm_v.encode()).hexdigest()
        # print(firm_v)

        if firm_vh == firm_h:
            break

        firm_v = firm_pda + '.DM/' + firm_csc + '/' + firm_phone
        firm_vh = hashlib.md5(firm_v.encode()).hexdigest()
        # print(firm_v)

        if firm_vh == firm_h:
            break

        firm_v = firm_pda + '.BDM/' + firm_csc + '/' + firm_phone
        firm_vh = hashlib.md5(firm_v.encode()).hexdigest()
        # print(firm_v)

        if firm_vh == firm_h:
            break

        b_count_phone = '@'
        for j in range(0, 26):
            if firm_vh == firm_h:
                break
            b_count_phone = b_count_phone.encode()
            b_count_phone = binascii.hexlify(b_count_phone).decode()
            b_count_phone = int(b_count_phone, 16) + 1
            b_count_phone = hex(b_count_phone)[2:].upper()
            b_count_phone = str(b_count_phone).encode()
            b_count_phone = binascii.unhexlify(b_count_phone).decode()
            # print(b_count_phone)

            firm_pda = model + edi_pda + 'U' + bootloader + major + year + month + b_count
            firm_csc = model + edi_csc + bootloader + major + year + month + b_count
            firm_phone = model + edi_phone + 'U' + bootloader + major_phone + year + month_phone + b_count_phone
            firm_v = firm_pda + '/' + firm_csc + '/' + firm_phone
            firm_vh = hashlib.md5(firm_v.encode()).hexdigest()
            # print(firm_v)

            if firm_vh == firm_h:
                break

            firm_v = firm_pda + '.DM/' + firm_csc + '/' + firm_phone
            firm_vh = hashlib.md5(firm_v.encode()).hexdigest()
            # print(firm_v)

            if firm_vh == firm_h:
                break

            firm_v = firm_pda + '.BDM/' + firm_csc + '/' + firm_phone
            firm_vh = hashlib.md5(firm_v.encode()).hexdigest()
            # print(firm_v)

            if firm_vh == firm_h:
                break

    if firm_vh != firm_h:
        print('--------오작동 대비 검증용--------')
        print(firm_h, "| 입력한 값", )
        print(firm_vh, "| 최종적으로 계산된 값")
        print('----------------------------------', end='\n')
        print('\n')
        print("해당 키워드와 일치하는 빌드가 없습니다")


print('--------오작동 대비 검증용--------')
print(firm_h, "| 입력한 값", )
print(firm_vh, "| 최종적으로 계산된 값")
print('----------------------------------', end='\n')
print('\n')
print('입력하신 펌웨어는', firm_v, '입니다')

os.system('pause')