# GAN-Generative Adverserial Network
 Learns a mapping from input images to output images.
 
 ## Datasets

The data format used by this program is the same as the original pix2pix format, which consists of images of input and desired output side by side like:

<img src="https://lh3.googleusercontent.com/hiSbZ5vinjoIteBMdcO0OLHvkzlQ1bUjhGAozjuIKOL_U6o8w-PgOOzEqELNsSVbMp7hBA=s170" width="256px"/>

The input and output image can be merged resized with corresponding output samples or just white image for testing can be made from small python snippets from ``files`` folder.

## Folder Format
  The images are to be placed into folder ``dataset`` containing another folder specifying the model name (eg:``pokemon``)
  The test inputs are to be placed in ``val`` folder.

## Training And Testing

```sh
# train the model
python python main.py  --mode train 

# test the model
python python main.py --phase test 
```

## Citation
If you use this code for your research, please cite the paper this code is based on: <a href="https://arxiv.org/pdf/1611.07004v1.pdf">Image-to-Image Translation Using Conditional Adversarial Networks</a>:

```
@article{pix2pix2016,
  title={Image-to-Image Translation with Conditional Adversarial Networks},
  author={Isola, Phillip and Zhu, Jun-Yan and Zhou, Tinghui and Efros, Alexei A},
  journal={arxiv},
  year={2016}
}
```
