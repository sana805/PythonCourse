import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#import numpy as np

# -----------------------------
# Sample Data
# -----------------------------
subjects = ["Maths", "Science", "English", "Computer", "History"]   #Bar chart for comparing student marks
marks = [85, 78, 90, 95, 72]

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 150, 180, 140, 210, 250]                      #line chart for track monthly sales trend.
                                                            #pie  chart for understanding mark distribution
study_hours = [1, 2, 3, 4, 5, 6, 7, 8]                 #Scatter Plot → Explore the relationship between study hours and marks
student_marks = [40, 45, 52, 60, 68, 75, 82, 90]

# -----------------------------
# Create Main Window
# -----------------------------
root = tk.Tk()
root.title("Interactive Matplotlib Dashboard")
root.geometry("1100x700")
root.configure(bg="#f4f6f8")

# -----------------------------
# Header
# -----------------------------
header = tk.Frame(root, bg="#1f4e78", height=80)
header.pack(fill="x")

title = tk.Label(
    header,
    text="Interactive Data Visualization Dashboard",
    font=("Arial", 24, "bold"),
    fg="white",
    bg="#1f4e78"
)
title.pack(pady=20)

# -----------------------------
# Control Panel
# -----------------------------
control_frame = tk.Frame(root, bg="#f4f6f8")
control_frame.pack(pady=15)

tk.Label(
    control_frame,
    text="Select Chart:",
    font=("Arial", 12, "bold"),
    bg="#f4f6f8"
).grid(row=0, column=0, padx=10)

chart_var = tk.StringVar()
chart_dropdown = ttk.Combobox(
    control_frame,
    textvariable=chart_var,
    values=[
        "Bar Chart",
        "Line Chart",
        "Pie Chart",
        "Scatter Plot"
    ],
    state="readonly",
    width=20
)
chart_dropdown.grid(row=0, column=1, padx=10)
chart_dropdown.current(0)

# -----------------------------
# Matplotlib Figure
# -----------------------------
fig, ax = plt.subplots(figsize=(9, 5))
fig.patch.set_facecolor("#ffffff")

canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(fill="both", expand=True, padx=20, pady=10)


# -----------------------------
# Chart Update Function
# -----------------------------
def update_chart():
    chart_type = chart_var.get()

    ax.clear()

    if chart_type == "Bar Chart":

        colors = [
            "#3498db",
            "#2ecc71",
            "#f1c40f",
            "#e74c3c",
            "#9b59b6"
        ]

        bars = ax.bar(subjects, marks, color=colors)

        ax.set_title(
            "Student Marks by Subject",
            fontsize=18,
            fontweight="bold"
        )
        ax.set_xlabel("Subjects")
        ax.set_ylabel("Marks")
        ax.set_ylim(0, 100)

        # Display values
        for bar in bars:
            height = bar.get_height()
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                height + 2,
                str(height),
                ha="center",
                fontweight="bold"
            )

        ax.grid(axis="y", alpha=0.3)

    elif chart_type == "Line Chart":

        ax.plot(
            months,
            sales,
            marker="o",
            linewidth=3,
            color="#2980b9"
        )

        ax.fill_between(
            months,
            sales,
            alpha=0.15,
            color="#2980b9"
        )

        ax.set_title(
            "Monthly Sales Trend",
            fontsize=18,
            fontweight="bold"
        )
        ax.set_xlabel("Month")
        ax.set_ylabel("Sales")

        ax.grid(True, alpha=0.3)

    elif chart_type == "Pie Chart":

        ax.pie(
            marks,
            labels=subjects,
            autopct="%1.1f%%",
            startangle=90,
            colors=[
                "#3498db",
                "#2ecc71",
                "#f1c40f",
                "#e74c3c",
                "#9b59b6"
            ],
            wedgeprops={"edgecolor": "white"}
        )

        ax.set_title(
            "Subject-wise Marks Distribution",
            fontsize=18,
            fontweight="bold"
        )

    elif chart_type == "Scatter Plot":

        ax.scatter(
            study_hours,
            student_marks,
            s=100,
            color="#e74c3c",
            edgecolors="black"
        )

        ax.set_title(
            "Study Hours vs Marks",
            fontsize=18,
            fontweight="bold"
        )
        ax.set_xlabel("Study Hours")
        ax.set_ylabel("Marks")

        ax.grid(True, alpha=0.3)

    fig.tight_layout()
    canvas.draw()


# -----------------------------
# Update Button
# -----------------------------
update_button = tk.Button(
    control_frame,
    text="Update Chart",
    command=update_chart,
    bg="#27ae60",
    fg="white",
    font=("Arial", 11, "bold"),
    padx=20,
    pady=5,
    cursor="hand2"
)

update_button.grid(row=0, column=2, padx=15)

# -----------------------------
# Exit Button
# -----------------------------
exit_button = tk.Button(
    control_frame,
    text="Exit",
    command=root.destroy,
    bg="#c0392b",
    fg="white",
    font=("Arial", 11, "bold"),
    padx=20,
    pady=5,
    cursor="hand2"
)

exit_button.grid(row=0, column=3, padx=10)

# -----------------------------
# Show Initial Chart
# -----------------------------
update_chart()

# -----------------------------
# Run Application
# -----------------------------
root.mainloop()
