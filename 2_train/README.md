# Introduction

- This is a forked repo of [BasicSR](https://github.com/xinntao/BasicSR) by [xinntao](https://github.com/xinntao).
- This repo was adapted to work on a Nvidia P400 on Ubuntu 18.04 x64 with CUDA 10

# Installation
1. `sudo apt install python3 python3-pip git`
2. `sudo apt install cuda nvidia-cuda-toolkit`
3. `pip3 install numpy opencv-python lmdb pyyaml tb-nightly future`
4. `pip3 install torch torchvision`
5. `sudo dpkg --configure -a && sudo apt -f install`
6. `git clone git@github.com:dancingborg/ECU_CSG3303_BasicSR.git basicSR`

# Usage
1. Check `config.yml` for correctness of input directories and settings
    - Check `pretrain_model_G` for pretrained model location, typically
      `RRDB_PSNR.pth` or `RRDB_ESRGAN.pth`
    - Check `dataroot_GT` for directory of **G**round **T**ruth high resolution images
    - Check `dataroot_LQ` for directory of **L**ow **Q**uality downsampled images
    - Check `n_workers` and lower it if running out of memory
    - Check `batch_size` and lower it if running out of memory
    - Check `niter` for **n**umber of desired **iter**ations
2. Execute `run.sh` from the command line
3. When complete, check `experiments/TRAINED/models/` for models to import to ESRGAN


# Reference

    @InProceedings{wang2018esrgan,
        author = {Wang, Xintao and Yu, Ke and Wu, Shixiang and Gu, Jinjin and Liu, Yihao and Dong, Chao and Qiao, Yu and Loy, Chen Change},
        title = {ESRGAN: Enhanced super-resolution generative adversarial networks},
        booktitle = {The European Conference on Computer Vision Workshops (ECCVW)},
        month = {September},
        year = {2018}
    }
    @InProceedings{wang2018sftgan,
        author = {Wang, Xintao and Yu, Ke and Dong, Chao and Loy, Chen Change},
        title = {Recovering realistic texture in image super-resolution by deep spatial feature transform},
        booktitle = {The IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
        month = {June},
        year = {2018}
    }
