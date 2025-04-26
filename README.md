# AI-Powered Code Generator Application

Bu proje, S4E DevOps staj programı için geliştirilmiş yapay zeka destekli bir kod üretici uygulamasıdır.

## Özellikler

- Flask tabanlı web arayüzü
- Ollama ile yerel LLM entegrasyonu
- Python kodu üretme ve başlık oluşturma
- Modern ve responsive tasarım
- Kubernetes ve Helm ile container orkestrasyonu

## Kurulum

### Gereksinimler

- Python 3.11+
- Docker
- Kubernetes (Minikube)
- Helm
- Ollama (yerel LLM için)

### Yerel Geliştirme

1. Sanal ortam oluşturun:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. Bağımlılıkları yükleyin:
```bash
pip install -r requirements.txt
```

3. Ollama'yı başlatın:
```bash
ollama serve
```

4. Uygulamayı çalıştırın:
```bash
python app.py
```

### Docker ile Çalıştırma

1. Docker imajını oluşturun:
```bash
docker build -t eshbah/ai-powered-code-generator-application:latest .
```

2. Container'ı çalıştırın:
```bash
docker run -p 5000:5000 eshbah/ai-powered-code-generator-application:latest
```

### Kubernetes ile Dağıtım

1. Helm chart'ı yükleyin:
```bash
helm install ai-code ./ai-code-chart --namespace default --create-namespace
```

2. Uygulamaya erişin:
```
http://localhost:30081
```

## Kullanım

1. Web arayüzüne gidin
2. İstediğiniz kodu açıklayan bir prompt girin
3. "Generate Code" butonuna tıklayın
4. Üretilen kodu kopyalayın ve kullanın
