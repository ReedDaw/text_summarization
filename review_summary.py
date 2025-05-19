from openai import OpenAI

client = OpenAI(api_key="api_key")
import pandas as pd

# Function to generate a summary and insights using the new chat-based GPT API
def generate_insights(review):
    # Define the prompt for generating the summary and insights
    prompt = f"""
    Review: {review}
    
    Provide a concise summary of the review. Additionally, extract and list any important insights from the review that might be useful for a professional or customer:
    1. Summary:
    2. Insights:
    """

    # Make the API call to OpenAI's new chat-based API
    response = client.chat.completions.create(model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.7,
    max_tokens=500,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0)

    # Extract the generated text from the response
    generated_text = response.choices[0].message.content.strip()

    return generated_text

# Read the input CSV file containing reviews
input_file = '/Users/reeddaw/text_summarization/reviews_input.csv'  # Change this to the actual file path
df = pd.read_csv(input_file)

# Create an empty list to store the results
results = []

# Process each review and generate insights
for index, row in df.iterrows():
    review = row['review_content']
    url = row['URL']

    # Generate the summary and insights
    generated_text = generate_insights(review)

    # Append the result to the list with the URL
    results.append({
        'URL': url,
        'review_content': review,
        'summary_insights': generated_text
    })

# Convert the results list to a DataFrame
output_df = pd.DataFrame(results)

# Save the output DataFrame to a CSV file
output_file = '/Users/reeddaw/text_summarization/reviews_output.csv'  # Change this to the desired output file path
output_df.to_csv(output_file, index=False)

print(f"Summaries and insights have been successfully saved to {output_file}")

