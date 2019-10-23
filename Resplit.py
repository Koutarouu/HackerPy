regex_pattern = r"\.|,"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))
#Sample In: 100,000,000.000100,000,000.000