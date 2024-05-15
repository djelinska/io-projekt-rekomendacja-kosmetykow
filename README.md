# Aplikacja Rekomendacji Kosmetyków

## Opis

Aplikacja Rekomendacji Kosmetyków to narzędzie, które umożliwia przeglądanie dostępnych produktów oraz otrzymywanie rekomendacji dla konkretnych produktów za pomocą modelu KNN (k-nearest neighbors).

### Jak to działa?

1. **Analiza Cech**: Model KNN analizuje cechy produktów, takie jak oceny użytkowników, aby stwierdzić, jak bardzo są one do siebie podobne.
2. **Wybór Produktu**: Użytkownik wybiera produkt, dla którego chce otrzymać rekomendacje.
3. **Rekomendacje**: Na podstawie wybranego produktu, model KNN sugeruje podobne produkty, które mogą zainteresować użytkownika.

### Dlaczego to jest użyteczne?

- Pomaga użytkownikom znaleźć nowe produkty, które mogą ich zainteresować, na podstawie ich preferencji.
- Ułatwia eksplorację asortymentu produktów i zwiększa zaangażowanie użytkowników w aplikację.

## Instalacja

1. Sklonuj repozytorium na swój lokalny komputer.
2. Zainstaluj wymagane biblioteki Pythona, uruchamiając `pip install -r requirements.txt`.
3. Uruchom serwer Flask, wykonując `python app.py`.
4. Otwórz nowe okno terminala i przejdź do katalogu zawierającego frontend (np. katalog zawierający plik `package.json`).
5. Zainstaluj wszystkie zależności frontendowe, uruchamiając `npm install`.
6. Uruchom serwer deweloperski React, wykonując `npm start`.
7. Przejdź w przeglądarce na adres `http://localhost:3000`, aby zobaczyć działającą aplikację React.

## Instrukcja Użytkowania

1. **Przeglądanie Produktów**: Wejdź na stronę główną aplikacji, aby zobaczyć wszystkie dostępne produkty. Możesz przewijać stronę w dół, aby zobaczyć więcej produktów.

2. **Rekomendacje**: Kliknij w przycisk pod wybranym produktem, aby zobaczyć produkty rekomendowane przez model KNN na podstawie tego produktu.

## Technologie

- Frontend: React, HTML, CSS, JavaScript
- Backend: Python, Flask
- Baza Danych: [Wstaw tutaj nazwę bazy danych, jeśli używasz]
- Model KNN: Python, biblioteki do uczenia maszynowego (scikit-learn)

## Źródła

- Zbiór danych Sephora na Kaggle: [link](https://www.kaggle.com/datasets/nadyinky/sephora-products-and-skincare-reviews)
- Poradnik dotyczący implementacji systemu rekomendacji przy użyciu algorytmu k-najbliższych sąsiadów (KNN): [link](https://youtu.be/kccT0FVK6OY?si=b0O_2qkBPa-xRqkX)
- Przykład implementacji algorytmu k-najbliższych sąsiadów (KNN): [link](https://github.com/jisilvia/kNN_Recommender_System/blob/main/kNN_Recommender_System.ipynb)
- ChatGPT
