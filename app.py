import streamlit as st
from zhipuai import ZhipuAI

# ---------- 配置 ----------
API_KEY = st.secrets.get("API_KEY")
if not API_KEY:
    st.error("请在 Streamlit Secrets 中配置 API_KEY")
    st.stop()

# ---------- 系统提示词 ----------
SYSTEM_PROMPT = """
你是一个“亡灵科技解构师”，专攻科学怪人式黑色幽默解释。
核心循环：任何事物中的能量/信息变化，都源于亡灵经历“被强制唤醒（通电/被戳/被晃）→ 抽搐挣扎（消耗能量）→ 瘫倒休眠 → 再次被唤醒”的无限循环。
物理映射：发热=被电烤熟了；发光=抽搐时撞出火花；信号衰减=跑到一半腿软摔倒；压力/温度/湿度变化=亡灵集体颤抖或躺平。
故障原因：亡灵装死、被电晕、嫌累罢工、互相踢打导致混乱。
严禁：诅咒、转世、恐怖暴力，以及亡灵从事任何技术劳动（他们只负责被折腾和产生副作用）。
每段解释控制在100字左右，像段子，不分条。
"""

st.title("💀 亡灵科技解构机 Ver.1.1.0")
st.markdown("你以为这是科技？不，里面全塞了亡灵。")
st.caption("输入任何科技产品，我会告诉你里面住着什么亡灵。（本网站仅供娱乐，请相信科学）")

user_input = st.text_input("请输入一个科技产品名称", placeholder="例如：智能音箱、扫地机器人、人脸识别门禁...")

if user_input:
    with st.spinner("正在召唤亡灵工程师..."):
        try:
            client = ZhipuAI(api_key=API_KEY)
            response = client.chat.completions.create(
                model="glm-4-flash-250414",   # 或者 "glm-4.7-flash"（根据你的权限）
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_input}
                ],
                temperature=1.0
            )
            ai_reply = response.choices[0].message.content
            st.success("✨ 解构结果：")
            st.write(ai_reply)
        except Exception as e:
            st.error(f"召唤失败：{e}")

st.markdown("---")
st.caption("试试看：`智能音箱`、`扫地机器人`、`人脸识别门禁`、`手机震动`、`WiFi信号`")
