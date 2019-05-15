# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    build.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: akharrou <akharrou@student.42.us.org>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/05/15 12:20:23 by akharrou          #+#    #+#              #
#    Updated: 2019/05/15 13:51:34 by akharrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import sys

DEFAULT    = '\033[0m'
ITALTIC    = '\033[3m'
UNDELRINED = '\033[4m'

print()

try:

	if (len(sys.argv) != 2):
		print(f'usage: python3 build {UNDELRINED}42_project_name{DEFAULT}')
		sys.exit(1)

	if (os.getcwd().find('42-GRUT') == -1):
		PREFIX = f'{os.getcwd()}/42-GRUT/'
	else:
		PREFIX = ''

	GRUT              = f'{PREFIX}/grut.template'
	EXTENSION         = sys.argv[1]
	EXTENSION_FOLDER  = 'extensions'
	GRUT_EXTENSION    = f'grut-{EXTENSION}.py'

	with open(GRUT, 'r') as fd_grut:
		with open(f'{PREFIX}/{EXTENSION_FOLDER}/{EXTENSION}.py', 'r') as fd_extension:
			with open(GRUT_EXTENSION, 'w') as fd_out:

				grut = fd_grut.read()
				grut = grut.replace('$__________', EXTENSION)

				extension_body = fd_extension.read()
				grut = grut.replace('$GRUTEXTENSION$', extension_body)

				fd_out.write(grut)

except Exception as e:
	print(f'{UNDELRINED}\n\n🚨  Please Report the Issue ! 🚨{DEFAULT}  :: G.R.U.T -- © 2019 akharrou 😓\n\n')
	print(f'{UNDELRINED}GRUT BUILD ISSUE:{DEFAULT} (copy paste and report (or dm me @akharrou) the issue)\n{ITALTIC}')
	raise e
