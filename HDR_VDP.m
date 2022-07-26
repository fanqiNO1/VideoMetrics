function ret = main(task, test, reference, color_encoding, display_diagonal_in, resolutionW, resolutionH, viewing_distance)
    fprintf("Loading images...\n");
    test_img = hdrread(test);
    ref_img = hdrread(reference);
    fprintf("Preparing...\n");
    display_diagonal_in = str2double(display_diagonal_in);
    resolutionW = str2double(resolutionW);
    resolutionH = str2double(resolutionH);
    viewing_distance = str2double(viewing_distance);
    resolution = [resolutionW resolutionH];
    fprintf("Calculating...\n");
    ppd = hdrvdp_pix_per_deg(display_diagonal_in, resolution, viewing_distance);
    ret = hdrvdp3(task, test_img, ref_img, color_encoding, ppd, {});
    fprintf("The Q is %.6f, the Q_JOD is %.6f\n", ret.Q, ret.Q_JOD);
end
