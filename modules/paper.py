


def video_id(dia):
    results = ""
    if dia == 'Alien':
        results = f'<iframe src="//player.bilibili.com/player.html?aid=782899585&bvid=BV1F24y1F7tG&cid=1110040687&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" height=600 width=800> </iframe>'
    elif dia == 'Amidar':
        results = f'<iframe src="//player.bilibili.com/player.html?aid=782899585&bvid=BV1F24y1F7tG&cid=1110041577&page=2" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" height=600 width=800> </iframe>'
    elif dia == 'Asterix':
        results = f'<iframe src="//player.bilibili.com/player.html?aid=782899585&bvid=BV1F24y1F7tG&cid=1110041921&page=3" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" height=600 width=800> </iframe>'
    elif dia == 'Boxing':
        results = f'<iframe src="//player.bilibili.com/player.html?aid=782899585&bvid=BV1F24y1F7tG&cid=1110042143&page=4" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" height=600 width=800> </iframe>'
    elif dia == 'Breakout':
        results = f'<iframe src="//player.bilibili.com/player.html?aid=782899585&bvid=BV1F24y1F7tG&cid=1110041998&page=5" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" height=600 width=800> </iframe>'
    elif dia == 'Crazyclimber':
        results = f'<iframe src="//player.bilibili.com/player.html?aid=782899585&bvid=BV1F24y1F7tG&cid=1110042418&page=6" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" height=600 width=800> </iframe>'
    elif dia == 'Pong':
        results = f'<iframe src="//player.bilibili.com/player.html?aid=782899585&bvid=BV1F24y1F7tG&cid=1110042436&page=7" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" height=600 width=800> </iframe>'
    elif dia == 'Assault':
        results = f'<iframe src="//player.bilibili.com/player.html?aid=782899585&bvid=BV1F24y1F7tG&cid=1111158210&page=8" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" height=600 width=800> </iframe>'
    elif dia == 'DemonAttack' or dia == 'Attack':
        results = f'<iframe src="//player.bilibili.com/player.html?aid=782899585&bvid=BV1F24y1F7tG&cid=1112123240&page=9" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" height=600 width=800> </iframe>'
    elif dia == 'Gopher':
        results = f'<iframe src="//player.bilibili.com/player.html?aid=782899585&bvid=BV1F24y1F7tG&cid=1113203119&page=10" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" height=600 width=800> </iframe>'
    elif dia == 'Hero':
        results = f'<iframe src="//player.bilibili.com/player.html?aid=782899585&bvid=BV1F24y1F7tG&cid=1116227957&page=11" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" height=600 width=800> </iframe>'
    elif dia == 'Jamesbond' or dia == 'Bond':
        results = f'<iframe src="//player.bilibili.com/player.html?aid=782899585&bvid=BV1F24y1F7tG&cid=1116227989&page=12" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" height=600 width=800> </iframe>'
    
    return results

def contx(dia):
    results = ""
    # print("dia:",dia)
    # Define results
    if dia == 'Paper':
        results = "本文是基于Efficientzero与Muzero改进的基于蒙特卡洛树的强化学习算法，研究意义可以归纳为以下几点：\n \
                1）将自监督方法用于强化学习AI训练，使用SimSiam作为自监督学习框架结合基于模型的强化学习，从而更好地利用模型环境；\n \
                2）雅达利游戏过程具有较大的分支因素，设计基于蒙特卡罗树搜索的强化学习算法，是在有限经验条件下设计游戏AI程序的一种很有前景的方法，能够从结果中学习并适应游戏环境的变化，为创造更有效且更吸引人的游戏AI提供了强大的方法指导；\n \
                3）通过设计有限的经验条件下的雅达利游戏AI程序，可以在提供优秀的游戏体验的同时降低游戏成本。此外，从这种方法中获得的见解可以应用于一般人工智能的构建，使其成为一个非常有价值的研究领域，值得进一步挖掘和研究。"
    
    elif dia == 'Simsiam':
        results = "SimSiam是一种经典的自监督学习框架，在这种方法中，模型可以学习对数据集进行预测，而无需人工标记注释。\n \
        SimSiam框架基于Siamese神经网络架构，该架构由两个具有相同权重的相同神经网络组成。其中一个网络，称为在线网络，用于对数据进行预测，而另一个网络，称为目标网络，用于为在线网络提供目标。\n \
        SimSiam主要思想是使用对比损失函数来鼓励在线网络学习对数据的各种转换不变的表示。\n \
        具体来说，在线网络被训练成在相同的输入上预测目标网络的输出，但应用了不同的增强。然后根据在线网络为每个增强输入产生的表示之间的余弦相似性计算对比损失。"
    elif dia == 'Muzero':
        results = "MuZero是Deepmind提出的一种强化学习算法，它结合了蒙特卡罗树搜索（MCTS）和深度神经网络的元素来学习和玩游戏。它是一种基于模型的强化学习算法，可以在没有任何先验知识或人类经验的情况下在复杂环境中学习和做出决策。 \n \
                    MuZero背后的关键思想是学习一个环境动力学模型，包括过渡动力学和奖励函数，然后使用这个模型来模拟和规划未来的轨迹。它结合使用价值网络、政策网络和动态网络来促进规划和决策过程。\n \
                    在训练过程中，MuZero使用MCTS通过迭代游戏、自我游戏和自我游戏来完善其模型和策略。它结合了树搜索和神经网络评估来探索和利用游戏树，选择导致最佳结果的行动。训练值网络来估计状态的值，训练策略网络来预测动作的概率分布，训练动态网络来预测给定当前状态和动作的下一个状态和奖励。\n \
                    MuZero值得注意的一个方面是，它是一种通用算法，可以应用于广泛的环境，而无需任何特定于领域的修改。它在各种领域取得了令人印象深刻的成果，包括桌面游戏、雅达利游戏，甚至是部分可观察性的游戏。"
    elif dia == 'MCTS':
        results = "MCTS代表蒙特卡罗树搜索。它是一种启发式搜索算法，用于决策和计划问题，特别是在游戏和其他具有复杂分支因素的领域。MCTS以其处理大型状态空间和基于有限信息做出明智决策的能力而闻名。 \n \
                    MCTS背后的核心思想是构建一个表示可能的操作序列及其结果的搜索树。它执行一系列模拟，称为蒙特卡罗rollouts，以估计给定状态下每个动作的值。该算法基于仿真结果动态扩展和探索搜索树。 \n \
                    MCTS主要包括四个关键步骤：选择、扩展、模拟（rollouts）、回溯（反向传播）。 \n \
                    通过迭代地重复这些步骤，MCTS逐步改进其对不同状态下每个动作值的估计，使其能够根据累积的统计数据做出明智的决策。MCTS执行的迭代或模拟越多，它在选择导致理想结果的操作方面就越好。\n \
                    MCTS已经成功地应用于各种领域，包括游戏(例如，AlphaGo, AlphaZero)，机器人，优化和规划问题。"
    
    elif dia == 'Efficentzero':
        results = "Efficientzero是在Deepmind的Muzero基础上修改的基于模型的强化学习算法，该方法一定程度上解决了强化学习在数据量有限的情况下的性能问题。 \n \
                    为了验证该算法的有效性，EfficientZero在强化学习算法通用测试基准Atari Game上取得了大幅度的提升。"
    elif dia == 'Alpacalora':
        results = "Alpaca-lora是本文Web可视化系统采用的大型语言模型，这是一结合LoRA微调技术的大型语言模型。 \n \
                    本文模型在冻结Alpaca参数的基础上，加入了LoRA网络结构，在微调参数下降的情况下，达到与Alpaca相似的性能。"

    elif dia == 'Pongfig':
        # results = f'<img src="https://raw.githubusercontent.com/FrankZxShen/Attention-Efficientzero-Alpaca-Lora-Webui/main/results/Alien.png" style="display: inline-block;">'
        results = f'![](https://raw.githubusercontent.com/FrankZxShen/Attention-Efficientzero-Alpaca-Lora-Webui/main/results_all/Pong.png)'
    elif dia == 'Alienfig':
        # results = f'<img src="https://raw.githubusercontent.com/FrankZxShen/Attention-Efficientzero-Alpaca-Lora-Webui/main/results/Alien.png" style="display: inline-block;">'
        results = f'![](https://raw.githubusercontent.com/FrankZxShen/Attention-Efficientzero-Alpaca-Lora-Webui/main/results_all/Alien.png)'
    elif dia == 'Amidarfig':
        # results = f'<img src="https://raw.githubusercontent.com/FrankZxShen/Attention-Efficientzero-Alpaca-Lora-Webui/main/results/Alien.png" style="display: inline-block;">'
        results = f'![](https://raw.githubusercontent.com/FrankZxShen/Attention-Efficientzero-Alpaca-Lora-Webui/main/results_all/Amidar.png)'
    elif dia == 'Boxingfig':
        # results = f'<img src="https://raw.githubusercontent.com/FrankZxShen/Attention-Efficientzero-Alpaca-Lora-Webui/main/results/Alien.png" style="display: inline-block;">'
        results = f'![](https://raw.githubusercontent.com/FrankZxShen/Attention-Efficientzero-Alpaca-Lora-Webui/main/results_all/Boxing.png)'
    elif dia == 'Crazyclimberfig':
        # results = f'<img src="https://raw.githubusercontent.com/FrankZxShen/Attention-Efficientzero-Alpaca-Lora-Webui/main/results/Alien.png" style="display: inline-block;">'
        results = f'![](https://raw.githubusercontent.com/FrankZxShen/Attention-Efficientzero-Alpaca-Lora-Webui/main/results_all/CrazyClimber.png)'
    elif dia == 'Assaultfig':
        # results = f'<img src="https://raw.githubusercontent.com/FrankZxShen/Attention-Efficientzero-Alpaca-Lora-Webui/main/results/Alien.png" style="display: inline-block;">'
        results = f'![](https://raw.githubusercontent.com/FrankZxShen/Attention-Efficientzero-Alpaca-Lora-Webui/main/results_all/Assault.png)'
    
    return results