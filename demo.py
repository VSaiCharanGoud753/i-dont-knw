from printer import show_sum, get_sum, format_sum

show_sum(3,5)

get_sum(3,5)

use_print=True
use_format=False

if use_print:
    show_sum(3,5)

else:
    result=get_sum(3,5)
    result=[]
    result.append(result)
    print(result)

print(format_sum(3, 5))


