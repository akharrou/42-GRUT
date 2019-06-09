# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    build.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: akharrou <akharrou@student.42.us.org>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/05/15 12:20:23 by akharrou          #+#    #+#              #
#    Updated: 2019/06/09 15:10:45 by akharrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import sys
import pathlib

# COLORIZATION — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — #

RED        = '\033[31m'
GREEN      = '\033[32m'
YELLOW     = '\033[38;2;247;249;94m'
GOLD       = '\033[38;2;218;171;119m'

DEFAULT    = '\033[0m'
ITALTIC    = '\033[3m'
UNDELRINED = '\033[4m'
BACKGROUND = '\033[0m'
STRIPS     = GOLD

RED_BACKGROUND    = '\033[41m'
GREEN_BACKGROUND  = '\033[42m'

# SCRIPT — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — #

try:

	HOME = str(pathlib.Path.home())

	if (len(sys.argv) != 2):
		print(f'usage: python3 build {UNDELRINED}42_project_name{DEFAULT}')
		sys.exit(1)


	EXTENSION         = sys.argv[1]

	PATH_42GRUT       = f'{HOME}/42-GRUT'
	GRUT_TEMPLATE     = f'{PATH_42GRUT}/grut.template'
	EXTENSION_FOLDER  = f'{PATH_42GRUT}/Extensions/'
	GRUT_EXTENSION    = f'{EXTENSION_FOLDER}/grut-{EXTENSION}.py'

	with open(GRUT_TEMPLATE, 'r') as fd_grut:
		with open(f'{EXTENSION_FOLDER}{EXTENSION}.py', 'r') as fd_extension:
			with open(GRUT_EXTENSION, 'w') as fd_out:

				grut = fd_grut.read()
				grut = grut.replace('$__________', EXTENSION)

				extension_body = fd_extension.read()
				grut = grut.replace('$GRUTEXTENSION$', extension_body)

				fd_out.write(grut)

# WELCOME MESSAGE — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — #

	print(f'\n"{UNDELRINED}{ITALTIC}grut-{EXTENSION}.py{DEFAULT}" has successfully been built in your project\'s root directory.')
	print(f'\nTo get started, run:')

	print(f'\n     MANUAL:   {UNDELRINED}python3 grut-{EXTENSION}.py 0 0 --manual{DEFAULT}')
	print(f'\n     USAGE:    {UNDELRINED}python3 grut-{EXTENSION}.py 0 0 --help{DEFAULT}\n')

	print(('                             or'))

	# PROJECT SPECIFIC MESSAGE — — — — — — — — — — — — — — — — — — — — — — — — — — — — #

	if (EXTENSION == 'ft_ls'):
		print(f'\n     USAGE EXAMPLE:  python3 grut-ft_ls.py {UNDELRINED}"/bin/ls -lR"{DEFAULT} {UNDELRINED}"./ft_ls -lR"{DEFAULT}')
		print(f'\n     USAGE EXAMPLE:  python3 grut-ft_ls.py {UNDELRINED}"/bin/ls -l -at"{DEFAULT} {UNDELRINED}"./ft_ls -l -at"{DEFAULT} ~/ /var /goinfre ~/Applications ~/Desktop')
		print(f'\n     USAGE EXAMPLE:  python3 grut-ft_ls.py {UNDELRINED}"/bin/ls -RSip"{DEFAULT} {UNDELRINED}"./ft_ls -RSip"{DEFAULT} -f file_Containing_Input_On_Each_Line\n')

	elif (EXTENSION == 'fillit'):
		print(f'\n     USAGE EXAMPLE:  python3 grut-ft_fillit.py {UNDELRINED}./fillit_A{DEFAULT} {UNDELRINED}./fillit_B{DEFAULT} testfile_1 testfile_2 testfile_3')
		print(f'\n     USAGE EXAMPLE:  python3 grut-ft_fillit.py {UNDELRINED}./fillit_A{DEFAULT} {UNDELRINED}./fillit_B{DEFAULT} -f file_Containing_Names_Of_Test_Files_On_Each_Line\n')

	elif (EXTENSION == 'ft_ssl_md5'):
		print(f'\n     USAGE EXAMPLE:  python3 grut-ft_ssl_md5.py {UNDELRINED}md5{DEFAULT} {UNDELRINED}-q{DEFAULT} {UNDELRINED}./ft_ssl{DEFAULT} {UNDELRINED}md5 -q{DEFAULT} testfile_1 testfile_2 testfile_3\n')
		print(f'\n     USAGE EXAMPLE:  python3 grut-ft_ssl_md5.py {UNDELRINED}openssl{DEFAULT} {UNDELRINED}sha256{DEFAULT} {UNDELRINED}./ft_ssl{DEFAULT} {UNDELRINED}sha256{DEFAULT} file1 file2 file3\n')
		print(f'\n     USAGE EXAMPLE:  python3 grut-ft_ssl_md5.py {UNDELRINED}openssl{DEFAULT} {UNDELRINED}sha512 <<<{DEFAULT} {UNDELRINED}./ft_ssl{DEFAULT} {UNDELRINED}sha512 <<<{DEFAULT} file1 file2 file3\n')

# ERROR CATCHING — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — #

except FileNotFoundError as e:
	print(f'{UNDELRINED}{EXTENSION}{DEFAULT}: Wrong Project Name 🤔  ?\nTry Again 😀')

except Exception as e:
	print(f' {f"—" * 90}\n')
	print(f'{RED_BACKGROUND}{YELLOW}💣  G.R.U.T BUILD CRASHED 💣{DEFAULT}\n')
	print(f'{UNDELRINED}\n🚨  Please Report the Issue ! 🚨{DEFAULT}  :: 42 G.R.U.T -- © 2019')
	print(f'{DEFAULT}Copy paste the following and {YELLOW}report or dm{DEFAULT} @akharrou or @kmira the issue\n\n')
	print(f'{UNDELRINED}GRUT BUILD ISSUE:\n{DEFAULT}{RED_BACKGROUND}{ITALTIC}')
	raise e
