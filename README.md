# tuning_al_gui: Active Learning tuning for EUPanda

This repository contains the code behind the Active Learning tuning approach
presented in \[[1]\].

While the Active Learning approach is standalone (contained in `src/range_al`), its
implementation for the Franka Panda robot and related tuning GUI depends on
[EUPanda], my ROS-based end-user programming framework.
**Watch the robot in action [here]!**


\[[1]\] Mattia Racca, Ville Kyrki, and Maya Cakmak, **"Interactive Tuning of Robot Program Parameters via Expected Divergence Maximization"**, HRI'20
```bibtex
@inproceedings{racca20,
author = {Racca, Mattia and Kyrki, Ville and Cakmak, Maya},
title = {Interactive Tuning of Robot Program Parameters via Expected Divergence Maximization},
year = {2020},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
booktitle = {Proceedings of the 2020 ACM/IEEE International Conference on Human-Robot Interaction},
pages = {629–638},
keywords = {human-robot interaction, end-user programming, active learning},
series = {HRI '20}
}
```

[EUPanda]: https://github.com/MattiaRacca/eupanda
[1]: https://dl.acm.org/doi/abs/10.1145/3319502.3374784
[here]: https://vimeo.com/mattiaracca/hri20


#### License
Everything authored by me is released under the GNU GPL 3.0 license. Some files are authored by others, and are included as part of my own setup; they still belong to the original authors.
