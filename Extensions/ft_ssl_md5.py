	BAR_LEN  = 197

	FILE_A='__output_A__'
	FILE_B='__output_B__'

	def GRUTBody__ft_ssl_md5(program_A, program_B):

		i = 0
		total_trues = 0
		total_args = len(arguments)
		width = len(str(total_args))

		print(f' {f"—" * (197 + width)}')
		print(f'| {"":{width}} |  {"INPUT:":100}|   {"PROGRAM A:":35}|   {"PROGRAM B:":35}|  {"IDENTICAL":11}|')
		print(f'|-{"-" * width}-|{"-" * 102}|{"-" * 38}|{"-" * 38}|{"-" * 13}|')

		with open(f"{FILE_A}", 'w+') as fd_A:
			with open(f"{FILE_B}", 'w+') as fd_B:

				for arg in arguments:

					arg = arg.strip('\n').replace('\t', '    ')

					i += 1
					os.system(f'{program_A} "{arg}" > {FILE_A}')
					os.system(f'{program_B} "{arg}" > {FILE_B}')

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

		os.remove(f'{FILE_A}')
		os.remove(f'{FILE_B}')
