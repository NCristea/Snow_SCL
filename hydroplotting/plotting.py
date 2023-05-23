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

def plotSWE_P_T_Q(t, sP, sSWE, sT, sQ, time_period):
    fig = plt.figure()
    #gs = gridspec.GridSpec(2, 1, height_ratios=[1, 2])
    gs = gridspec.GridSpec(3, 1, height_ratios=[1, 2, 1])

    # SWE plot
    ax = plt.subplot(gs[1])

    ax.plot(t, sSWE, color="r")
    # Create secondary axes
    ax2 = ax.twinx()
    ax2.bar(t, -sP, color=['black'])

    # fix the axis labels
    #convert P to mm/day

    max_pre = max(sP)

    #y2_ticks = np.linspace(0, max_pre, max_pre + 1)

    #y2_ticks = np.rint(y2_ticks)

    #y2_ticklabels = [str(i) for i in y2_ticks]

    #ax2.set_yticks(-1 * y2_ticks)
    #ax2.set_yticklabels(y2_ticklabels)

    ax.set_xlim(time_period)

    ax.set_ylabel('SWE[m]', color='k')

    ax2.set_ylabel('P[mm/day]', color='k')

    ax.tick_params(axis='y', colors='k')
    ax.xaxis.grid(visible=None, which='major', color='.7', linestyle='-')
    ax.yaxis.grid(visible=None, which='major', color='.7', linestyle='-')
    ax.set_xlim(min(t), max(t))

    ax.set_ylim(0, 0.8)

    #ax.set_ylim(0, np.nanmax(sSWE)*1.2)
    ax.set_xlim(time_period)
    plt.setp(ax.get_xticklabels(), visible=False)
    # temperature plot

    ax2 = plt.subplot(gs[0])

    ax2.plot(t, sT)
    ax2.xaxis.grid(visible=None, which='major', color='.7', linestyle='-')
    ax2.yaxis.grid(visible=None, which='major', color='0.7', linestyle='-')
    ax2.set_ylabel('T [deg C]')
    ax2.set_xlim(min(t), max(t))
    plt.setp(ax2.get_xticklabels(), visible=False)
    ax2.set_xlim(time_period)

    ax2 = plt.subplot(gs[2])

    sQ_p = sQ.loc[t]

    ax2.plot(t, sQ_p)
    ax2.xaxis.grid(visible=None, which='major', color='.9', linestyle='-')
    ax2.yaxis.grid(visible=None, which='major', color='0.9', linestyle='-')
    ax2.set_ylabel('Q [cms])')
    ax2.set_xlim(min(t), max(t))
    ax2.set_xlabel('Time')
    ax2.tick_params(axis='x', labelrotation=45)

    plt.tight_layout()
    #ax2.invert_yaxis()
    plt.gcf().subplots_adjust(bottom=0.15)
    ax2.set_xlim(time_period)
    #ax3.set_xlim(time_period)
    #ax2.set_xticklabels(ax2.get_xticks(), rotation = 45)
    plt.show()
    #plt.style.use('seaborn-paper')
    #plt.savefig(filename,format='pdf')
    plt.close(fig)

def plotSWE_P_T_Q_model(t, sP, sSWE, sT, sQ, tQm, sQm, time_period):
    fig = plt.figure()
    #gs = gridspec.GridSpec(2, 1, height_ratios=[1, 2])
    gs = gridspec.GridSpec(3, 1, height_ratios=[1, 2, 1])

    # SWE plot
    ax = plt.subplot(gs[1])

    ax.plot(t, sSWE, color="r")
    # Create secondary axes
    ax2 = ax.twinx()
    ax2.bar(t, -sP, color=['black'])

    # fix the axis labels
    #convert P to mm/day

    max_pre = max(sP)

    #y2_ticks = np.linspace(0, max_pre, max_pre + 1)

    #y2_ticks = np.rint(y2_ticks)

    #y2_ticklabels = [str(i) for i in y2_ticks]

    #ax2.set_yticks(-1 * y2_ticks)
    #ax2.set_yticklabels(y2_ticklabels)

    ax.set_xlim(time_period)

    ax.set_ylabel('SWE[m]', color='k')

    ax2.set_ylabel('P[mm/day]', color='k')

    ax.tick_params(axis='y', colors='k')
    ax.xaxis.grid(visible=None, which='major', color='.7', linestyle='-')
    ax.yaxis.grid(visible=None, which='major', color='.7', linestyle='-')
    ax.set_xlim(min(t), max(t))

    ax.set_ylim(0, 0.8)

    #ax.set_ylim(0, np.nanmax(sSWE)*1.2)
    ax.set_xlim(time_period)
    plt.setp(ax.get_xticklabels(), visible=False)
    # temperature plot

    ax2 = plt.subplot(gs[0])

    ax2.plot(t, sT)
    ax2.xaxis.grid(visible=None, which='major', color='.7', linestyle='-')
    ax2.yaxis.grid(visible=None, which='major', color='0.7', linestyle='-')
    ax2.set_ylabel('T [deg C]')
    ax2.set_xlim(min(t), max(t))
    plt.setp(ax2.get_xticklabels(), visible=False)
    ax2.set_xlim(time_period)

    ax2 = plt.subplot(gs[2])

    sQ_p = sQ.loc[t]
    sQm_p = sQm.loc[tQm]

    ax2.plot(t, sQ_p)
    ax2.plot(tQm, sQm_p)
    ax2.xaxis.grid(visible=None, which='major', color='.9', linestyle='-')
    ax2.yaxis.grid(visible=None, which='major', color='0.9', linestyle='-')
    ax2.set_ylabel('Q [cms])')
    ax2.set_xlim(min(t), max(t))
    ax2.set_xlabel('Time')
    ax2.tick_params(axis='x', labelrotation=45)
    ax2.legend(['simulated', 'observed'])

    plt.tight_layout()
    #ax2.invert_yaxis()
    plt.gcf().subplots_adjust(bottom=0.15)
    ax2.set_xlim(time_period)
    #ax3.set_xlim(time_period)
    #ax2.set_xticklabels(ax2.get_xticks(), rotation = 45)
    plt.show()
    #plt.style.use('seaborn-paper')
    #plt.savefig(filename,format='pdf')
    plt.close(fig)

#%%
