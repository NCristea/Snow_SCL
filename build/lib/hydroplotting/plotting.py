import matplotlib.pyplot as plt
from matplotlib import gridspec
import numpy as np

def plotSWE_P_T(t, sP, sSWE, sT, time_period):
    fig = plt.figure()
    gs = gridspec.GridSpec(2, 1, height_ratios=[1, 2])

    # SWE plot
    ax = plt.subplot(gs[1])
    ax.plot(t, sSWE, color = 'red')
    # Create secondary axes
    ax2 = ax.twinx()
    c = 'orange'
    ax2.bar(t, -sP, color = c)

    # Now need to fix the axis labels
    max_pre = max(sP)
    y2_ticks = np.linspace(0, int(max_pre), int(max_pre + 1))
    #y2_ticks = np.int(y2_ticks)

    y2_ticklabels = [str(i) for i in y2_ticks]
    ax2.set_yticks(-1 * y2_ticks)
    ax2.set_yticklabels(y2_ticklabels)

    ax.set_xlim(time_period)

    ax.set_ylabel('SWE[unit]', color='k')
    ax2.set_ylabel('P[unit]', color='k')
    ax.set_xlabel('Time [day]')

    ax.tick_params(axis='y', colors='k')
    ax.xaxis.grid(visible = None, which='major', color ='.7', linestyle='-')
    ax.yaxis.grid(visible = None, which='major', color ='.7', linestyle='-')
    ax.set_xlim(min(t), max(t))
    ax.set_ylim(0, np.nanmax(sSWE)*1.2)
    ax.set_xlim(time_period)
    ax.tick_params(axis='x', labelrotation = 45)
    # temperature plot
    ax2 = plt.subplot(gs[0])

    ax2.plot(t, sT)
    ax2.xaxis.grid(visible = None, which='major', color='.7', linestyle='-')
    ax2.yaxis.grid(visible = None, which='major', color='0.7', linestyle='-')
    ax2.set_ylabel('T(deg C)')
    ax2.set_xlim(min(t), max(t))
    plt.setp(ax2.get_xticklabels(), visible=False)

    plt.tight_layout()
    #ax2.invert_yaxis()
    plt.gcf().subplots_adjust(bottom=0.15)
    ax2.set_xlim(time_period)
    #ax2.set_xticklabels(ax2.get_xticks(), rotation = 45)
    plt.show()
    #plt.savefig(filename,format='pdf')
    plt.close(fig)