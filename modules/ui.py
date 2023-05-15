import os

import gradio as gr
from modules import reload_web as rd
from modules.device import what_device
from modules.context import Context
# from modules.model import infer
from modules.model import Alpaca
from modules.paper import video_id, contx

css = "style.css"
script_path = "scripts"
_gradio_template_response_orig = gr.routes.templates.TemplateResponse

games = ['Alien', 'Amidar', 'Assault', 'Asterix', 'Boxing', 'Breakout', 'Crazyclimber', 'DemonAttack', 'Attack', 'Gopher', 'Hero', 'Jamesbond', 'Bond', 'Pong', 'Test']
paper_contx = ['Paper', 'Muzero', 'Efficentzero', 'Simsiam', 'MCTS', 'Alpacalora', \
'Pongfig', 'Boxingfig', 'Crazyclimberfig', 'Alienfig', 'Amidarfig', 'Assaultfig', 'Crazyclimberfig']

def predict(ctx, model, query, top_p, top_k, is_instruction, temperature, num_beams, use_stream_chat):
    ctx.limit_round()
    flag = True
    instruction = ""
    if is_instruction:
        instruction = "Output the last word of the text that I input. For example, if my input is 'l want to play Pong', the output is 'Pong'."
    for _, output in model.infer(
            input=query,
            use_stream_chat=use_stream_chat,
            history=ctx.history,
            temperature=temperature,
            top_p=top_p,
            top_k=top_k,
            instruction=instruction,
            num_beams=num_beams,
    ):
        if flag:
            ctx.append(query, output)
            flag = False
        else:
            ctx.update_last(query, output)
        yield ctx.rh, ""
    ctx.refresh_last()
    print(ctx.rh)
    yield ctx.rh, ""

def run_prompt(ctx):
    for dialogues in ctx:
        print(dialogues)
        if dialogues[1] in games:
            # dialogues[1] = f'<video controls="controls" width="800" height="600"><source src="home/szx/rl/efficientzero-demo/{video}" type="video/mp4" />Your browser does not support playing videos.</video>'
            dialogues[1] = video_id(dialogues[1])
            # dialogues[1] = f'<iframe src="home/szx/rl/efficientzero-demo/{video}"  controls="controls" scrolling="yes" border="0" frameborder="no" framespacing="0" allowfullscreen="true" height=800 width=800> </iframe>'
            # ctx[-1].append(f'<video src="/{ctx[0][1]}" style="display: inline-block;">')
        if dialogues[1] in paper_contx:
            dialogues[1] = contx(dialogues[1])
    return ctx

def clear_history(ctx):
    ctx.clear()
    return gr.update(value=[])


def apply_max_round_click(ctx, max_round):
    ctx.max_rounds = max_round
    return f"Applied: max round {ctx.max_rounds}"


def create_ui():
    reload_javascript()
    device = what_device()
    with gr.Blocks(css=css, analytics_enabled=False) as chat_interface:
        Alpaca_lora = Alpaca(device)
        _ctx = Context()
        state = gr.State(_ctx)
        model = gr.State(Alpaca_lora)
        gr.Markdown("""<h1><center>Attention-Efficientzero-Alpaca-LoRa Webui</center></h1>""")
        with gr.Row():
            with gr.Column(scale=7):
                chatbot = gr.Chatbot(elem_id="chat-box", show_label=False).style(height=800)
                with gr.Row():
                    input_message = gr.Textbox(placeholder="(Chinese is not supported, please use ChatGLM 6b)和微调Efficientzero-羊驼对话吧！About Efficientzero...(按 Ctrl+Enter 发送)", show_label=False, lines=4, elem_id="chat-input").style(container=False)
                    clear_input = gr.Button("🗑️", elem_id="del-btn")

                with gr.Row():
                    submit = gr.Button("发送", elem_id="c_generate")

                with gr.Row():
                    revoke_btn = gr.Button("撤回")

            with gr.Column(scale=3):
                with gr.Row():
                    with gr.Column(variant="panel"):
                        with gr.Row():
                            top_p = gr.Slider(minimum=0.01, maximum=1.0, step=0.01, label='Top P', value=0.95)
                        with gr.Row():
                            top_k = gr.Slider(minimum=10.0, maximum=256.0, step=1.0, label='Top k', value=40)
                        with gr.Row():
                            temperature = gr.Slider(minimum=0.0, maximum=1.0, step=0.01, label='Temperature', value=0.75)
                        with gr.Row():
                            num_beams = gr.Slider(minimum=0.0, maximum=8.0, step=2.0, label='num_beams', value=4.0)

                        with gr.Row():
                            max_rounds = gr.Slider(minimum=1, maximum=100, step=1, label="最大对话轮数", value=20)
                            apply_max_rounds = gr.Button("✔", elem_id="del-btn")
                        
                        with gr.Row():
                            is_instruction = gr.Checkbox(label="精准匹配模式", value=False)

                        cmd_output = gr.Textbox(label="控制台输出")
                        with gr.Row():
                            use_stream_chat = gr.Checkbox(label='使用流式输出', value=False)
                with gr.Row():
                    with gr.Column(variant="panel"):
                        with gr.Row():
                            clear_history_btn = gr.Button("清空对话")

                        with gr.Row():
                            sync_his_btn = gr.Button("同步对话")

                        with gr.Row():
                            save_his_btn = gr.Button("保存对话")
                            load_his_btn = gr.UploadButton("读取对话", file_types=['file'], file_count='single')

                        with gr.Row():
                            save_md_btn = gr.Button("保存为 MarkDown")

        submit.click(predict, inputs=[
            state,
            model,
            input_message,
            top_p,
            top_k,
            is_instruction,
            temperature,
            num_beams,
            use_stream_chat
        ], outputs=[
            chatbot,
            input_message
        ]).then(run_prompt, chatbot, chatbot)
        revoke_btn.click(lambda ctx: ctx.revoke(), inputs=[state], outputs=[chatbot])
        clear_history_btn.click(clear_history, inputs=[state], outputs=[chatbot])
        clear_input.click(lambda x: "", inputs=[input_message], outputs=[input_message])
        save_his_btn.click(lambda ctx: ctx.save_history(), inputs=[state], outputs=[cmd_output])
        save_md_btn.click(lambda ctx: ctx.save_as_md(), inputs=[state], outputs=[cmd_output])
        load_his_btn.upload(lambda ctx, f: ctx.load_history(f), inputs=[state, load_his_btn], outputs=[chatbot])
        sync_his_btn.click(lambda ctx: ctx.rh, inputs=[state], outputs=[chatbot])
        apply_max_rounds.click(apply_max_round_click, inputs=[state, max_rounds], outputs=[cmd_output])

    with gr.Blocks(css=css, analytics_enabled=False) as settings_interface:
        with gr.Row():
            reload_ui = gr.Button("Reload UI")

        def restart_ui():
            rd.need_restart = True

        reload_ui.click(restart_ui)

    interfaces = [
        (chat_interface, "Chat", "chat"),
        (settings_interface, "Settings", "settings")
    ]

    with gr.Blocks(css=css, analytics_enabled=False, title="Attention Efficientzero") as demo:
        with gr.Tabs(elem_id="tabs") as tabs:
            for interface, label, ifid in interfaces:
                with gr.TabItem(label, id=ifid, elem_id="tab_" + ifid):
                    interface.render()

    return demo


def reload_javascript():
    scripts_list = [os.path.join(script_path, i) for i in os.listdir(script_path) if i.endswith(".js")]
    javascript = ""
    # with open("script.js", "r", encoding="utf8") as js_file:
    #     javascript = f'<script>{js_file.read()}</script>'

    for path in scripts_list:
        with open(path, "r", encoding="utf8") as js_file:
            javascript += f"\n<script>{js_file.read()}</script>"

    # todo: theme
    # if cmd_opts.theme is not None:
    #     javascript += f"\n<script>set_theme('{cmd_opts.theme}');</script>\n"

    def template_response(*args, **kwargs):
        res = _gradio_template_response_orig(*args, **kwargs)
        res.body = res.body.replace(
            b'</head>', f'{javascript}</head>'.encode("utf8"))
        res.init_headers()
        return res

    gr.routes.templates.TemplateResponse = template_response
