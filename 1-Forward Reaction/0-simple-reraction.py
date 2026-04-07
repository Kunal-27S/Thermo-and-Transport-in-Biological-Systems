import sys

from basico import *
import numpy as np
import matplotlib.pyplot as plt

fig1=plt.figure(figsize=(8, 6.0))
ax = fig1.add_subplot(111)


new_model(name='Simple Model');
add_reaction('R1', 'A -> B');

set_species('B', initial_concentration=0)
set_species('A', initial_concentration=10)
get_species().initial_concentration

set_reaction_parameters('(R1).k1', value=1)
get_reaction_parameters('k1')


result = run_time_course(duration=50)
ax=result.plot();

ax.set_xlabel(r'time', fontsize=15,labelpad=8)
ax.set_ylabel(r' concentration', fontsize=15,labelpad=8)


plt.tight_layout( )
plt.savefig('i0simple-model.png', bbox_inches='tight' , transparent=False,  dpi=300)
plt.close
