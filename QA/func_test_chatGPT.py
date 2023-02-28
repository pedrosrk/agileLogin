# 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
import openai

# Define OpenAI API key 
openai.api_key = "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"

# Set up the model and prompt
model_engine = "text-davinci-003"
prompt = "What is the feeling contained in the sentence I love you?"

# Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

response = completion.choices[0].text
print(response)