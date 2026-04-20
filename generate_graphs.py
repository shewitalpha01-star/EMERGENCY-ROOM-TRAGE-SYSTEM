import matplotlib
matplotlib.use('Agg')   # non-interactive backend — no window needed
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ── colour palette (priority 10 = darkest red, 1 = light green) ──────────────
PRIORITY_COLORS = {
    10: '#8B0000', 9: '#C0392B', 8: '#E74C3C', 7: '#E67E22',
    6:  '#F39C12', 5: '#F1C40F', 4: '#2ECC71', 3: '#27AE60',
    2:  '#1ABC9C', 1: '#16A085'
}

# ── raw data from OUTPUTT.txt ─────────────────────────────────────────────────
priority_distribution = {10:105, 9:105, 8:98, 7:111, 6:91, 5:91, 4:93, 3:94, 2:120, 1:92}
treated_by_priority   = {10:124, 9:127, 8:117, 7:19}
hourly_treated = [15,15,16,17,17,17,16,16,18,17,20,15,13,15,17,16,14,12,18,18,17,15,17,16]

fig = plt.figure(figsize=(20, 22))
fig.patch.set_facecolor('#0D1117')
fig.suptitle('Emergency Room Triage System — Simulation Dashboard',
             fontsize=20, fontweight='bold', color='white', y=0.98)

# ── helper ────────────────────────────────────────────────────────────────────
def style_ax(ax, title):
    ax.set_facecolor('#161B22')
    ax.set_title(title, color='white', fontsize=13, fontweight='bold', pad=10)
    ax.tick_params(colors='#8B949E')
    for spine in ax.spines.values():
        spine.set_edgecolor('#30363D')
    ax.xaxis.label.set_color('#8B949E')
    ax.yaxis.label.set_color('#8B949E')

# ═══════════════════════════════════════════════════════════════════════════════
# 1. Priority Distribution Bar Chart
# ═══════════════════════════════════════════════════════════════════════════════
ax1 = fig.add_subplot(3, 3, 1)
priorities = list(priority_distribution.keys())
counts     = list(priority_distribution.values())
colors     = [PRIORITY_COLORS[p] for p in priorities]
bars = ax1.bar([str(p) for p in priorities], counts, color=colors, edgecolor='#30363D', linewidth=0.8)
for bar, count in zip(bars, counts):
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
             str(count), ha='center', va='bottom', color='white', fontsize=9)
ax1.set_xlabel('Priority Level')
ax1.set_ylabel('Number of Patients')
style_ax(ax1, '1. Initial Patient Priority Distribution (1000 patients)')

# ═══════════════════════════════════════════════════════════════════════════════
# 2. Treated Patients by Priority (Horizontal Bar)
# ═══════════════════════════════════════════════════════════════════════════════
ax2 = fig.add_subplot(3, 3, 2)
tp   = list(treated_by_priority.keys())
tc   = list(treated_by_priority.values())
pct  = [32.0, 32.8, 30.2, 4.9]
tc_colors = [PRIORITY_COLORS[p] for p in tp]
hbars = ax2.barh([f'Priority {p}' for p in tp], tc, color=tc_colors, edgecolor='#30363D')
for bar, count, p in zip(hbars, tc, pct):
    ax2.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
             f'{count}  ({p}%)', va='center', color='white', fontsize=9)
ax2.set_xlabel('Patients Treated')
ax2.set_xlim(0, 160)
style_ax(ax2, '2. Treated Patients by Priority (387 total)')

# ═══════════════════════════════════════════════════════════════════════════════
# 3. Hourly Treatment Line Chart
# ═══════════════════════════════════════════════════════════════════════════════
ax3 = fig.add_subplot(3, 3, 3)
hours = list(range(1, 25))
ax3.plot(hours, hourly_treated, color='#58A6FF', linewidth=2, marker='o',
         markersize=5, markerfacecolor='#1F6FEB')
ax3.fill_between(hours, hourly_treated, alpha=0.2, color='#58A6FF')
peak_h = hourly_treated.index(max(hourly_treated)) + 1
ax3.annotate(f'Peak: Hour {peak_h}\n({max(hourly_treated)} patients)',
             xy=(peak_h, max(hourly_treated)),
             xytext=(peak_h + 2, max(hourly_treated) + 0.5),
             color='#F0E68C', fontsize=8,
             arrowprops=dict(arrowstyle='->', color='#F0E68C'))
ax3.axhline(y=16, color='#FF6B6B', linestyle='--', linewidth=1, label='Avg (16/hr)')
ax3.legend(facecolor='#161B22', labelcolor='white', fontsize=8)
ax3.set_xlabel('Hour of Day')
ax3.set_ylabel('Patients Treated')
ax3.set_xticks(hours)
style_ax(ax3, '3. Hourly Treatment Rate (24-Hour Simulation)')

# ═══════════════════════════════════════════════════════════════════════════════
# 4. Pie Chart — Treated vs Remaining
# ═══════════════════════════════════════════════════════════════════════════════
ax4 = fig.add_subplot(3, 3, 4)
sizes  = [387, 834]
labels = ['Treated (387)', 'Remaining (834)']
pie_colors = ['#2ECC71', '#E74C3C']
wedges, texts, autotexts = ax4.pie(
    sizes, labels=labels, colors=pie_colors,
    autopct='%1.1f%%', startangle=90,
    wedgeprops=dict(edgecolor='#30363D', linewidth=1.5))
for t in texts:    t.set_color('white')
for at in autotexts: at.set_color('white'); at.set_fontsize(10)
ax4.set_title('4. Treated vs Remaining in Queue\n(Total: 1221 patients)',
              color='white', fontsize=13, fontweight='bold', pad=10)
ax4.set_facecolor('#161B22')

# ═══════════════════════════════════════════════════════════════════════════════
# 5. Stacked Bar — Initial vs Treated per Priority
# ═══════════════════════════════════════════════════════════════════════════════
ax5 = fig.add_subplot(3, 3, 5)
treated_full = {p: treated_by_priority.get(p, 0) for p in range(1, 11)}
initial_full = priority_distribution
x = np.arange(1, 11)
init_vals    = [initial_full[p] for p in x]
treated_vals = [treated_full[p] for p in x]
remaining    = [i - t for i, t in zip(init_vals, treated_vals)]
b1 = ax5.bar(x, treated_vals, color=[PRIORITY_COLORS[p] for p in x],
             label='Treated', edgecolor='#30363D')
b2 = ax5.bar(x, remaining, bottom=treated_vals, color='#30363D',
             label='Remaining', edgecolor='#161B22', alpha=0.7)
ax5.set_xlabel('Priority Level')
ax5.set_ylabel('Patients')
ax5.set_xticks(x)
ax5.legend(facecolor='#161B22', labelcolor='white', fontsize=8)
style_ax(ax5, '5. Treated vs Remaining per Priority Level')

# ═══════════════════════════════════════════════════════════════════════════════
# 6. Cumulative Treatments Over 24 Hours
# ═══════════════════════════════════════════════════════════════════════════════
ax6 = fig.add_subplot(3, 3, 6)
cumulative = np.cumsum(hourly_treated)
ax6.step(hours, cumulative, color='#F39C12', linewidth=2, where='post')
ax6.fill_between(hours, cumulative, step='post', alpha=0.15, color='#F39C12')
ax6.set_xlabel('Hour of Day')
ax6.set_ylabel('Cumulative Patients Treated')
ax6.set_xticks(hours)
style_ax(ax6, '6. Cumulative Treatments Over 24 Hours')

# ═══════════════════════════════════════════════════════════════════════════════
# 7. Priority Heatmap — Arrivals by Hour (from patients.csv)
# ═══════════════════════════════════════════════════════════════════════════════
ax7 = fig.add_subplot(3, 1, 3)

# Build heatmap matrix [priority 10..1] x [hour 0..23] from patients.csv data
import csv, os

matrix = np.zeros((10, 24), dtype=int)
csv_path = os.path.join(os.path.dirname(__file__), 'data', 'patients.csv')
with open(csv_path, newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        p = int(row['Priority'])
        h = int(row['Hour'])
        matrix[10 - p][h] += 1   # row 0 = priority 10

im = ax7.imshow(matrix, aspect='auto', cmap='YlOrRd', interpolation='nearest')
ax7.set_xticks(range(24))
ax7.set_xticklabels([f'{h:02d}:00' for h in range(24)], rotation=45, ha='right', fontsize=7)
ax7.set_yticks(range(10))
ax7.set_yticklabels([f'Priority {p}' for p in range(10, 0, -1)], fontsize=9)
cbar = plt.colorbar(im, ax=ax7, orientation='vertical', pad=0.01)
cbar.set_label('Patient Count', color='white')
cbar.ax.yaxis.set_tick_params(color='white')
plt.setp(cbar.ax.yaxis.get_ticklabels(), color='white')
# annotate cells
for i in range(10):
    for j in range(24):
        if matrix[i][j] > 0:
            ax7.text(j, i, str(matrix[i][j]), ha='center', va='center',
                     fontsize=6, color='black' if matrix[i][j] > 3 else 'white')
style_ax(ax7, '7. Patient Arrival Heatmap — Priority × Hour of Day')

# ── final layout ──────────────────────────────────────────────────────────────
plt.tight_layout(rect=[0, 0, 1, 0.97])
out_path = os.path.join(os.path.dirname(__file__), 'data', 'simulation_dashboard.png')
plt.savefig(out_path, dpi=150, bbox_inches='tight', facecolor='#0D1117')
print(f"Dashboard saved → {out_path}")
