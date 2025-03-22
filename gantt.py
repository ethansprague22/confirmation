import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Define your tasks with start and end dates along with their assigned group.
# Adjust these tasks as needed for your project.
tasks = [
    {"Task": "Literature Review", "Start": datetime(2023, 1, 1), "End": datetime(2023, 6, 30), "Group": "Research/Experiments"},
    {"Task": "Proposal Development", "Start": datetime(2023, 7, 1), "End": datetime(2023, 9, 30), "Group": "Writing"},
    {"Task": "Experimentation", "Start": datetime(2023, 10, 1), "End": datetime(2024, 3, 31), "Group": "Research/Experiments"},
    {"Task": "Data Analysis", "Start": datetime(2024, 4, 1), "End": datetime(2025, 3, 31), "Group": "Data Analysis"},
    {"Task": "Thesis Drafting", "Start": datetime(2025, 4, 1), "End": datetime(2026, 1, 31), "Group": "Writing"},
    {"Task": "Final Revisions & Submission", "Start": datetime(2026, 2, 1), "End": datetime(2026, 7, 31), "Group": "Writing"},
]

# Define colors for each of the three groups.
group_colors = {
    "Research/Experiments": "skyblue",
    "Data Analysis": "lightcoral",
    "Writing": "lightgreen"
}

fig, ax = plt.subplots(figsize=(12, 6))

# Plot each task as a horizontal bar.
for i, task in enumerate(tasks):
    start_date_num = mdates.date2num(task["Start"])
    # Duration in days
    duration = (task["End"] - task["Start"]).days
    # Each task is plotted on its own horizontal level (using i*10 for separation)
    ax.broken_barh([(start_date_num, duration)], (i*10, 9),
                   facecolors=group_colors.get(task["Group"], "grey"),
                   edgecolor='black',
                   linewidth=1)
    # Optionally, add the task name as a label on the left
    ax.text(start_date_num - 10, i*10 + 4.5, task["Task"],
            va='center', ha='right', fontsize=9)

# Format the x-axis to show dates.
ax.xaxis_date()
# Place the x-axis on the top.
ax.xaxis.tick_top()
# Set major ticks every 3 months and format them as "Mon Year".
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.xticks(rotation=45)

# Set the y-axis limits so all tasks are visible.
ax.set_ylim(0, len(tasks)*10)
# Set the x-axis limits to cover the full timeline (with a little padding).
ax.set_xlim(mdates.date2num(datetime(2023,1,1))-15, mdates.date2num(datetime(2026,7,31))+15)

ax.set_xlabel('Timeline')
ax.set_title('PhD Project Timeline Gantt Chart Template')

plt.tight_layout()
plt.show()
