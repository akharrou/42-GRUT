	import time

	BAR_LEN  = 38 + (110 * 2) + 11 + 16
	COL1_LEN = 38
	COL2_LEN = 110
	COL3_LEN = 110
	COL4_LEN = 11

	FILE_A = f'/tmp/__output_A__'
	FILE_B = f'/tmp/__output_B__'

	def GRUTBody__ft_ls(program_A, program_B):

		i = 0
		total_trues = 0
		total_args = len(arguments)
		width = len(str(total_args))

		print(f' {f"—" * (BAR_LEN + width)}')
		print(f'| {"":{width}} |  {"INPUT:":{COL1_LEN}}|   {"PROGRAM A:":{COL2_LEN}}|   {"PROGRAM B:":{COL3_LEN}}|  {"IDENTICAL":{COL4_LEN}}|')
		print(f'|-{"-" * width}-|{"-" * (COL1_LEN + 2)}|{"-" * (COL2_LEN + 3)}|{"-" * (COL2_LEN + 3)}|{"-" * 13}|')

		with open(f"{FILE_A}", 'w+') as fd_A:
			with open(f"{FILE_B}", 'w+') as fd_B:

					for arg in arguments:

						try:

							arg = arg.strip('\n').replace('\t', '    ')

							test_trues = 0

							i += 1

							print(f"""| {'':{width}} |  {f'':{COL1_LEN}}|   {'':{COL2_LEN}}|   {'':{COL3_LEN}}| """, end="")
							print(f'  {"":{COL4_LEN - 1}}|')

							print(f"""| {i:0{width}} |  PATH: {f'{UNDELRINED}{arg}{DEFAULT}':{COL1_LEN + 2}}|   {f'':{COL2_LEN}}|   {f'':{COL3_LEN}}|   {f'':{COL4_LEN - 1}}|""")

							program_A_t1 = time.perf_counter()
							os.system(f"{program_A} {arg} > {FILE_A}")
							program_A_t2 = time.perf_counter()
							tt_program_A_time = program_A_t2 - program_A_t1

							program_B_t1 = time.perf_counter()
							os.system(f"{program_B} {arg} > {FILE_B}")
							program_B_t2 = time.perf_counter()
							tt_program_B_time = program_B_t2 - program_B_t1

							fd_A.seek(0)
							fd_B.seek(0)

							outputs = list(zip(fd_A.readlines(), fd_B.readlines()))

							programA_output = outputs[0][0].rstrip('\n')
							programB_output = outputs[0][1].rstrip('\n')

							lines_read = 1
							for lineA, lineB in outputs:

								lines_read += 1

								programA_output = lineA.rstrip('\n')
								programB_output = lineB.rstrip('\n')

								print(f"""| {'':{width}} |  {f'':{COL1_LEN}}|   {programA_output:{COL2_LEN}}|   {programB_output:{COL3_LEN}}| """, end="")

								if (programA_output == programB_output):
									print(f'  {f"[{GREEN}TRUE{DEFAULT}]":{COL4_LEN + 8}}|')
									test_trues += 1
								else:
									print(f'  {f"[{RED}FALSE{DEFAULT}]":{COL4_LEN + 8}}|')

							if (test_trues == len(outputs)):
								total_trues += 1

							print(f"""| {f'':{width}} |  {f'':{COL1_LEN}}|   {'':{COL2_LEN}}|   {'':{COL3_LEN}}|   {f'':{COL4_LEN - 1}}|""")
							print(f"""| {f'':{width}} |  {f'Time :':{COL1_LEN}}|   {f'{tt_program_A_time} seconds':{COL2_LEN}}|   {f'{tt_program_B_time} seconds':{COL3_LEN}}|   {f'':{COL4_LEN - 1}}|""")
							print(f"""| {f'':{width}} |  {f'':{COL1_LEN}}|   {'':{COL2_LEN}}|   {'':{COL3_LEN}}| """, end="")
							print(f'  {"":{COL4_LEN - 1}}|')

							print(f' {f"—" * (BAR_LEN + width)}')

						except Exception as e:
							print(f'|\n|  Something unexpected happened with the following argument : {RED_BACKGROUND}{YELLOW}💣  {arg} 💣{DEFAULT}\n|')
							print(f'|-{"-" * width}-|{"-" * (COL1_LEN + 2)}|{"-" * (COL2_LEN + 3)}|{"-" * (COL2_LEN + 3)}|{"-" * 13}|')

			print(f'\n[{total_trues} / {i}] IDENTICAL RESULTS ')

			os.remove(f'{FILE_A}')
			os.remove(f'{FILE_B}')
