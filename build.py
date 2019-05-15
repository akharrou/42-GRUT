# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    build.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: akharrou <akharrou@student.42.us.org>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/05/15 12:20:23 by akharrou          #+#    #+#              #
#    Updated: 2019/05/15 13:25:55 by akharrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

DEFAULT    = '\033[0m'
UNDELRINED = '\033[4m'

try:

	GRUT              = f'grut.template'
	EXTENSION         = sys.argv[1]
	EXTENSION_FOLDER  = 'extensions'
	GRUT_EXTENSION    = f'grut-{EXTENSION}.py'

	with open(GRUT, 'r') as fd_grut:
		with open(f'{EXTENSION_FOLDER}/{EXTENSION}.py', 'r') as fd_extension:
			with open(GRUT_EXTENSION, 'w') as fd_out:

				grut = fd_grut.read()
				grut = grut.replace('$__________', EXTENSION)

				extension_body = fd_extension.read()
				grut = grut.replace('$GRUTEXTENSION$', extension_body)

				fd_out.write(grut)

except Exception:
	print(f'usage: python3 build {UNDELRINED}42_project_name{DEFAULT}')
