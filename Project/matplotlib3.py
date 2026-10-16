import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

# --------------------------------
# DATA
# --------------------------------
data = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [25000, 32000, 28000, 40000, 45000, 38000],
    "Profit": [5000, 7000, 6000, 9000, 11000, 8500],
    "Expenses": [20000, 25000, 22000, 31000, 34000, 29500],
    "Customers": [120, 150, 135, 180, 210, 190]
})

# --------------------------------
# COLORS
# --------------------------------
BLUE = "#3498DB"
GREEN = "#2ECC71"
ORANGE = "#F39C12"
PURPLE = "#9B59B6"
RED = "#E74C3C"
CYAN = "#00CEC9"
YELLOW = "#F1C40F"
DARK_BLUE = "#154360"
BG = "#F4F6F7"

# --------------------------------
# LAPTOP SIZE
# --------------------------------
fig = plt.figure(figsize=(12, 6.7))
fig.patch.set_facecolor(BG)

# --------------------------------
# TITLE
# --------------------------------
fig.text(
    0.5, 0.94,
    "SALES & PROFIT INTERACTIVE DASHBOARD",
    ha="center",
    fontsize=20,
    fontweight="bold",
    color=DARK_BLUE
)

# --------------------------------
# KPI CARDS
# --------------------------------

fig.text(
    0.16, 0.82,
    "TOTAL SALES\n₹2,08,000",
    ha="center",
    va="center",
    fontsize=11,
    fontweight="bold",
    color="white",
    bbox=dict(
        boxstyle="round,pad=0.65",
        facecolor=BLUE
    )
)

fig.text(
    0.39, 0.82,
    "TOTAL PROFIT\n₹46,500",
    ha="center",
    va="center",
    fontsize=11,
    fontweight="bold",
    color="white",
    bbox=dict(
        boxstyle="round,pad=0.65",
        facecolor=GREEN
    )
)

fig.text(
    0.61, 0.82,
    "EXPENSES\n₹1,71,500",
    ha="center",
    va="center",
    fontsize=11,
    fontweight="bold",
    color="white",
    bbox=dict(
        boxstyle="round,pad=0.65",
        facecolor=ORANGE
    )
)

fig.text(
    0.84, 0.82,
    "CUSTOMERS\n985",
    ha="center",
    va="center",
    fontsize=11,
    fontweight="bold",
    color="white",
    bbox=dict(
        boxstyle="round,pad=0.65",
        facecolor=PURPLE
    )
)

# --------------------------------
# CHART
# --------------------------------
ax = fig.add_axes([0.09, 0.24, 0.82, 0.47])
ax.set_facecolor("white")


# --------------------------------
# SALES FUNCTION
# --------------------------------
def show_sales(event=None):

    ax.clear()

    colors = [
        BLUE,
        GREEN,
        YELLOW,
        RED,
        PURPLE,
        CYAN
    ]

    ax.bar(
        data["Month"],
        data["Sales"],
        color=colors,
        edgecolor=DARK_BLUE,
        linewidth=1
    )

    ax.set_title(
        "Monthly Sales",
        fontsize=16,
        fontweight="bold",
        color=DARK_BLUE,
        pad=10
    )

    ax.set_xlabel("Month", fontsize=10)
    ax.set_ylabel("Sales (₹)", fontsize=10)

    ax.tick_params(labelsize=9)

    ax.grid(
        axis="y",
        linestyle="--",
        alpha=0.25
    )

    fig.canvas.draw_idle()


# --------------------------------
# PROFIT FUNCTION
# --------------------------------
def show_profit(event=None):

    ax.clear()

    ax.plot(
        data["Month"],
        data["Profit"],
        color=GREEN,
        linewidth=3,
        marker="o",
        markersize=8,
        markerfacecolor=YELLOW,
        markeredgecolor=DARK_BLUE
    )

    ax.fill_between(
        range(len(data)),
        data["Profit"],
        color=GREEN,
        alpha=0.12
    )

    ax.set_xticks(range(len(data)))
    ax.set_xticklabels(data["Month"])

    ax.set_title(
        "Monthly Profit",
        fontsize=16,
        fontweight="bold",
        color=DARK_BLUE,
        pad=10
    )

    ax.set_xlabel("Month", fontsize=10)
    ax.set_ylabel("Profit (₹)", fontsize=10)

    ax.tick_params(labelsize=9)

    ax.grid(
        True,
        linestyle="--",
        alpha=0.25
    )

    fig.canvas.draw_idle()


# --------------------------------
# BUTTONS
# --------------------------------
sales_area = fig.add_axes(
    [0.32, 0.07, 0.14, 0.07]
)

profit_area = fig.add_axes(
    [0.54, 0.07, 0.14, 0.07]
)

btn_sales = Button(
    sales_area,
    "SALES",
    color=BLUE,
    hovercolor=DARK_BLUE
)

btn_profit = Button(
    profit_area,
    "PROFIT",
    color=GREEN,
    hovercolor="#196F3D"
)

btn_sales.on_clicked(show_sales)
btn_profit.on_clicked(show_profit)

# --------------------------------
# SHOW SALES FIRST
# --------------------------------
show_sales()

plt.show()