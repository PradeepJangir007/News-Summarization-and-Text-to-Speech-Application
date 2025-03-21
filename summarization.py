import ast
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForCausalLM
class ArticleComparer:
    def __init__(self, model_name="TinyLlama/TinyLlama-1.1B-Chat-v1.0"):
        self.model_name = model_name
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(self.model_name)
        self.model_pipeline = pipeline("text-generation",
                                      model=self.model,
                                      tokenizer=self.tokenizer,
                                      device_map="auto",
                                      )

    def compare_articles(self, news_data):
        articles = [article['summary'] for article in news_data["articles"]]
        results = []

        for i in range(0, len(articles), 2):
            if i + 1 >= len(articles):
                break  # Avoid index error for odd number of articles

            article1 = articles[i]
            article2 = articles[i + 1]

            # Get the model's response
            response = self.model_pipeline(f'''
                Compare the two news articles provided below and generate a structured JSON output.

                Article {i+1}:
                {article1}

                Article {i+2}:
                {article2}

                Output Format:
                {{
                    "Coverage Differences": [
                        {{
                            "Comparison": "Summarize the key difference in focus between the two articles.",
                            "Impact": "Explain how each article influences public perception differently."
                        }}
                    ]
                }}
            ''')[0]

            try:
                new_data = response['generated_text'][response['generated_text'].rfind("Coverage Differences"):]
                parsed_response = ast.literal_eval(new_data[new_data.index('{'):new_data.index('}')+1])
                results.append(parsed_response)
                print(parsed_response)
            except Exception as e:
                print(f"Error parsing model output: {e}")
                continue

        news_data["Comparative Sentiment Score"]["Coverage Differences"] = results
        return news_data

    def get_final_summary(self, news_data):
        articles_text = "\n\n".join([f" {article['summary']}" for article in news_data['articles']])

        response = self.model_pipeline(f"""
                                          Analyze the sentiment of the following news articles and provide a final summary of the overall sentiment.

                                          Articles:
                                          {articles_text}

                                          Extract and structure the output as follows:
                                          {{
                                              "Final Sentiment Analysis": "Summarize in one line whether the overall news coverage is positive, neutral, or negative.
                                              Mention any potential impact on the company's stock, public perception, or business operations."
                                          }}

                                          Ensure the output is in valid JSON format.
                                          """)[0]

        try:
            new=response['generated_text'][response['generated_text'].rfind("Final Sentiment Analysis"):]
            final_summary = str(new[len("Final Sentiment Analysis :"):new.find('.')]).replace('"',"")
            news_data["Final Sentiment Analysis"] = final_summary
        except Exception as e:
            print(f"Error parsing final summary output: {e}")
            news_data["Final Sentiment Analysis"] = "Error generating final summary."

        return news_data
