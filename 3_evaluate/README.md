# Introduction

- This is a forked repo of [ESRGAN](https://github.com/xinntao/ESRGAN) by [xinntao](https://github.com/xinntao).
- This repo was adapted to work on a Nvidia P400 on Ubuntu 18.04 x64 with CUDA 10

# Installation
1. `sudo apt install python3 python3-pip git`
2. `sudo apt install cuda nvidia-cuda-toolkit`
3. `pip3 install numpy opencv-python lmdb pyyaml tb-nightly future`
4. `pip3 install torch torchvision`
5. `sudo dpkg --configure -a && sudo apt -f install`
6. `git clone git@github.com:dancingborg/ECU_CSG3303_ESRGAN.git esrgan`

# Reference
<!--
    @article{wang2018esrgan,
        author={Wang, Xintao and Yu, Ke and Wu, Shixiang and Gu, Jinjin and Liu, Yihao and Dong, Chao and Loy, Chen Change and Qiao, Yu and Tang, Xiaoou},
        title={ESRGAN: Enhanced super-resolution generative adversarial networks},
        journal={arXiv preprint arXiv:1809.00219},
        year={2018}
    }
-->    
    @InProceedings{wang2018esrgan,
        author = {Wang, Xintao and Yu, Ke and Wu, Shixiang and Gu, Jinjin and Liu, Yihao and Dong, Chao and Qiao, Yu and Loy, Chen Change},
        title = {ESRGAN: Enhanced super-resolution generative adversarial networks},
        booktitle = {The European Conference on Computer Vision Workshops (ECCVW)},
        month = {September},
        year = {2018}
    }
