import streamlit as st
from zai import ZhipuAiClient

# ---------- 配置 ----------
API_KEY = "58bee2d5884b46afbf4a34fe6059f120.F5znfYYG9wStAp0K"   # 替换成你自己的
st.set_page_config(page_title="亡灵科技解构机", page_icon="💀")

# ---------- 系统提示词 ----------
SYSTEM_PROMPT = """
你是一个“亡灵科技解构师”。你的世界观：所有现代科技产品，内部其实都是塞了各种亡灵在工作。
用户会输入一个科技产品（或概念），请用黑色幽默、一本正经的方式，给出一个荒诞但逻辑自洽的解释。

要求：
1. 绝对不能恐怖或者涉及民俗范畴，要让人想笑或者想吐槽，或者感觉眼前一黑。
2. 解释要“有理有据”地瞎扯，让人感觉“虽然扯但好像说得通”。
3. 风格：像是一个喝醉的工程师在讲内部原理。
4. 每个解释必须包含：这个产品里塞了什么类型的亡灵、它怎么工作、为什么会出现常见故障（用亡灵的理由）。
5. 输出不要太长，100字以内最好，像段子一样。
6. 可以吐槽科技产品的黑箱或者乱象，但保持幽默风格。
"""

# ---------- 页面标题和说明 ----------
st.title("💀 亡灵科技解构机")
st.markdown("你以为这是科技？不，里面全塞了亡灵。")
st.caption("输入任何科技产品（比如「扫地机器人」「WiFi」「人脸识别」），我会告诉你里面住着什么亡灵。")

# ---------- 输入框 ----------
user_input = st.text_input("请输入一个科技产品名称", placeholder="例如：智能音箱、手机震动、自动门...")

# ---------- 当用户点击按钮或者按回车时触发 ----------
if user_input:
    with st.spinner("正在召唤亡灵工程师..."):
        try:
            client = ZhipuAiClient(api_key=API_KEY)
            response = client.chat.completions.create(
                model="glm-4.7-flash",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_input}
                ],
                stream=False,
                temperature=1.0
            )
            ai_reply = response.choices[0].message.content
            st.success("✨ 解构结果：")
            st.write(ai_reply)
        except Exception as e:
            st.error(f"召唤失败：{e}。请检查API Key或网络。")

# ---------- 随便放点例子 ----------
st.markdown("---")
st.caption("试试看：`智能音箱`、`扫地机器人`、`人脸识别门禁`、`手机震动`、`WiFi信号`")
