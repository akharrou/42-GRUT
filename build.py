# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    build.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: akharrou <akharrou@student.42.us.org>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/05/15 12:20:23 by akharrou          #+#    #+#              #
#    Updated: 2019/05/15 19:20:10 by akharrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import sys

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

	if (len(sys.argv) != 2):
		print(f'usage: python3 build {UNDELRINED}42_project_name{DEFAULT}')
		sys.exit(1)

	if (os.path.basename(os.getcwd()) == '42-GRUT'):
		PATH_42GRUT = f'{os.getcwd()}/'
	else:
		PATH_42GRUT = f'{os.getcwd()}/42-GRUT/'

	GRUT              = f'{PATH_42GRUT}grut.template'
	EXTENSION         = sys.argv[1]
	EXTENSION_FOLDER  = f'{PATH_42GRUT}Extensions/'
	GRUT_EXTENSION    = f'{PATH_42GRUT}../grut-{EXTENSION}.py'

	with open(GRUT, 'r') as fd_grut:
		with open(f'{EXTENSION_FOLDER}{EXTENSION}.py', 'r') as fd_extension:
			with open(GRUT_EXTENSION, 'w') as fd_out:

				grut = fd_grut.read()
				grut = grut.replace('$__________', EXTENSION)

				extension_body = fd_extension.read()
				grut = grut.replace('$GRUTEXTENSION$', extension_body)

				fd_out.write(grut)

	print(f'\n"{UNDELRINED}{ITALTIC}grut-{EXTENSION}.py{DEFAULT}" has successfully been built in your project\'s root directory.')
	print(f'\nTo get started, run:')
	print(f'\n     MANUAL:   {UNDELRINED}python3 grut-{EXTENSION}.py --manual{DEFAULT}')
	print(f'\n     USAGE:    {UNDELRINED}python3 grut-{EXTENSION}.py --help{DEFAULT}\n')
	print(('                             or'))
	print(f'\n     USAGE EXAMPLE:  python3 grut-{EXTENSION}.py {UNDELRINED}input_arguments ...{DEFAULT}\n')

except Exception as e:
	print(f' {f"—" * 90}\n')
	print(f'{RED_BACKGROUND}{YELLOW}💣  G.R.U.T BUILD CRASHED 💣{DEFAULT}\n')
	print(f'{UNDELRINED}\n🚨  Please Report the Issue ! 🚨{DEFAULT}  :: G.R.U.T -- © 2019 {UNDELRINED}kmira{DEFAULT} & {UNDELRINED}akharrou{DEFAULT} 😓')
	print(f'{DEFAULT}Copy paste the following and {YELLOW}report or dm{DEFAULT} us @akharrou / @kmira the issue\n\n')
	print(f'{UNDELRINED}GRUT BUILD ISSUE:\n{DEFAULT}{RED_BACKGROUND}{ITALTIC}')
	raise e
