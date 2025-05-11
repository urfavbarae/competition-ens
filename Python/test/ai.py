"""import openai
import requests

# Replace 'your_api_key' with your actual OpenAI API key
api_key = 'your_api_key'

def generate_image_from_text(text):
    openai.api_key = api_key

    prompt = f"Generate an image of {text}"
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
    )

    image_url = response.choices[0].text.strip()
    return image_url

if __name__ == "__main__":
    text = "a serene mountain landscape"
    image_url = generate_image_from_text(text)

    if image_url:
        response = requests.get(image_url)
        with open(f"{text.replace(' ', '_')}.png", "wb") as f:
            f.write(response.content)
        print(f"Image generated and saved as '{text.replace(' ', '_')}.png'")
    else:
        print("Image generation failed.")"""
