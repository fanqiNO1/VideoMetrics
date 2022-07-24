# Calculate the average SSIM based on the SSIm log from ffmpeg.
# A line in the log looks like this:
# n:514 Y:0.907333 U:0.895552 V:0.935018 All:0.909984 (10.456785)
import argparse


def cal_avg_SSIM(args):
    ssim_all = []
    ssim = []
    with open(args.log, "r") as f:
        lines = f.readlines()
        for line in lines:
            if "All" in line:
                line_split = line.split(" ")

                ssim_all_avg = line_split[4]
                ssim_avg = line_split[5]

                ssim_all_avg_item = ssim_all_avg.split(":")[1]
                ssim_avg_item = ssim_avg.replace("(", "").replace(")", "")

                ssim_all.append(float(ssim_all_avg_item))
                ssim.append(float(ssim_avg_item))

    return sum(ssim_all) / len(ssim_all), sum(ssim) / len(ssim)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--log', type=str, default='',
                        help='The log file path.')
    args = parser.parse_args()
    ssim_all, ssim = cal_avg_SSIM(args)
    print(f"The average SSIM is {ssim_all:.6f} ({ssim:.6f})")
