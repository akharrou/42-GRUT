	BAR_LEN  = 105
	COL1_LEN = 38
	COL2_LEN = 20
	COL3_LEN = 20
	COL4_LEN = 11

	FILE_A = '__output_A__'
	FILE_B = '__output_B__'

	def GRUTBody__fillit(program_A, program_B):

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

						arg = arg.strip('\n').replace('\t', '    ')

						with open(arg, 'r') as fd_input:

							test_trues = 0

							i += 1
							os.system(f'{program_A} "{arg}" > {FILE_A}')
							os.system(f'{program_B} "{arg}" > {FILE_B}')

							fd_A.seek(0)
							fd_B.seek(0)

							inputFile = fd_input.readlines()
							inputFile.insert(0, '')
							inputFile.insert(0, arg)

							outputs = list(zip(fd_A.readlines(), fd_B.readlines(), inputFile))

							programA_output = outputs[0][0].rstrip('\n')
							programB_output = outputs[0][1].rstrip('\n')
							arg_input = outputs[0][2].rstrip('\n')

							print(f"""| {'':{width}} |  {f'':{COL1_LEN}}|   {'':{COL2_LEN}}|   {'':{COL3_LEN}}| """, end="")
							print(f'  {"":{COL4_LEN - 1}}|')

							print(f"""| {i:0{width}} |  FILE: {f'{UNDELRINED}{arg_input}{DEFAULT}':{COL1_LEN + 2}}|   {programA_output:{COL2_LEN}}|   {programB_output:{COL3_LEN}}| """, end="")

							outputs = outputs[1:]

							if (programA_output == programB_output):
								print(f'  {f"[{GREEN}TRUE{DEFAULT}]":{COL4_LEN + 8}}|')
								test_trues += 1
							else:
								print(f'  {f"[{RED}FALSE{DEFAULT}]":{COL4_LEN + 8}}|')

							lines_read = 1
							for lineA, lineB, lineInput in outputs:

								lines_read += 1

								programA_output = lineA.rstrip('\n')
								programB_output = lineB.rstrip('\n')
								arg_input = lineInput.rstrip('\n')

								print(f"""| {'':{width}} |  {f'{arg_input}':{COL1_LEN}}|   {programA_output:{COL2_LEN}}|   {programB_output:{COL3_LEN}}| """, end="")

								if (programA_output == programB_output):
									print(f'  {f"[{GREEN}TRUE{DEFAULT}]":{COL4_LEN + 8}}|')
									test_trues += 1
								else:
									print(f'  {f"[{RED}FALSE{DEFAULT}]":{COL4_LEN + 8}}|')

							if (test_trues == len(outputs) + 1):
								total_trues += 1

							arg_input = inputFile[lines_read:]
							for line in arg_input:
								line = line.rstrip('\n')
								print(f"""| {'':{width}} |  {f'{line}':{COL1_LEN}}|   {'':{COL2_LEN}}|   {'':{COL3_LEN}}| """, end="")
								print(f'  {"":{COL4_LEN - 1}}|')

							print(f"""| {'':{width}} |  {f'':{COL1_LEN}}|   {'':{COL2_LEN}}|   {'':{COL3_LEN}}| """, end="")
							print(f'  {"":{COL4_LEN - 1}}|')

							print(f' {f"—" * (BAR_LEN + width)}')


			print(f'\n[{total_trues} / {i}] IDENTICAL RESULTS ')

			os.remove(f'{FILE_A}')
			os.remove(f'{FILE_B}')
