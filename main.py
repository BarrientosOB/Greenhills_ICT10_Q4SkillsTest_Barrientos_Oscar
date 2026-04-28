from pyscript import display, document
import numpy as np
import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)

import matplotlib.pyplot as plt


days = np.array(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
absences = np.array([0, 0, 0, 0, 0])

def generate_graph():
    document.getElementById("plot").innerHTML = ""
    
    plt.figure(figsize=(6, 4))
    plt.plot(days, absences, marker='o')
    plt.title('Weekly Attendance (Absences)')
    plt.ylabel('Number of Absences')
    plt.grid(True)
    
    display(plt, target="plot")
    plt.close()

def update_data(event):
    day_idx = int(document.getElementById('day-select').value)
    val = document.getElementById('absence-count').value

    if val:
        absences[day_idx] = int(val)
        generate_graph()
        
        
        document.getElementById('absence-count').value = ""

generate_graph()