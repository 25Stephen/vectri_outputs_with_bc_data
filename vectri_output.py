import xarray as xr
import matplotlib.pyplot as plt
from cartopy import crs, feature
import glob
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
from matplotlib.gridspec import SubplotSpec

lon_formatter = LongitudeFormatter(zero_direction_label=True)
lat_formatter = LatitudeFormatter()
bounds = [-3.3, 1.2, 4.5, 11.5]
def set_fig_params(axes):
    for i,j in enumerate(axes):
    # for i in (range(0,len(axes))):
        axes[i].set_extent(bounds)
        axes[i].add_feature(feature.COASTLINE)
        axes[i].add_feature(feature.BORDERS)
        axes[i].add_feature(feature.STATES, linewidth = 0.2)
        axes[i].set_xticks([-3,-2,-1,0,1.2], crs=crs.PlateCarree())
        axes[i].set_yticks([11,10,9,8,7,6], crs=crs.PlateCarree())
        lon_formatter = LongitudeFormatter(zero_direction_label=True)
        lat_formatter = LatitudeFormatter()
        axes[i].xaxis.set_major_formatter(lon_formatter)
        axes[i].yaxis.set_major_formatter(lat_formatter)
        
def create_subtitle(fig: plt.Figure, grid: SubplotSpec, title: str):
    row = fig.add_subplot(grid)
    row.set_title(f'{title}\n', fontweight='semibold')#) if row==1 else row.set_title(f'{title}')
    # if row==0 row.set_title(f'{title}\n\n\n', fontweight='semibold') else row.set_title(f'{title}\n'
    row.set_frame_on(False)
    row.axis('off')
path1 = '/media/kenz/1B8D1A637BBA134B/Data/calculated/'

#### Load data
mt_mpi = glob.glob(path1+'trans_MPI-M-MPI-ESM-LR_rcp*_GERICS-REMO2015_*.nc')
mt_nor = glob.glob(path1+'trans_NCC-NorESM1-M_rcp*_GERICS-REMO2015_*.nc')

vec = xr.open_dataset(path1+'VECTRI_GHA-22_NCC-NorESM1-M_rcp26_r1RICS-REMO2015.nc')
