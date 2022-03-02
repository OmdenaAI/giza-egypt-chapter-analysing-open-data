
from typing import Optional
import datetime
import matplotlib
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap, addcyclic
import numpy as np

try:
    path = r'C:\\Users\\oeb\\AppData\\Local\\Programs\\FFmpeg\\bin\\ffmpeg.exe'
    matplotlib.rcParams['animation.ffmpeg_path'] = path
except:
    pass

def int_datetime(tit:int)->str:
    
    tit = str(tit)
    day   = tit[6:-2]
    month = tit[4:-4]
    year  = tit[0:-6]
    date = year+'-'+month+'-'+day
    return date

def get_titles(lis:list([int]),
    )->list([datetime.datetime]):
    
    titles = map(lambda x:int_datetime(x) ,lis)
    titles = map(lambda x:datetime.datetime.strptime(x,"%Y-%m-%d") 
        ,titles)
    
    return list(titles)

def get_str_titles(lis:list([int]),
    label:str,
    )->list([str]):
    
    titles = map(lambda x: label +int_datetime(x) ,lis)
    
    return list(titles)

def adder(a:float,per:float)->float:
    return a + per

def reduce_list(lis:list,
    values: Optional[int]=3,
        )->list:
    lis = lis[~np.isnan(lis)]
    
    high = round(float(lis.max()),2)
    low  = round(float(lis.min()),2)
    mid  = round( (low+high)/2.0 ,2)
    
    per  = round(0.01*low,2)
    low  = round(adder(low, per),2)
    # negative
    high = round(adder(high,-1* per),2)
    reduced = [low, mid, high]
    return reduced

class Maps():

    def __init__(self,
            grad_va:int=400,
            grad_victor:int=70,
            #proj_res: Optional[str] = None,
            proj_res: str = 'h',
            ):
        self.grad_victor = grad_victor
        self.proj_res = proj_res
        self.grad_va = grad_va
        self.cmap = 'RdBu_r'
        self.cs_grad = None
        self.cbar = None
        self.map_ = None
        self.fig = None
        self.cs = None
        self.x = None
        self.y = None

    def _setup(self,
        fig_size:tuple((int,int)))->None:
        # set 
        fig = plt.figure(figsize=fig_size,
            facecolor=None,
            frameon=False,
            dpi = 1920 / max(fig_size) )

        ax = fig.add_subplot()
        ax.set_facecolor(color=None)
        fig.patch.set_alpha(0.0)
        self.fig = fig
        return fig

    def _map_init(self,
            records_values:list,
            longs_values:list,
            lats_values:list,
            lat_0:float = 30.8,
            width:float = 0.35E6,
            lon_0:float = 31.24,
            height:float= 0.299E6):

        self.map_ = Basemap(projection='lcc', resolution=self.proj_res,
            lat_0=lat_0, lon_0=lon_0,
            width=width, height=height);

        self.map_.shadedrelief();
        temp_cyclic, lons_cyclic = addcyclic(records_values, longs_values);
        # Create 2D lat/lon arrays for Basemap
        lon2d, lat2d = np.meshgrid(lons_cyclic, lats_values);
        # Transforms lat/lon into plotting coordinates for projection
        x, y = self.map_(lon2d, lat2d);
        self.x = x
        self.y = y
        return temp_cyclic

    def plot(self,
        records_values:list,
        longs_values:list,
        lats_values:list,
        plot_title:str,
        cbar_label:str,
        lat_0:float = 30.8,
        width:float = 0.35E6,
        lon_0:float = 31.24,
        height:float= 0.299E6,
        fig_size:tuple((int,int))= (10,10),
        cbar_title:str='temp in ⁰c',
        cmap:str = 'RdBu_r',
        animation_res: Optional [int] = 1920,
            )->None:

        self.fig = self._setup(fig_size)
        temp_cyclic = self._map_init(records_values=records_values,
            longs_values=longs_values,
            lats_values=lats_values,lat_0=lat_0,
            width=width,lon_0=lon_0,height=height
        )
        
        cmap = plt.cm.get_cmap(cmap)
        # drawing contours
        self.cs = self.map_.contourf(self.x, self.y, temp_cyclic, self.grad_va, cmap=cmap)
        self.cs_grad = self.map_.contour(self.x, self.y, temp_cyclic, self.grad_victor,
                linewidths=0.05, colors='k')
        self.cbar = plt.colorbar(self.cs, shrink=0.7)
        
        # cbar labels
        labels = reduce_list(records_values)
        self.cbar.set_ticks(ticks=labels,labels=labels)
        self.cbar.set_label(cbar_title,color='black',)
        # plot title
        plt.title(plot_title)
        return

    def cleaner(self)->None:
        def clean(lis):
            [i.remove() for i in lis]

        [clean(c.collections) for c in [self.cs_grad,self.cs]]
        self.cbar.remove()
    
    def animate(self,
        records_values:list([list([float])]),
        longs_values:list,
        lats_values:list,
        plot_titles:list([str]),
        cbar_label:str,
        lat_0:float = 30.8,
        width:float = 0.35E6,
        lon_0:float = 31.24,
        height:float= 0.299E6,
        fig_size:tuple((int,int))= (10,10),
        cbar_title:str='temp in ⁰c',
        cmap:str = 'RdBu_r',
        animation_res:int = 1920,
        interval:int=100,
        animation_vid_name:str='anim.mp4',
        )->animation:

        cmap = plt.cm.get_cmap(self.cmap)
        
        def update(frame,):
            # clean figure
            self.cleaner()
            
            # drawing contours
            temp_cyclic, lons_cyclic = addcyclic(records_values[frame], longs_values);

            self.cs = self.map_.contourf(self.x, self.y, temp_cyclic,self.grad_va, cmap=cmap);
            self.cs_grad = self.map_.contour(self.x ,self.y,temp_cyclic,self.grad_victor,
                    linewidths=0.05,colors='k');
            self.cbar = plt.colorbar(self.cs, shrink=0.7);

            # cbar labels
            labels = reduce_list(records_values[frame])
            self.cbar.set_ticks(ticks=labels,labels=labels) 
            self.cbar.set_label(cbar_title,color='black',);
            # plot title
            plt.title(plot_titles[frame])

            return
        # init
        self.plot(
            records_values=records_values[0],
            longs_values=longs_values,
            lats_values=lats_values,
            plot_title=plot_titles[0],
            cbar_label=cbar_label,
            lat_0=lat_0,width=width,
            lon_0=lon_0,height=height,
            fig_size=fig_size,
            cbar_title=cbar_title,
            cmap=cmap,
            animation_res=animation_res,
            )
        frms = len(records_values)
        anim = animation.FuncAnimation(self.fig, update,
                                    frames=frms,interval=interval, blit=False)
        writervideo = animation.FFMpegWriter()
        
        anim.save(animation_vid_name, writer=writervideo,
                savefig_kwargs={'transparent': True, 'facecolor': None})
        
        return anim