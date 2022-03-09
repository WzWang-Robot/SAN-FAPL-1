# SAN-FAPL
This repository contains source codes for our paper: "Feedback-efficient Active Preference Learning for Socially Aware Robot Navigation". 
For more details, please refer to [our website](https://sites.google.com/view/san-fapl).
## Abstract
Socially aware robot navigation, where a robot is required to optimize its trajectory to maintain comfortable and compliant spatial interactions with humans in addition to reaching its goal without collisions, is a fundamental yet challenging task in the context of human-robot interaction. While existing learning-based methods have achieved better performance than the preceding model-based ones, they still have drawbacks: reinforcement learning depends on the handcrafted reward that is unlikely to effectively quantify broad social compliance, and can lead to reward exploitation problems; meanwhile, inverse reinforcement learning suffers from the need for expensive human demonstrations. In this paper, we propose a feedback-efficient active preference learning approach, FAPL, that distills human comfort and expectation into a reward model to guide the robot agent to explore latent aspects of social compliance. We further introduce hybrid experience learning to improve the efficiency of human feedback and samples, and evaluate benefits of robot behaviors learned from FAPL through extensive simulation experiments and a user study (N=10) employing a physical robot to navigate with human subjects in real-world scenarios.
## Overview Architecture for FAPL
这里插入论文的fig2
## Usage

### Set Up
配置环境
### Run the code
运行代码

## Acknowledgement

Some portion of the code were adapted from the [CrowdNav repo](https://github.com/vita-epfl/CrowdNav).





