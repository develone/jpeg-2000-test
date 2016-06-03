from myhdl import *
from PIL import Image # Part of the standard Python Library

import waveletsim_53 as dwt
import waveletsim as f_dwt
class JPEGEnc2k(object):

    def __init__(self):
        """
        """
  
        # @todo: the following parameters should be part of the args
        self.pixel_nbits = 24
        ''' T1 ,T2, omega1 and  omega2 
        [0,0] [0,1] [0,2][0,3] [0,4] [0,5]
        [1,0] [1,1] [1,2][1,3] [1,4] [1,5]
        [2,0] [2,1] [2,2][2,3] [2,4] [2,5]

        N1 number rows in tile , N2  number columns in Tile
        required to cover the image area'''
        self.T1 = 0
        self.T2 = 0
        self.N1 = 8
        self.N2 = 8
        self.omega1 = 0
        self.omega2 = 0
        self.tile = [self.T1, self.T2]
        self.tiles  = (self.N1,self.N2,)
        self.origin = (self.omega1, self.omega2)
        self.filter = [5,3]
        self.img_fn = ""
        self.mode = ""
        self.width = 0
        self.height = 0
        self.r_subband = []
        self.g_subband = []
        self.b_subband = []
        self.dwt_level = 3
        #self.gr_subband = []
        self.max_frame_rate = 0
        '''
        self.clock = clock
        self.reset = reset
        '''
    def get_filter(self):
        return self.filter

    def set_filter(self, val):
        self.filter  = val

    def get_dwt_level(self):
        return self.dwt_level

    def set_dwt_level(self, val):
        self.dwt_level  = val

    def get_img(self):
        return self.img

    def get_pix(self):
        return self.pix

    def get_gr_subband(self):
        return self.gr_subband

    def get_r_subband(self):
        return self.r_subband

    def get_g_subband(self):
        return self.g_subband

    def get_b_subband(self):
        return self.b_subband

    def get_mode(self):
        return self.mode

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def set_mode(self, str):
        self.mode = str

    def get_img_fn(self):
        return self.img_fn
 
    def set_img_fn(self, str):
        self.img_fn = str

    def get_tile(self):
        #print self.tile, type(self.tile)
        return self.tile

    '''tile is a list'''
    def set_tile(self,val1, val2):
        self.T1 = val1
        self.T2 = val2
        self.tile = [self.T1, self.T2]

    def get_tiles(self):
        #print self.tiles
        return self.tiles

    def get_origin(self):
        return self.origin

    '''tile_size is a tuple'''
    def set_tiles_N1_N2(self,val1, val2):
        #print val1, val2
        self.N1 = val1
        self.N2 = val2
        self.tiles  = (self.N1,self.N2,) 
        #print self.N1, self.N2, self.tiles, type(self.tiles)

    '''origin is a tuple'''
    def set_origin_omega1_omega2(self,val1, val2):
        #print val1, val2
        self.omega1 = val1
        self.omega2 = val2
        self.origin  = (self.omega1,self.omega2,) 
        #print self.omega1, self.omega2, self.origin, type(self.origin)
 
    def read_image_file(self):
        if (self.img_fn == ""):
            print "img_fn is not set:"
            print "use jp2k.set_img_fn(filename)"
        else:
            self.img = Image.open(self.img_fn)
            self.mode = self.img.mode
            self.width, self.height = self.img.size
            print self.mode, self.width, self.height

            if (self.mode == "RGB"):
               rgb = list(self.img.getdata())
               self.pix = self.img.load()
                
               """get r g b from rgb"""
               for n in range(len(rgb)):
                  rr, gg, bb = rgb[n]
                  self.r_subband.append(rr)
                  self.g_subband.append(gg)
                  self.b_subband.append(bb)
               #print rgb,len(rgb)
               for n in range(len(rgb)):
                   r,g,b = rgb[n]
                   print r
               for n in range(len(rgb)):
                   r,g,b = rgb[n]
                   print g
               for n in range(len(rgb)):
                   r,g,b = rgb[n]
                   print b
               self.r_subband = [self.r_subband[i:i+self.img.size[0]] for i in range(0, len(self.r_subband), self.img.size[0])]
               self.g_subband = [self.g_subband[i:i+self.img.size[0]] for i in range(0, len(self.g_subband), self.img.size[0])]
               self.b_subband = [self.b_subband[i:i+self.img.size[0]] for i in range(0, len(self.b_subband), self.img.size[0])]
               '''int 5/3 dwt or floating point 9/7 data required'''
               if (self.filter[0] == 9):
                   for row in range(0, len(self.r_subband)):
                       for col in range(0, len(self.r_subband[0])):
                           self.r_subband[row][col] = float(self.r_subband[row][col])
                           self.g_subband[row][col] = float(self.g_subband[row][col])
                           self.b_subband[row][col] = float(self.b_subband[row][col])
                   print 'Red', len(self.r_subband[0]), len(self.r_subband[1])
                   print 'Green', len(self.g_subband[0]),len(self.g_subband[1])
                   print 'Blue', len(self.b_subband[0]),len(self.b_subband[1])
               
        
            else:
                  
                  self.gr_subband = list(self.img.getdata())
                  self.pix = self.img.load()
                  self.gr_subband = [self.gr_subband[i:i+self.img.size[0]] for i in range(0, len(self.gr_subband), self.img.size[0])] 
                  if (self.filter[0] == 9):
                     for row in range(0, len(self.gr_subband)):
                        for col in range(0, len(self.gr_subband[0])):
                            self.gr_subband[row][col] = float(self.gr_subband[row][col])
                  print 'Gray', len(self.gr_subband[0]), len(self.gr_subband[1])

    def col_dwt(self,cc):
        #print cc
        for row in range(2, self.get_height(), 2):
            #print cc, row-1, row, row + 1, self.fwd_gr[row-1][cc], self.fwd_gr[row][cc], self.fwd_gr[row+1][cc]
            self.fwd_gr[row][cc] = (self.fwd_gr[row][cc] - ((int(self.fwd_gr[row-1][cc])>>1) + (int(self.fwd_gr[row+1][cc])>>1))) 
            #print self.fwd_gr[row][cc]      
        for row in range(1, self.get_height()-1, 2):
            #print cc, row-1, row, row + 1, self.fwd_gr[row-1][cc], self.fwd_gr[row][cc], self.fwd_gr[row+1][cc]
            self.fwd_gr[row][cc] = (self.fwd_gr[row][cc] + (2 + (int(self.fwd_gr[row-1][cc])) + (int(self.fwd_gr[row+1][cc]))>>2)) 
            #print self.fwd_gr[row][cc] 

    def fwd_dwt(self):
        print "forward dwt using file ", self.img_fn, "dwt_level", self.dwt_level, "dwt_filter", self.filter
        if (self.mode == "RGB"):
            self.fwd_r = self.r_subband
            self.fwd_g = self.g_subband
            self.fwd_b = self.b_subband 
            self.fwd_r = dwt.fwt97_2d(self.fwd_r, self.dwt_level)
            self.fwd_g = dwt.fwt97_2d(self.fwd_g, self.dwt_level)
            self.fwd_b = dwt.fwt97_2d(self.fwd_b, self.dwt_level)
            rgb = []
            for row in range(len(self.fwd_r)):
                for col in range(len(self.fwd_r)):
                    rgb.append((self.fwd_r[row][col],self.fwd_g[row][col],self.fwd_b[row][col]))
            for row in range(len(self.fwd_r)):
                for col in range(len(self.fwd_r)):
                    #pix[row,col] = rgb[col + row*128]
                    self.pix[col,row] = rgb[col + row*len(self.fwd_r)] 
        else:
            self.fwd_gr = self.gr_subband
            #'''
            # Not calling the waveletsim_53 fwt97_2d
            # Instead using the a local function which performs 1 col at time
            print 'performing 1 column at a time'
            for ccc in range(self.get_width()):
                self.col_dwt(ccc)
            self.fwd_gr = dwt.de_interleave(self.fwd_gr,self.get_height(),self.get_width())
            for ccc in range(self.get_width()):
                self.col_dwt(ccc)
            self.fwd_gr = dwt.de_interleave(self.fwd_gr,self.get_height(),self.get_width())
            self.fwd_gr = dwt.lower_upper(self.fwd_gr,self.get_height(),self.get_width())
            '''
            self.fwd_gr = dwt.fwt97_2d(self.fwd_gr, self.dwt_level)
            '''
            dwt.seq_to_img(self.fwd_gr, self.pix)
           

    def fwd_f_dwt(self):
        print "forward dwt using file ", self.img_fn, "dwt_level", self.dwt_level, "dwt_filter", self.filter
        if (self.mode == "RGB"):
            self.fwd_r = self.r_subband
            self.fwd_g = self.g_subband
            self.fwd_b = self.b_subband 
            self.fwd_r = f_dwt.fwt97_2d(self.fwd_r, self.dwt_level)
            self.fwd_g = f_dwt.fwt97_2d(self.fwd_g, self.dwt_level)
            self.fwd_b = f_dwt.fwt97_2d(self.fwd_b, self.dwt_level)
            rgb = []
            for row in range(len(self.fwd_r)):
                for col in range(len(self.fwd_r)):
                    rgb.append((self.fwd_r[row][col],self.fwd_g[row][col],self.fwd_b[row][col]))
            for row in range(len(self.fwd_r)):
                for col in range(len(self.fwd_r)):
                    #pix[row,col] = rgb[col + row*128]
                    self.pix[col,row] = rgb[col + row*len(self.fwd_r)] 
        else:
            self.fwd_gr = self.gr_subband

            self.fwd_gr = f_dwt.fwt97_2d(self.fwd_gr, self.dwt_level)
            dwt.seq_to_img(self.fwd_gr, self.pix)
            
