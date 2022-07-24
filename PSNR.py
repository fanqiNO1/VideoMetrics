# Calculate the average PSNR based on the PSNR log from ffmpeg.
# A line in the log looks like this:
# n:114 mse_avg:6.90 mse_y:7.44 mse_u:7.26 mse_v:4.39 psnr_avg:39.74 psnr_y:39.41 psnr_u:39.52 psnr_v:41.71
import argparse


def cal_avg_PSNR(args):
    psnr = []
    with open(args.log, "r") as f:
        lines = f.readlines()
        for line in lines:
            if "psnr_avg" in line:
                psnr_avg = line.split(" ")[5]
                psnr_avg_item = psnr_avg.split(":")[1]
                psnr.append(float(psnr_avg_item))
    return sum(psnr) / len(psnr)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--log', type=str, default='',
                        help='The log file path.')
    args = parser.parse_args()
    average_PSNR = cal_avg_PSNR(args)
    print(f"The average PSNR is {average_PSNR:.6f}.")
