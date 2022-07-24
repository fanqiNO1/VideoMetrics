# Calculate the Bit Per Pixel (BPP) of the video.
import argparse
import os
import platform


def cal_BPP(args):
    file_size = os.stat(args.video).st_size
    bpp = file_size * 8 / args.frames / args.width / args.height
    return bpp


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--video', type=str, default='',
                        help='The input video path.')
    parser.add_argument('--width', type=int, default=0,
                        help='The width of the video.')
    parser.add_argument('--height', type=int, default=0,
                        help='The height of the video.')
    parser.add_argument('--frames', type=int, default=0,
                        help='The number of frames of the video.')
    args = parser.parse_args()
    bpp = cal_BPP(args)
    video_name = args.video.split(
        '/')[-1] if platform.system() == 'Linux' else args.video.split('\\')[-1]
    print(f"The BPP of the video {video_name} is {bpp:.6f}.")
