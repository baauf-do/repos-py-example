from fastapi import FastAPI
import gradio as gr  # type: ignore
from app.api.routes import router
from app.services.ollama_chat import call_ollama_chat

app = FastAPI(title='Chatbot API')

app.include_router(router, prefix='/api')


@app.get('/about')
def about_get():
  return {'message': 'Welcome to the Chatbot API!'}


# ✅ Tạo ChatInterface với theme 'huggingface'
# app_ui = gr.ChatInterface(
#     fn=lambda message, history: call_ollama_chat(message, model='llama3'),
#     title='🦙 Chat với Ollama (Dark Mode)',
#     description='Sử dụng Gradio + theme tối.',
#     examples=['Bạn là ai?', 'Trái cam có vị gì?', 'Cay?'],
#     theme='huggingface'  # ✅ Chỉ cần thế này là OK
# )

# 🎨 Giao diện Gradio sử dụng cùng logic với API
with gr.Blocks(theme='soft') as app_ui:
  gr.Markdown("""
    <div align="center">
      <h1>Welcome to the Chatbot! 👋</h1>
    </div>
  """)

  model_dropdown = gr.Dropdown(choices=['llama3.2'], value='llama3.2', label='Chọn mô hình')

  chatbot = gr.Chatbot()
  textbox = gr.Textbox(label='Câu hỏi của bạn', placeholder='Nhập câu hỏi của bạn ở đây...', elem_id='input-textbox')
  # gr.Markdown('---')
  examples = gr.Examples(examples=['Who are you?', 'What is the taste of an orange?', 'Spicy?'], inputs=textbox)
  send_btn = gr.Button('Send', elem_id='send-btn')
  # gr.Markdown('---')

  def on_send(message, history, model_choice):
    response = call_ollama_chat(message, model_choice)
    history.append((message, response))
    return '', history

  send_btn.click(fn=on_send, inputs=[textbox, chatbot, model_dropdown], outputs=[textbox, chatbot])

  # reset_btn = gr.Button('Reset', elem_id='reset-btn')
  # reset_btn.click(fn=lambda: ('', []), inputs=[], outputs=[textbox, chatbot])


# Mount vào FastAPI tại /
gr.mount_gradio_app(app, app_ui, path='/')
