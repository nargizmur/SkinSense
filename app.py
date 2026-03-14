import gradio as gr
import tensorflow as tf
import numpy as np
 
model = tf.keras.models.load_model('melanoma_best.h5')
 
def predict_skin(image):
    if image is None:
        return None
    img = tf.image.resize(image, [224, 224])
    img = np.expand_dims(np.array(img) / 255.0, axis=0)
    pred = float(model.predict(img)[0][0])
    return {" Меланома": round(pred, 3), " Не меланома": round(1-pred, 3)}
 
css = """
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800;900&display=swap');
 
* { font-family: 'Outfit', sans-serif; box-sizing: border-box; margin: 0; padding: 0; }
 
body, .gradio-container {
    background: linear-gradient(160deg, #060d1a 0%, #0a1628 40%, #0d2444 100%) !important;
    min-height: 100vh;
}
 
.gradio-container {
    max-width: 600px !important;
    margin: 0 auto !important;
    padding: 16px !important;
}
 
.hero {
    text-align: center;
    padding: 28px 0 20px;
}
.hero-title {
    font-size: clamp(2.2em, 8vw, 3.5em);
    font-weight: 900;
    color: white;
    letter-spacing: -2px;
    line-height: 1;
    margin-bottom: 6px;
}
.hero-title span { color: #5dd4f0; }
.hero-sub {
    color: rgba(93,212,240,0.7);
    font-size: clamp(0.7em, 3vw, 0.85em);
    letter-spacing: 4px;
    text-transform: uppercase;
    font-weight: 600;
    margin-bottom: 24px;
}
 
.card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(93,212,240,0.15);
    border-radius: 18px;
    padding: 20px;
    margin-bottom: 14px;
    backdrop-filter: blur(10px);
}
.card-title {
    color: #5dd4f0;
    font-size: 0.72em;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 14px;
}
 
.steps-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 10px;
}
@media (min-width: 480px) {
    .steps-grid { grid-template-columns: 1fr 1fr; }
}
 
.step-item {
    display: flex;
    align-items: center;
    gap: 10px;
    color: rgba(255,255,255,0.8);
    font-size: clamp(0.82em, 3.5vw, 0.9em);
    line-height: 1.4;
}
.step-num {
    background: linear-gradient(135deg, #5dd4f0, #3ab8d8);
    color: #060d1a;
    border-radius: 50%;
    width: 26px; height: 26px;
    min-width: 26px;
    display: flex; align-items: center; justify-content: center;
    font-weight: 800; font-size: 0.78em;
}
 
.warning {
    background: rgba(255,200,0,0.06);
    border: 1px solid rgba(255,200,0,0.2);
    border-radius: 12px;
    padding: 12px 16px;
    color: rgba(255,215,80,0.85);
    font-size: clamp(0.75em, 3vw, 0.82em);
    line-height: 1.7;
    text-align: center;
    margin-top: 14px;
}
 
.awareness-title {
    color: white;
    font-size: clamp(1em, 4vw, 1.3em);
    font-weight: 800;
    margin-bottom: 14px;
    letter-spacing: -0.5px;
}
.awareness-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 10px;
    margin-bottom: 14px;
}
@media (min-width: 480px) {
    .awareness-grid { grid-template-columns: 1fr 1fr; }
}
 
.awareness-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(93,212,240,0.1);
    border-radius: 14px;
    padding: 16px;
}
.awareness-card-title {
    color: #5dd4f0;
    font-size: 0.75em;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 5px;
}
.awareness-card-text {
    color: rgba(255,255,255,0.65);
    font-size: clamp(0.78em, 3vw, 0.85em);
    line-height: 1.6;
}
.awareness-card-text b { color: rgba(255,255,255,0.9); }
 
.abcde-box {
    background: rgba(93,212,240,0.05);
    border: 1px solid rgba(93,212,240,0.2);
    border-radius: 14px;
    padding: 18px;
    margin-bottom: 12px;
}
.abcde-title {
    color: white;
    font-weight: 700;
    font-size: clamp(0.8em, 3.5vw, 0.9em);
    margin-bottom: 12px;
}
.abcde-grid {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 6px;
}
.abcde-item {
    text-align: center;
    background: rgba(255,255,255,0.04);
    border-radius: 10px;
    padding: 10px 4px;
}
.abcde-letter {
    font-size: clamp(1.2em, 4vw, 1.6em);
    font-weight: 900;
    color: #5dd4f0;
    line-height: 1;
}
.abcde-word {
    color: rgba(255,255,255,0.5);
    font-size: clamp(0.5em, 2vw, 0.65em);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin: 3px 0;
}
.abcde-desc {
    color: rgba(255,255,255,0.75);
    font-size: clamp(0.6em, 2.2vw, 0.72em);
    line-height: 1.4;
}
 
.footer-text {
    text-align: center;
    color: rgba(255,255,255,0.2);
    font-size: 0.72em;
    padding: 16px 0 8px;
    letter-spacing: 1px;
}
 
label span { color: white !important; font-weight: 600 !important; }
.svelte-1gfkn6j, [data-testid="image"] {
    background: rgba(255,255,255,0.04) !important;
    border: 2px dashed rgba(93,212,240,0.3) !important;
    border-radius: 16px !important;
}
button.primary {
    background: linear-gradient(135deg, #5dd4f0, #3ab8d8) !important;
    color: #060d1a !important;
    font-weight: 800 !important;
    border-radius: 12px !important;
    font-size: clamp(0.9em, 4vw, 1em) !important;
    border: none !important;
    padding: 12px !important;
    width: 100% !important;
    margin-top: 10px !important;
    letter-spacing: 0.5px !important;
}
button.primary:hover { opacity: 0.9 !important; }
.label-wrap {
    background: rgba(255,255,255,0.04) !important;
    border-radius: 12px !important;
    padding: 12px !important;
    border: 1px solid rgba(93,212,240,0.15) !important;
}
footer { display: none !important; }
 
@media (max-width: 600px) {
    .gr-row { flex-direction: column !important; }
    .gr-column { width: 100% !important; min-width: 100% !important; }
}
"""
 
html_content = """
<div class="hero">
  <div class="hero-title">Skin<span>Sense</span></div>
  <div class="hero-sub">AI-анализ меланомы</div>
</div>
<div class="card">
  <div class="card-title">Как правильно сфотографировать?</div>
  <div class="steps-grid">
    <div class="step-item"><div class="step-num">1</div>Протри камеру чистой тканью</div>
    <div class="step-item"><div class="step-num">2</div>Используй дневной свет, без вспышки</div>
    <div class="step-item"><div class="step-num">3</div>Держи камеру в 5–10 см от родинки</div>
    <div class="step-item"><div class="step-num">4</div>Убедись что родинка чётко в фокусе</div>
    <div class="step-item"><div class="step-num">5</div>Центрируй образование в кадре</div>
    <div class="step-item"><div class="step-num">6</div>Не двигай камеру при съёмке</div>
  </div>
  <div class="warning">
    Модель определяет лишь вероятность риска. Результат <b>не является медицинским диагнозом</b>.<br>
    При любых сомнениях — обратитесь к дерматологу.
  </div>
</div>
"""
 
html_awareness = """
<div class="card">
  <div class="awareness-title">Что такое меланома?</div>
  <div class="awareness-grid">
    <div class="awareness-card">
      <div class="awareness-card-title">Статистика</div>
      <div class="awareness-card-text">Меланома занимает 2 место в <b>Казахстане в структуре онкологии</b>. Ранняя диагностика увеличивает выживаемость до <b>98%</b>.</div>
    </div>
    <div class="awareness-card">
      <div class="awareness-card-title">Главные причины</div>
      <div class="awareness-card-text">УФ-излучение от солнца и соляриев — основной фактор риска. Защищай кожу <b>SPF 30+</b> каждый день, даже в облачную погоду.</div>
    </div>
    <div class="awareness-card">
      <div class="awareness-card-title">Кто в зоне риска</div>
      <div class="awareness-card-text">Светлая кожа, много родинок, семейная история меланомы, солнечные ожоги в детстве — всё это повышает риск.</div>
    </div>
    <div class="awareness-card">
      <div class="awareness-card-title">Когда к врачу</div>
      <div class="awareness-card-text">Осматривай кожу раз в два месяца. Если родинка изменилась за <b>4–6 недель</b> — срочно к дерматологу. Не жди!</div>
    </div>
  </div>
  <div class="abcde-box">
    <div class="abcde-title">Правило ABCDE — как самостоятельно оценить родинку</div>
    <div class="abcde-grid">
      <div class="abcde-item">
        <div class="abcde-letter">A</div>
        <div class="abcde-word">Asymmetry</div>
        <div class="abcde-desc">Одна половина не совпадает с другой</div>
      </div>
      <div class="abcde-item">
        <div class="abcde-letter">B</div>
        <div class="abcde-word">Border</div>
        <div class="abcde-desc">Края неровные или размытые</div>
      </div>
      <div class="abcde-item">
        <div class="abcde-letter">C</div>
        <div class="abcde-word">Color</div>
        <div class="abcde-desc">Несколько оттенков в одном образовании</div>
      </div>
      <div class="abcde-item">
        <div class="abcde-letter">D</div>
        <div class="abcde-word">Diameter</div>
        <div class="abcde-desc">Больше 6 мм — размер карандашного ластика</div>
      </div>
      <div class="abcde-item">
        <div class="abcde-letter">E</div>
        <div class="abcde-word">Evolving</div>
        <div class="abcde-desc">Любые изменения формы, цвета, размера</div>
      </div>
    </div>
  </div>
</div>
<div class="footer-text">SkinSense Project · Создано для повышения осведомлённости о меланоме</div>
"""
 
with gr.Blocks(css=css, title="SkinSense") as iface:
    gr.HTML(html_content)
    with gr.Column():
        image_input = gr.Image(type='numpy', label="Загрузи фото родинки")
        submit_btn = gr.Button("Анализировать", variant="primary")
        output = gr.Label(num_top_classes=2, label="Результат анализа")
    submit_btn.click(fn=predict_skin, inputs=image_input, outputs=output)
    gr.HTML(html_awareness)

iface.launch(server_name="0.0.0.0", server_port=7860)
