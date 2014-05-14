/*
 * DecoderOptions.java
 *
 */

package jj2000.j2k.decoder;

/**
 *
 * @author Alberto Aguirre
 */
public class DecoderOptions {
    /**
     * The resolution level at which to reconstruct the image(0 means the lowest
     * available resolution whereas the maximum resolution level corresponds to
     * the original image resolution. If the given index is greater than the
     * number of available resolution levels of the compressed image,
     * the image is reconstructed at its highest resolution (among all
     * tile-components). Note that this option affects only the inverse wavelet
     * transform and not the number of bytes read by the codestream parser:
     * this number of bytes depends only on options nbytes or rate.
     */
    public int res_lev = -1;
    
    /**
     * Specifies the decoding rate in bits per pixel (bpp) where the number of
     * pixels is related to the image's original size (Note: this number is not
     * affected by the '-res' option). If it is equal to -1, the whole
     * codestream is decoded. The codestream is either parsed (default) or
     * truncated depending on the option 'parsing'. To specify the decoding
     * rate in bytes, use the 'nbytes' option instead.
     */
    public float rate = -1;
    
    /**
     *Specifies the decoding rate in bytes. The codestream is either parsed
     * (default) or truncated depending option 'parsing'. To specify the
     * decoding rate in bits per pixel, use the 'rate' option instead.
     * If it's equal to -1, the rate option will be used instead
     * Default = -1;
     */
    public int nbytes = -1;
    
    /**
     * Enable or not the parsing mode when decoding rate is specified
     * ('nbytes' or 'rate' options). If it is false, the codestream is decoded
     * as if it were truncated to the given rate. If it is true, the decoder
     * creates, truncates and decodes a virtual layer progressive codestream
     * with the same truncation points in each code-block.
     */
    public boolean parsing = true;
    
    /**
     * Specifies the maximum number of code blocks to use. Use the ncb
     * and lbody quit conditions. If state information is found for more code
     * blocks than is indicated with this option, the decoder will decode using
     * only information found before that point. Using this otion implies that
     * the 'rate' or 'nbyte' parameter is used to indicate the lbody parameter
     * which is the number of packet body bytes the decoder will decode.
     */
    public int ncb_quit = -1;
    
    /**
     * Specifies the maximum number of layers to decode for any codeblock"
     */
    public int l_quit = -1;
    
    /**
     * Specifies the maximum number of bit planes to decode for any code-block.
     */
    public int m_quit = -1;
    
    /**
     * Specifies the whether the decoder should only decode code-blocks included
     * in the first progression order.
     */
    public boolean poc_quit = false;
    
    /**
     * Specifies whether the decoder should only decode the first tile part of 
     * each tile.
     */
    public boolean one_tp = false;
    
    /**
     * Specifies whether the component transform indicated in the codestream 
     * should be used.
     */
   public boolean comp_transf = true;
   
   /**
    * Ignore any colorspace information in the image.
    */
   public boolean nocolorspace = false;             
   
   /**
    * Specifies if error detection should be performed by the entropy decoder 
    * engine. If errors are detected they will be concealed and the resulting 
    * distortion will be less important. Note that errors can only be detected 
    * if the encoder that generated the data included error resilience 
    * information.
    */
   public boolean cerror = true;
   
   /**
    * This argument makes sure that the no ROI de-scaling is performed. 
    * Decompression is done like there is no ROI in the image.
    */
   public boolean rno_roi = false;  

}
