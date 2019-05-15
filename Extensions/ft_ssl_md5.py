# ================================================== #
#
#   GRUT Extension
#
#   Project: ft_ssl_md5
#   Author:  akharrou
#   Date:    15/05/2019
#
# ================================================== #

import os

FILE_A='__output_A__'
FILE_B='__output_B__'

def GRUTBody__ft_ssl_md5(launch_command_programA, launch_command_programB):

	i = 0
	total_trues = 0
	total_args = len(arguments)
	width = len(str(total_args))

	print(f' {f"—" * (197 + width)}')
	print(f'| {"":{width}} |  {"INPUT:":100}|   {"PROGRAM A:":35}|   {"PROGRAM B:":35}|  {"IDENTICAL":11}|')
	print(f'|-{"-" * width}-|{"-" * 102}|{"-" * 38}|{"-" * 38}|{"-" * 13}|')

	with open("{FILE_A}", 'w+') as fd_A:
		with open("{FILE_B}", 'w+') as fd_B:

			for arg in arguments:

				arg = arg.strip('\n').replace('\t', '    ')

				i += 1
				os.system(f'{launch_command_programA} "{arg}" > {FILE_A}')
				os.system(f'{launch_command_programB} "{arg}" > {FILE_B}')

				fd_A.seek(0)
				programA_output = fd_A.readline().rstrip('\n')

				fd_B.seek(0)
				programB_output = fd_B.readline().rstrip('\n')

				print(f"""| {i:0{width}} |  {f'"{arg}"':100}|   {programA_output:35}|   {programB_output:35}| """, end="")

				if (programA_output == programB_output):
					print(f'  {f"[{GREEN}TRUE{DEFAULT}]":19}|')
					total_trues += 1
				else:
					print(f'  {f"[{RED}FALSE{DEFAULT}]":19}|')

	print(f'|{f"—" * (197 + width)}|')
	print(f'[{total_trues} / {i}] identical outputs ‼️ ')

	os.remove('{FILE_A}')
	os.remove('{FILE_B}')
