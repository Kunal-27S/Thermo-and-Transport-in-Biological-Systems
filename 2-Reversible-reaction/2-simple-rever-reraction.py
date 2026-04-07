import sys

from basico import *
import numpy as np
import matplotlib.pyplot as plt
colorb=['#c7e9b4','#41b6c4','#225ea8', ]
colorr=['#fdd49e','#fc8d59','#d7301f']


fig1=plt.figure(figsize=(8, 6.0))
ax = fig1.add_subplot(111)



new_model(name='Simple Model');
add_reaction('R1', 'A = B');

set_species('B', initial_concentration=0)
set_species('A', initial_concentration=10)
get_species().initial_concentration

set_reaction_parameters('(R1).k1', value=0.6)
set_reaction_parameters('(R1).k2', value=0.3)

print (get_reactions())

cl=1
result = run_time_course(duration=50)
result.plot(y='A', color=colorr[cl], ax=ax, label=r'$A$',  linewidth=4);
result.plot(y='B', color=colorb[cl], ax=ax,  label=r'$B$', linestyle='-', linewidth=4);



    

lg=ax.legend(fancybox=False,loc='upper right',  numpoints=1, prop={'size':20}, labelspacing=0.2, handletextpad=0.4)
lg._legend_box.align = "center"
lg.get_title().set_fontsize(25)
lg.get_title().set_position((20, 0))
lg.get_frame().set_alpha(0.0)  



ax.set_xlabel(r'time', fontsize=15,labelpad=8)
ax.set_ylabel(r' concentration', fontsize=15,labelpad=8)


plt.tight_layout( )
plt.savefig('i2simple-model-reversible.png', bbox_inches='tight' , transparent=False,  dpi=300)
plt.close
