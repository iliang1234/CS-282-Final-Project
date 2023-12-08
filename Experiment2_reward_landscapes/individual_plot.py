"""
Plotting functions
Hao et. al, 2018, Loss Landscape research
"""
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize

import h5py
import argparse
import numpy as np
from os.path import exists
import seaborn as sns
import pdb

## helper functions to read in output values from colab
def remove_chars(input_str):
  input_str = input_str.replace('[', '')  
  input_str = input_str.replace(']', '')
  input_str = input_str.replace(',', '')
  return input_str

def read_2d_array_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        two_d_array = []
        
        for line in lines:
            stripped = line.strip().split()
            cleaned_stripped = [remove_chars(string) for string in stripped]
            # pdb.set_trace()

            elements = [float(e) for e in cleaned_stripped]
            two_d_array.append(elements)
            
    return two_d_array

REWARDS = read_2d_array_from_file('all_rewards_mce.txt')


def plot_d_contour(surf_file, surf_name='train_loss', vmin=0.1, vmax=10, vlevel=0.5, show=False):
    """Plot 2D contour map and 3D surface."""

    f = h5py.File(surf_file, 'r')
    x = np.array(f['xcoordinates'][:])
    y = np.array(f['ycoordinates'][:])
    X, Y = np.meshgrid(x, y)

    iterations = [0,2,5,10,15,20, 30, 50,70, 100,150, 200,250, 300, 389]
    for i in iterations:
        assert surf_name in f.keys()
        # replace with our values
        Z = np.array(REWARDS[i]).reshape((10, 10))
        # cut to 100 by 100
        print("z shape: ", Z.shape)

        print(Z)

        if (len(x) <= 1 or len(y) <= 1):
            print('The length of coordinates is not enough for plotting contours')
            return

        # --------------------------------------------------------------------
        # Plot 3D surface
        # --------------------------------------------------------------------
        print("reached plotting 3-d surface")
        fig = plt.figure()
        ax = Axes3D(fig)
        ## set legend
        cmap = plt.get_cmap('inferno') 
        norm = Normalize(vmin=0, vmax=2.45) 
        scalar_map = cm.ScalarMappable(cmap=cmap, norm=norm)
        scalar_map.set_array([]) 
        ##

        surf = ax.plot_surface(X, Y, Z, facecolors=cmap(norm(Z)), linewidth=0, antialiased=False)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Reward Values')
        ax.set_zlim3d(0, 2.45)
        # fig.colorbar(surf, shrink=0.5, aspect=5)
        fig.colorbar(scalar_map)
        fig.savefig('mce_rewards_3d_iter' + str(i) + '.pdf', dpi=300,
                    bbox_inches='tight', format='pdf')

    f.close()
    print("finished 3d surface")
    # if show: plt.show()
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plot 2D loss surface')
    parser.add_argument('--surf_file', '-f', default='', help='The h5 file that contains surface values')
    parser.add_argument('--dir_file', default='', help='The h5 file that contains directions')
    parser.add_argument('--proj_file', default='', help='The h5 file that contains the projected trajectories')
    parser.add_argument('--surf_name', default='train_loss', help='The type of surface to plot')
    parser.add_argument('--vmax', default=10, type=float, help='Maximum value to map')
    parser.add_argument('--vmin', default=0.1, type=float, help='Miminum value to map')
    parser.add_argument('--vlevel', default=0.5, type=float, help='plot contours every vlevel')
    parser.add_argument('--zlim', default=10, type=float, help='Maximum loss value to show')
    parser.add_argument('--show', action='store_true', default=False, help='show plots')

    args = parser.parse_args()

    if exists(args.surf_file) and exists(args.proj_file) and exists(args.dir_file):
        plot_contour_trajectory(args.surf_file, args.dir_file, args.proj_file,
                                args.surf_name, args.vmin, args.vmax, args.vlevel, args.show)
    elif exists(args.proj_file) and exists(args.dir_file):
        plot_trajectory(args.proj_file, args.dir_file, args.show)
    elif exists(args.surf_file):
        plot_2d_contour(args.surf_file, args.surf_name, args.vmin, args.vmax, args.vlevel, args.show)
