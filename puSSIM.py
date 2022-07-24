# Based on the hdr_metrics from https://sourceforge.net/projects/hdrvdp/files/simple_metrics.
# The binary file `HDR_Metrics` is compiled by MATLAB R2022a.
# Install `MATLAB_Runtime_R2022a_Update_3_glnxa64` first to run it.
import argparse
import os

import cv2


def EXR2HDR(filename):
    # Because the input of puSSIM should be HDR format files and the output of HDRConvert is EXR format files,
    # We should convert EXR file to HDR file by Opencv.
    exrfile = cv2.imread(filename, cv2.IMREAD_ANYCOLOR | cv2.IMREAD_ANYDEPTH)
    filename_ = filename.replace("exr", "hdr")
    cv2.imwrite(filename_, exrfile)


def cal_puSSIM(args):
    puSSIM = []
    ref_imgs = sorted(os.listdir(args.ref_path))
    test_imgs = sorted(os.listdir(args.test_path))
    assert len(ref_imgs) == len(test_imgs), "The number of reference images and test images are not equal."
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

        cmd = f'./HDR_Metrics "puSSIM" "{ref_img}" "{test_img}"'
        result = os.popen(cmd).read()
        # The result of HDR_Metrics is like:
        # Loading images...
        # Calculating...
        # The puSSIM is 1.000000
        puSSIM_avg = result.split("\n")[-2].split(" ")[-1]
        puSSIM.append(float(puSSIM_avg))
    return sum(puSSIM) / len(puSSIM)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--ref_path', type=str, default=None, 
                        help='The path of reference images.')
    parser.add_argument('--test_path', type=str, default=None,
                        help='The path of test images.')
    args = parser.parse_args()
    puSSIM = cal_puSSIM(args)
    print(f"The average puSSIM is {puSSIM:.6f}")
