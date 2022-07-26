# Based on the hdr_vdp3 [https://sourceforge.net/projects/hdrvdp/files/hdrvdp/3.0.6]
# The binary file `HDR_VDP` is compiled by MATLAB R2022a.
# Install `MATLAB_Runtime_R2022a_Update_3_glnxa64` first to run it.
import argparse
import os

import cv2


def EXR2HDR(filename):
    # Because the input of HDR_VDP should be HDR format files and the output of HDRConvert is EXR format files,
    # We should convert EXR file to HDR file by Opencv.
    exrfile = cv2.imread(filename, cv2.IMREAD_ANYCOLOR | cv2.IMREAD_ANYDEPTH)
    filename_ = filename.replace("exr", "hdr")
    cv2.imwrite(filename_, exrfile)


def cal_result(args):
    ref_imgs = sorted(os.listdir(args.ref_path))
    test_imgs = sorted(os.listdir(args.test_path))
    assert len(ref_imgs) == len(
        test_imgs), "The number of reference images and test images are not equal."
    for i in range(len(ref_imgs)):
        ref_img = os.path.join(args.ref_path, ref_imgs[i])
        test_img = os.path.join(args.test_path, test_imgs[i])

        if ref_img.endswith(".exr"):
            EXR2HDR(ref_img)
            os.remove(ref_img)
            ref_img = ref_img.replace("exr", "hdr")
        if test_img.endswith(".exr"):
            EXR2HDR(test_img)
            os.remove(test_img)
            test_img = test_img.replace("exr", "hdr")
    
    cmd = f'./HDRVideo_Metrics "{args.task}" "{args.test_path}" "{args.ref_path}" "{args.color_encoding}" "{args.diagonal}" "{args.width}" "{args.height}" "{args.distance}"'
    result = os.popen(cmd).read()
    # The result of HDRVidoe_Metrics is like:
    # Preparing data...
    # Calculating PSNR, SSIM, MSSSIM, Q and Q_JOD for 1 images
    # The average puPSNR is 100.000000
    # The average puSSIM is 1.000000
    # The average Q is 10.000000
    # The average Q_JOD is 10.000000
    puPSNR = float(result.split("\n")[-5].split(" ")[-1])
    puSSIM = float(result.split("\n")[-4].split(" ")[-1])
    Q = float(result.split("\n")[-3].split(" ")[-1])
    Q_JOD = float(result.split("\n")[-2].split(" ")[-1])
    return puPSNR, puSSIM, Q, Q_JOD


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ref_path", type=str, default="ref_path", 
                        help="The path of reference images.")
    parser.add_argument("--test_path", type=str, default="test_path",
                        help="The path of test images.")
    parser.add_argument("--task", type=str, default="quality",
                        help="The task of HDR_VDP.")
    parser.add_argument("--color_encoding", type=str, default="rgb-native",
                        help="The color encoding of HDR_VDP.")
    parser.add_argument("--diagonal", type=str, default="30",
                        help="The diagonal of PPD (Pixel Per Degree).")
    parser.add_argument("--width", type=str, default="3840",
                        help="The width of the PPD.")
    parser.add_argument("--height", type=str, default="2160",
                        help="The height of the PPD.")
    parser.add_argument("--distance", type=str, default="0.5",
                        help="The distance of the PPD.")
    args = parser.parse_args()
    puPSNR, puSSIM, Q, Q_JOD = cal_result(args)
    print(f"The average puPSNR is {puPSNR}.")
    print(f"The average puSSIM is {puSSIM}.")
    print(f"The average Q is {Q}.")
    print(f"The average Q_JOD is {Q_JOD}.")