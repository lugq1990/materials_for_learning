## activation



### GLU（Gated Linear Unit）线性门控单元的FFN（Feed-Forward Network）

[explain for the activation function with GLU, gated linear unit](https://github.com/wdndev/llm_interview_note/blob/main/02.%E5%A4%A7%E8%AF%AD%E8%A8%80%E6%A8%A1%E5%9E%8B%E6%9E%B6%E6%9E%84/6.%E6%BF%80%E6%B4%BB%E5%87%BD%E6%95%B0/6.%E6%BF%80%E6%B4%BB%E5%87%BD%E6%95%B0.md)

Gated Linear Unit (GLU) 是一种改进的激活函数形式，广泛用于神经网络中的前馈网络（Feed-Forward Network，FFN）。GLU 的设计灵感来自于门控机制，这种机制常见于循环神经网络（RNN）和 Transformer 等架构中。GLU 在 FFN 中的应用主要是为了增加网络的非线性表达能力，同时引入更强的选择性机制。

### GLU 的基本公式

GLU 可以用以下公式表示：

\[ \text{GLU}(X) = (X W_1 + b_1) \otimes \sigma(X W_2 + b_2) \]

其中：
- \(X\) 是输入向量。
- \(W_1\) 和 \(W_2\) 是权重矩阵。
- \(b_1\) 和 \(b_2\) 是偏置项。
- \(\sigma\) 是 sigmoid 函数，用于门控机制。
- \(\otimes\) 表示按元素乘法（Hadamard 乘积）。

### FFN 中的 GLU

在 FFN 中使用 GLU 时，通常会有两层线性变换，每一层都应用 GLU 激活函数。FFN 的结构通常如下：

1. **线性变换 + 激活函数（如 ReLU）**：
\[ H = \text{ReLU}(XW_1 + b_1) \]

2. **线性变换**：
\[ Y = HW_2 + b_2 \]

引入 GLU 后，FFN 的结构变为：

1. **线性变换 + GLU**：
\[ H = \text{GLU}(X) = (X W_1 + b_1) \otimes \sigma(X W_2 + b_2) \]

2. **线性变换**：
\[ Y = HW_3 + b_3 \]

其中，\(W_1\)、\(W_2\)、\(b_1\) 和 \(b_2\) 是第一层线性变换和 GLU 的参数，\(W_3\) 和 \(b_3\) 是第二层线性变换的参数。

### GLU 的优势

1. **增强的非线性能力**：GLU 将输入划分为两部分，一部分用于线性变换，另一部分通过 sigmoid 函数进行门控，使得输出具有更强的非线性能力。

2. **选择性**：通过 sigmoid 函数引入的门控机制，可以控制信息的流动，选择性地通过有用的信息，同时抑制不相关或不重要的信息。

3. **更稳定的梯度**：GLU 通过门控机制，可以缓解梯度消失或梯度爆炸的问题，使得训练过程更加稳定。

### 应用场景

GLU 在许多神经网络架构中都得到了应用，尤其是在需要处理长序列或复杂依赖关系的任务中，如语言模型、机器翻译和自然语言处理任务中。通过引入 GLU，可以有效地增强模型的表现能力，提高任务的准确性和鲁棒性。

### 总结

Gated Linear Unit (GLU) 是一种结合了线性变换和门控机制的激活函数，通过在 FFN 中引入 GLU，可以增强模型的非线性表达能力和选择性，提升模型的性能和训练稳定性。在实际应用中，GLU 通过对输入信息的选择性控制，实现了更优的特征提取和表示能力。