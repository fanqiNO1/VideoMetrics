function ret = main(vdp_task, test_path, ref_path, color_encoding, display_diagonal_in, resolutionW, resolutionH, viewing_distance)
    fprintf("Preparing data...\n");
    test_imgs = dir(fullfile(test_path, '*.hdr'));
    ref_imgs = dir(fullfile(ref_path, '*.hdr'));
    if length(test_imgs) ~= length(ref_imgs)
        error('Number of test images and reference images do not match');
    end

    display_diagonal_in = str2double(display_diagonal_in);
    resolutionW = str2double(resolutionW);
    resolutionH = str2double(resolutionH);
    viewing_distance = str2double(viewing_distance);
    resolution = [resolutionW resolutionH];
    ppd = hdrvdp_pix_per_deg(display_diagonal_in, resolution, viewing_distance);

    puPSNR = [];
    puSSIM = [];
    Q = [];
    Q_JOD = [];
    fprintf("Calculating PSNR, SSIM, MSSSIM, Q and Q_JOD for %d images\n", length(test_imgs));
    for i = 1:length(test_imgs)
        test_img = hdrread(fullfile(test_path, test_imgs(i).name));
        ref_img = hdrread(fullfile(ref_path, ref_imgs(i).name));
        puPSNR_i = qm_pu2_psnr(test_img, ref_img);
        if isinf(puPSNR_i)
            puPSNR_i = 100;
        end
        puSSIM_i = qm_pu2_ssim(test_img, ref_img);
        ret_i = hdrvdp3(vdp_task, test_img, ref_img, color_encoding, ppd, {});
        Q_i = ret_i.Q;
        Q_JOD_i = ret_i.Q_JOD;

        puPSNR = [puPSNR puPSNR_i];
        puSSIM = [puSSIM puSSIM_i];
        Q = [Q Q_i];
        Q_JOD = [Q_JOD Q_JOD_i];
    end

    puPSNR_avg = mean(puPSNR);
    puSSIM_avg = mean(puSSIM);
    Q_avg = mean(Q);
    Q_JOD_avg = mean(Q_JOD);
    fprintf("The average puPSNR is %.6f\n", puPSNR_avg);
    fprintf("The average puSSIM is %.6f\n", puSSIM_avg);
    fprintf("The average Q is %.6f\n", Q_avg);
    fprintf("The average Q_JOD is %.6f\n", Q_JOD_avg);
    ret = 0;
end
