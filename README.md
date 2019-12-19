# tuning_al_gui: Active Learning tuning for EUPanda

This repository contains the code behind the Active Learning tuning approach
presented in our soon-to-appear HRI'20 paper **"Interactive Tuning of Robot
Program Parameters via Expected Divergence Maximization", Mattia Racca,
Ville Kyrki, and Maya Cakmak"**.

While the AL approach is standalone (contained in `src/range_al`), its
implementation for the Franka Panda robot and related AL tuning GUI depends on
[EUPanda], my ROS-based end-user programming framework.

#### TODO:
- [ ] document intregration with [EUPanda] (how to build the catkin workspace)
- [ ] document main .launch files
- [ ] add screenshot of the AL tuning GUI
- [ ] add reference/link to paper

[EUPanda]: https://github.com/MattiaRacca/eupanda


#### License
Everything authored by me is released under the GNU GPL 3.0 license. Some files are authored by others, and are included as part of my own setup; they still belong to the original authors.
