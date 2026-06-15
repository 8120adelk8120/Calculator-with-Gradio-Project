import gradio as gr

def calculator(num1, operation, num2):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        return num1 / num2

demo = gr.Interface(
    fn=calculator,
    inputs=[
        gr.Number(label="Number 1"),
        gr.Radio(["add", "subtract", "multiply", "divide"], label="Operation"),
        gr.Number(label="Number 2")
    ],
    outputs=gr.Number(label="Result"),
    examples=[
        [5, "add", 3],
        [4, "divide", 2],
        [-4, "multiply", 2.5],
        [0, "subtract", 1.2],
    ],
    title="Test Calculator",
    description="Simple Gradio calculator"
)

if __name__ == "__main__":
    demo.launch()