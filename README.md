# VideoMetrics

Some metrics for video compression, including BPP, PSNR, and SSIM etc.

Work on Ubuntu 20.04. Other versions or other OSes are not tested.

## For SDR (Standard Dynamic Range)

The metrics for SDR video are BPP, PSNR and SSIM.

The corresponding scripts mainly based on the FFMPEG.

## For HDR (High Dynamic Range)

The metrics for HDR video are BPP, puPSNR, puSSIM, and hDR-VDP.

Because the original metrics are based on matlab, it is compiled to binary files.

Besides, because the original metrics are mainly designed for image, the scripts apply the metrics into video by recursively call.

## Requirements

Opencv

MATLAB_Runtime_R2022a_Update_3_glnxa64

## Warning

Because the HDR part is mainly based on matlab, it has a very very low speed!