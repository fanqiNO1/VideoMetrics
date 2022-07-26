function puMetrics = main(task, test, reference)
    test_img = hdrread(test);
    reference_img = hdrread(reference);
    switch task
    case 'puMSSSIM'
        puMetrics = puMSSSIM(test_img, reference_img);
    case 'puPSNR'
        puMetrics = qm_pu2_psnr(test_img, reference_img);
    case 'puSSIM'
        puMetrics = qm_pu2_ssim(test_img, reference_img);
    end
end