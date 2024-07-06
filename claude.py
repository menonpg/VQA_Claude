import os
import time
import base64
import requests
import fitz
from client import Client

class Chat:
    def __init__(self):
        self.client = None

    def run(self, api_key=None, model=None, prompt=None, system_prompt=None, max_tokens=None, stop_sequences=None, stream=None, temperature=None, top_p=None, top_k=None):

        self.client = Client(api_key=api_key)
        self.model = model if model else self.client.config.get('model')
        self.max_tokens = max_tokens if max_tokens else 1024

        conversation_history = []

        print("Assistant: Hello! How can I assist you today?")
        while True:
            if prompt:
                user_input = prompt.strip()
                print(f"User: {user_input}")
                prompt = None
            else:
                user_input = input("User: ").strip()
                if user_input.lower() in ['exit', 'quit']:
                    print("\nThank you for using the Claude AI toolkit. Have a great day!")
                    break

                if not user_input:
                    print("Invalid input detected. Please enter a valid message.")
                    continue

            conversation_history.append({"role": "user", "content": user_input})

            data = {
                "messages": conversation_history,
                "model": self.model,
                "system_prompt": system_prompt,
                "max_tokens": self.max_tokens,
                "stop_sequences": stop_sequences,
                "stream": stream,
                "temperature": temperature,
                "top_p": top_p,
                "top_k": top_k
            }
            data = {k: v for k, v in data.items() if v is not None}

            endpoint = self.client.config.get('messages_endpoint')

            if stream:
                response = self.client.stream_post(endpoint, data)
                assistant_response = response
            else:
                response = self.client.post(endpoint, data)
                assistant_response = response
                print(f"Assistant: {assistant_response}")
            conversation_history.append({"role": "assistant", "content": assistant_response})

class Text:
    def __init__(self):
        self.client = None

    def run(self, api_key=None, model=None, prompt=None, system_prompt=None, max_tokens=None, stop_sequences=None, stream=None, temperature=None, top_p=None, top_k=None):

        self.client = Client(api_key=api_key)
        self.model = model if model else self.client.config.get('model')
        self.max_tokens = max_tokens if max_tokens else 1024

        if not prompt:
            return "Error: { Invalid input detected }. Please enter a valid message."

        data = {
            "messages": [{"role": "user", "content": prompt}],
            "model": self.model,
            "system_prompt": system_prompt,
            "max_tokens": self.max_tokens,
            "stop_sequences": stop_sequences,
            "stream": stream,
            "temperature": temperature,
            "top_p": top_p,
            "top_k": top_k
        }
        data = {k: v for k, v in data.items() if v is not None}

        endpoint = self.client.config.get('messages_endpoint')

        if stream:
            response = self.client.stream_post(endpoint, data)
            assistant_response = response
        else:
            response = self.client.post(endpoint, data)
            assistant_response = response
        return assistant_response

class Vision:
    def __init__(self):
        self.client = None
        self.directory_path = os.path.dirname(__file__)
        self.upload_folder_path = os.path.join(self.directory_path, 'uploads')
        os.makedirs(self.upload_folder_path, exist_ok=True)

    def process_image_input(self, image_file, session_id):
        if image_file:
            session_path = os.path.join(self.upload_folder_path, session_id)
            os.makedirs(session_path, exist_ok=True)
            extension = self.get_mime_type(image_file.name)
            if extension is None:
                return None, "Unsupported image format. Please use a .jpg, .jpeg, .png, .webp, or .gif image file."
            filename = f"{str(time.time())}.{extension}"
            image_path = os.path.join(session_path, filename)
            with open(image_path, 'wb') as f:
                f.write(image_file.read())
            return image_path, None
        else:
            return None, "No image file provided."

    def process_pdf_input(self, pdf_file, session_id):
        if pdf_file:
            session_path = os.path.join(self.upload_folder_path, session_id)
            os.makedirs(session_path, exist_ok=True)
            extension = self.get_mime_type(pdf_file.name)
            if extension != "pdf":
                return None, "Unsupported file format. Please use a .pdf file."
            filename = f"{str(time.time())}.pdf"
            pdf_path = os.path.join(session_path, filename)
            with open(pdf_path, 'wb') as f:
                f.write(pdf_file.read())

            images = self.pdf_to_images(pdf_path, session_path)
            return images, None
        else:
            return None, "No PDF file provided."

    def pdf_to_images(self, pdf_path, output_folder):
        doc = fitz.open(pdf_path)
        image_paths = []
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            pix = page.get_pixmap()
            image_path = os.path.join(output_folder, f"page_{page_num + 1}.png")
            pix.save(image_path)
            image_paths.append(image_path)
        return image_paths

    def image_to_base64(self, image_path):
        try:
            with open(image_path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode('utf-8'), None
        except Exception as e:
            return None, f"Failed to convert the image to base64. Error: {e}"

    def get_mime_type(self, filename):
        if filename.lower().endswith(".jpg") or filename.lower().endswith(".jpeg"):
            return "jpeg"
        elif filename.lower().endswith(".png"):
            return "png"
        elif filename.lower().endswith(".webp"):
            return "webp"
        elif filename.lower().endswith(".gif"):
            return "gif"
        elif filename.lower().endswith(".pdf"):
            return "pdf"
        else:
            return None

    def run(self, api_key=None, model=None, prompt=None, image=None, system_prompt=None, max_tokens=None, stop_sequences=None, stream=None, temperature=None, top_p=None, top_k=None, session_id=None):

        self.client = Client(api_key=api_key)
        self.model = model if model else self.client.config.get('model')
        self.max_tokens = max_tokens if max_tokens else 1024

        if image:
            mime_type = self.get_mime_type(image.name)
            if mime_type == "pdf":
                images, error = self.process_pdf_input(image, session_id)
                if error:
                    return error
                vision_prompt = []
                assistant_responses = []
                for img_path in images:
                    image_base64, error = self.image_to_base64(img_path)
                    if error:
                        return error
                    vision_prompt.append(
                        {
                            "role": "user", 
                            "content": [
                                {
                                    "type": "image",
                                    "source": {
                                        "type": "base64",
                                        "media_type": "image/png",
                                        "data": image_base64,
                                    }
                                },
                                {
                                    "type": "text", 
                                    "text": prompt
                                }
                            ]
                        }
                    )
                    data = {
                        "messages": vision_prompt,
                        "model": self.model,
                        "system_prompt": system_prompt,
                        "max_tokens": self.max_tokens,
                        "stop_sequences": stop_sequences,
                        "stream": stream,
                        "temperature": temperature,
                        "top_p": top_p,
                        "top_k": top_k
                    }
                    data = {k: v for k, v in data.items() if v is not None}
                    endpoint = self.client.config.get('messages_endpoint')
                    if stream:
                        response = self.client.stream_post(endpoint, data)
                    else:
                        response = self.client.post(endpoint, data)
                    assistant_responses.append(response)
                    vision_prompt.append({"role": "assistant", "content": response})
                assistant_response = "\n".join(assistant_responses)
            else:
                image_path, error = self.process_image_input(image, session_id)
                if error:
                    return error
                image_base64, error = self.image_to_base64(image_path)
                if error:
                    return error
                mime_type = self.get_mime_type(image_path)
                if mime_type is None:
                    return "Unsupported image format. Please use a .jpg, .jpeg, .png, .webp, or .gif image file."

                vision_prompt = [
                    {
                        "role": "user", 
                        "content": [
                            {
                                "type": "image",
                                "source": {
                                    "type": "base64",
                                    "media_type": f"image/{mime_type}",
                                    "data": image_base64,
                                }
                            },
                            {
                                "type": "text", 
                                "text": prompt
                            }
                        ]
                    }
                ]

                data = {
                    "messages": vision_prompt,
                    "model": self.model,
                    "system_prompt": system_prompt,
                    "max_tokens": self.max_tokens,
                    "stop_sequences": stop_sequences,
                    "stream": stream,
                    "temperature": temperature,
                    "top_p": top_p,
                    "top_k": top_k
                }
                data = {k: v for k, v in data.items() if v is not None}
                endpoint = self.client.config.get('messages_endpoint')
                if stream:
                    assistant_response = self.client.stream_post(endpoint, data)
                else:
                    assistant_response = self.client.post(endpoint, data)

        else:
            return "Error: Image input is required."

        return assistant_response