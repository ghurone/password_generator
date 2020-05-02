from secrets import choice


def password(tam=12, c_upp=True, c_spe=True, c_num=True):
    upp_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num_list = '1234567890'
    spe_list = '!@#$%&*'

    pass_list = 'abcdefghijklmnopqrstuvwxyz'
    psd = ''

    if c_upp:
        pass_list += upp_list

    if c_spe:
        pass_list += spe_list

    if c_num:
        pass_list += num_list

    for i in range(tam):
        psd += choice(pass_list)

    return psd
