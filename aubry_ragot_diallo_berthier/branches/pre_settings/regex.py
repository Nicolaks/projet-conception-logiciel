

 #permet de regarder pour la variable.
#[_{2,3}] #permet de regarder pour la variable.
import re
with open('settings.txt') as f:
    for line in f:
        match = re.search('^-.*-', line)
        test = re.search('_.*_', line)

print(match)
print(test)
