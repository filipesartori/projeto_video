from tiktok import uploadVideo

session_id = "64ab5fd76ac874ad9acb990ed815da04"
file = "./output.mp4"
title = "MY SUPER TITLE"
tags = ["Viral", "Trend"]

uploadVideo(session_id, file, title, tags, verbose=True)