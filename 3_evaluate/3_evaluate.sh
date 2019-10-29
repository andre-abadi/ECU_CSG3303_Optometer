#!/bin/bash
echo
echo 'Clearing local input/ and output/ directories.'
echo
rm -rv input/*
rm -rv output/*
echo
echo 'Copying model trained with basicSR if present'
echo
cp -v ../basicSR/experiments/TRAINED/models/latest_G.pth ./models/
echo
echo 'Copying files to local input directory'
echo
rsync -zvah --no-p --no-g /volume1/transfer/Optometer/ESRGAN-Input/ ./input
echo
echo 'Executing ESRGAN'
echo
python3 test.py
echo
echo 'Copying output files back out from local directory'
echo
rsync -zvah --no-p --no-g ./output/ /volume1/transfer/Optometer/ESRGAN-Output/
echo
echo 'Evaluating output files for mean PSNR and SSIM'
echo
python3 calculate.py
echo
echo 'Copying model to Model library'
cp -v models/latest_G.pth /volume1/transfer/Optometer/Models/latest_G_$(date -d "today" +"%Y-%m-%d-%H-%M-%S").pth
