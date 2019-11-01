# Introduction
- This repository is an open source representation of the author's **CSG3303 Applied IT Project** at Edith Cowan University in Semester 2 of 2019
- This repository contains the code and templates needed to:
  1. Generate random valid registration plate character sets
  2. Render synthetic Western Australian vehicle registration plates using the randomly generated character sets
  3. Conduct further training of a pre-trained SRGAN model using the synthetic registration plates
  4. Use the further trained model to upscale images and evaluate effectiveness by comparing PSNR and SSIM against ground truth originals
- This repository accompanies the primary deliverable for the project, an analytical report
- A redacted copy of the analytical report can be found in the **5_report** folder of this repository

# Pre-Requisities
- This repository requires the following environment to operate correctly

  | Type             | State                   |
  | ---              | ---                     |
  | Operating System | Linux (Ubuntu)          |
  | Hardware         | NVIDIA CUDA-enabled GPU |
  | Software         | Linux Nvidia Drivers    |

# Installation
- The author took the following steps to provision the working environment so that this repository

  | Software  | Installation Command                                                         |
  | ---       | ---                                                                          |
  | Python 3  | `sudo apt install python3 python3-pip`                                       |
  | Git       | `sudo apt install git`                                                       |
  | CUDA      | `sudo apt install cuda nvidia-cuda-toolkit`                                  |
  | Python ML | `pip3 install numpy opencv-python lmdb pyyaml tb-nightly future torchvision` |
  | Auto Fix  | `sudo dpkg --configure -a && sudo apt -f install`                            |


# Usage
- Each numbered folder has its own README.md file with instructions on how to use that particlar tool, but a brief overview is provided here
- **1_generator** is a Python 3 program that generates random registration plate character sets
  1. Execute `1_generate.sh`
  2. Enter the number of plates to be generated. `How many plates? Default is 5:`
  3. Enter the desired file to be written by the program. Which file to write to? `Default is output.txt:`
  4. Enter the plate type to be generated. `Plate type to generate? Default is 1:`
  5. See `1_generate/README.md` for generation options
- **2_render** is a folder of image files that you can load in Photoshop
  1. Install the font at `2_render/Fonts/`
  2. Use the generated character sets as variables to substitute the static strings in the files
  3. Export each variable as a file
  4. Use another image manipulation program (like Irfan View) to make folders of downsampled training and test images while keeping the ground truth values for reference
- **3_train** is an adapted version of [BasicSR](https://github.com/xinntao/BasicSR) for this project
  1. Check `config.yml` for correctness of input directories and settings
  
      | Setting            | Effect                                                                                        |
      | ---                |  ---                                                                                          |
      | `pretrain_model_G` | Path to pretrained model with `pth` extension, typically `RRDB_PSNR.pth` or `RRDB_ESRGAN.pth` |     
      | `dataroot_GT`      | Directory of **G**round **T**ruth high resolution images                                      |
      | `dataroot_LQ`      | Directory of **L**ow **Q**uality downsampled images                                           |
      | `n_workers`        | Number of worker threads. Lower it if running out of memory                                   |
      | `batch_size`       | Lower it if running out of memory                                                             |
      | `niter`            | **n**umber of **iter**ations                                                                  |
  2. Execute `3_train.sh` from the command line
  3. When complete, check `experiments/TRAINED/models/` for models to import to ESRGAN
- **4_evaluate** is an adapted version of [ESRGAN](https://github.com/xinntao/ESRGAN) for this project
  1. Check `4_evaluate.sh`
  
      | Setting            | Effect                                                |
      | ---                | ---                                                   |
      | Line 10            | Where to source latest model from BasicSR             |
      | Line 14            | Input folder                                          |
      | Line 22            | Output folder                                         |
      | Line 29            | Where to archive the model used with a time reference |
  2. Run `4_evaluate.sh`
  3. Check output folder

# Attribution
- This repository combines several previous repositories of the author's forks and some original work
- The main repositories used as a source for this repository were as follows, and they contain all the commits showing progress and modifications to any original works:
  1. [dancingborg/ECU_CSG3303_RegistrationPlateGenerator](https://github.com/dancingborg/ECU_CSG3303_RegistrationPlateGenerator), the author's own work
  2. [dancingborg/ECU_CSG3303_BasicSR](https://github.com/dancingborg/ECU_CSG3303_BasicSR), a fork of [xinntao/BasicSR](https://github.com/xinntao/BasicSR)
  3. [dancingborg/ECU_CSG3303_ESRGAN](https://github.com/dancingborg/ECU_CSG3303_ESRGAN), a fork of [xinntao/ESRGAN](https://github.com/xinntao/ESRGAN)
- This repository contains code to train and executed [ESRGAN](https://github.com/xinntao/ESRGAN), which is an original work by [xinntao](https://github.com/xinntao)
  - The [BasicSR](https://github.com/xinntao/BasicSR) and [ESRGAN](https://github.com/xinntao/ESRGAN) components of this repository are predominantly not the original work of the author, but adapted (forked) as permitted by the licenses of the original works
- The following reference gives attribution to the author of the original [BasicSR](https://github.com/xinntao/BasicSR) code used in this repository:

  ```
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
  ```

- The following reference gives attribution to the oauthor of the original [ESRGAN](https://github.com/xinntao/ESRGAN) code used in this repository:

  ```
  @article{wang2018esrgan,
      author={Wang, Xintao and Yu, Ke and Wu, Shixiang and Gu, Jinjin and Liu, Yihao and Dong, Chao and Loy, Chen Change and Qiao, Yu and Tang, Xiaoou},
      title={ESRGAN: Enhanced super-resolution generative adversarial networks},
      journal={arXiv preprint arXiv:1809.00219},
      year={2018}
  }   
  @InProceedings{wang2018esrgan,
      author = {Wang, Xintao and Yu, Ke and Wu, Shixiang and Gu, Jinjin and Liu, Yihao and Dong, Chao and Qiao, Yu and Loy, Chen Change},
      title = {ESRGAN: Enhanced super-resolution generative adversarial networks},
      booktitle = {The European Conference on Computer Vision Workshops (ECCVW)},
      month = {September},
      year = {2018}
  }
  ```
