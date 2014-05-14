/*
 * EncoderOptions.java
 *
 */

package jj2000.j2k.encoder;

import jj2000.j2k.codestream.ProgressionType;
import jj2000.j2k.entropy.encoder.LayersInfo;
import jj2000.j2k.entropy.encoder.MQCoder;
import jj2000.j2k.wavelet.FilterTypes;
import jj2000.j2k.wavelet.analysis.ForwardWT;

/**
 *
 * @author Alberto Aguirre
 */
public class EncoderOptions {
    
    public static final int QTYPE_EXPOUNDED = 1;
    public static final int QTYPE_DERIVED = 2;
    public static final int QTYPE_REVERSIBLE = 3;
    
    public static final int ROI_RECT = 1;
    public static final int ROI_CIRC = 2;
    public static final int ROI_ARBITRARY = 3;  
    
    //General Encoder options;
    public boolean disable_jp2_extension = false;
    public boolean file_format = false;
    public boolean pph_tile = false;
    public boolean pph_main = false;
    public int tile_parts = 0;
    public int tw = 0;
    public int th = 0;
    public int refx = 0;
    public int refy = 0;
    public int trefx = 0;
    public int trefy = 0;
    public float rate = Float.MAX_VALUE;
    public boolean lossless = false;
    public boolean psop = false;
    public boolean peph = false;
    
    public boolean mct = false;
    
    public int ffilters = FilterTypes.W9X7;
    public int wlev = 5;
    public int wwt = ForwardWT.WT_IMPL_FULL;
    public int wcboffx = 0;
    public int wcboffy = 0;
    
    
    public int qtype = QTYPE_EXPOUNDED;
    public float qstep = 0.0078125f;
    public int qguard_bits = 2;
    
    public int roi_type = -1;
    public int[] roi_coord = null;
    public boolean ralign = false;
    public int rstart_level = -1;
    public boolean rno_rect = false;   
    
    public int cblksizx = 64;
    public int cblksizy = 64;
    
    public boolean cbypass = false;
    public boolean cresetMQ = false;
    public boolean cterminate = false;
    public boolean ccausal = false;
    public boolean cseg_symbol = false;
    public int cterm_type = MQCoder.TERM_NEAR_OPT;
    public int clen_calc = MQCoder.LENGTH_NEAR_OPT;  
    public int[] cpp = null;
    
    public int aptype = ProgressionType.LY_RES_COMP_POS_PROG;
    public String alayers = "0.015 +20 2.0 +10";
    //public String alayers = "";
    
    
    
}
