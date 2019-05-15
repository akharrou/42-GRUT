# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    grutbuilder.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: akharrou <akharrou@student.42.us.org>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/05/15 12:20:23 by akharrou          #+#    #+#              #
#    Updated: 2019/05/15 12:46:13 by akharrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

DEFAULT    = '\033[0m'
UNDELRINED = '\033[4m'

try:

	GRUT           = f'grut.txt'
	EXTENSION      = sys.argv[1]
	GRUT_EXTENSION = f'grut-{EXTENSION}.py'

	with open(GRUT, 'r') as fd_grut:
		with open(GRUT_EXTENSION, 'w') as fd_extension:

			grut = str(fd_grut.read())
			grut = grut.replace('$__________', EXTENSION)

			grut = grut.replace('import sys', f'import sys\nimport {EXTENSION}')

			fd_extension.write(grut)

except Exception:
	print(f'usage: grutBuilder {UNDELRINED}project_name{DEFAULT}')
