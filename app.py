from flask import Flask, request, jsonify
import logging
from sentence_transformers import SentenceTransformer, util
from waitress import serve
from toml import load
import os

app = Flask(__name__, static_folder=".")

# 语义比较
def calculate_similarity(sentence1, sentence2):
    # 对两个句子进行编码
    embeddings = model_bert.encode([sentence1, sentence2], convert_to_tensor=True)
    # 计算余弦相似度
    similarity = util.pytorch_cos_sim(embeddings[0], embeddings[1])
    return similarity.item()

@app.route('/sentence_similarity', methods=['POST'])
def sentence_similarity():
    data = request.json
    logging.debug(f"Received data: {data}")
    sentence1 = data.get('sentence1', '')
    sentence2 = data.get('sentence2', '')

    if not sentence1 or not sentence2:
        return jsonify({'error': 'Invalid input, sentence and keywords are required'}), 400
    
    similarity = calculate_similarity(sentence1, sentence2)
    return jsonify(similarity)

def main():
    # 配置日志
    logging.basicConfig(level=logging.DEBUG)
    global model_bert
    # 加载预训练的SBERT模型
    # paraphrase-multilingual-MiniLM-L12-v2
    # BERT_PATH='old_models/paraphrase-multilingual-MiniLM-L12-v2/0_Transformer'
    # script_dir = os.path.dirname(os.path.abspath(__file__))
    model_dir = os.path.join(app.static_folder, 'paraphrase-multilingual-MiniLM-L12-v2')
    model_bert = SentenceTransformer(model_dir)
    # model_bert.save_pretrained('./paraphrase-multilingual-MiniLM-L12-v2')
    # model_bert = SentenceTransformer(BERT_PATH)
    logging.info('Model loaded successfully.')
      # 读取toml配置文件
    with open('config.toml', 'r') as f:
        config = load(f)
    
    serve(app, host=config['profile']['host'], port=config['profile']['port'])
    # app.run(host='0.0.0.0', port=11005)

if __name__ == '__main__':
    main()
