# 📚 Book Management API

This is a simple Django REST API for managing a collection of books. It includes endpoints for listing, creating, updating, retrieving, and deleting books.

## 🛠️ Project Setup

This project uses Docker for containerization and a Makefile to simplify common commands.

### Prerequisites

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Python 3](https://www.python.org/) (for local virtual environment setup)

## 🚀 Getting Started

Clone the repository and navigate to the project folder:

```bash
git clone https://github.com/RaiTamarindo/book_mgmt.git
cd book_mgmt
```

### 📦 Makefile Commands

| Command           | Description                                           |
| ----------------- | ----------------------------------------------------- |
| `make setup`      | Create a virtual environment and install dependencies |
| `make run`        | Build and start Docker containers                     |
| `make stop`       | Stop and remove Docker containers                     |
| `make logs`       | Tail logs of the running containers                   |
| `make test`       | Run tests (via `docker-compose.test.yml`)             |
| `make clean`      | Remove the virtual environment and Python cache files |
| `make migrations` | Generate database migrations from the models          |

## 🧪 Testing the API

Once the containers are running (`make run`), you can access:

- Django Admin: [http://localhost:8000/admin](http://localhost:8000/admin)
- Books API: [http://localhost:8000/api/books](http://localhost:8000/api/books)

### Example `curl` Commands

📘 **List all books:**

```bash
curl http://localhost:8000/api/books/
```

➕ **Create a new book:**

```bash
curl -X POST http://localhost:8000/api/books/ \
  -H "Content-Type: application/json" \
  -d '{
        "title": "The Pragmatic Programmer",
        "author": "Andy Hunt and Dave Thomas",
        "isbn": "9780135957059",
        "description": "A book about pragmatic approaches to software development.",
        "published_date": "1999-10-20",
        "pages": 352,
        "language": "English"
      }'
```

🔍 **Retrieve a book by ID:**

```bash
curl http://localhost:8000/api/books/1/
```

📝 **Update a book:**

```bash
curl -X PUT http://localhost:8000/api/books/1/ \
  -H "Content-Type: application/json" \
  -d '{
        "title": "The Pragmatic Programmer (Updated)",
        "author": "Andy Hunt and Dave Thomas",
        "isbn": "9780135957059",
        "description": "Updated description.",
        "published_date": "1999-10-20",
        "pages": 360,
        "language": "English"
      }'
```

❌ **Delete a book:**

```bash
curl -X DELETE http://localhost:8000/api/books/1/
```

## 🧱 Project Structure

```
.
├── books/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── services.py
├── manage.py
├── requirements.txt
├── docker-compose.yml
├── Makefile
└── README.md
```

## 🧩 Enrichment

The `create_book_with_enrichment` function is called during creation to automatically enrich book data (e.g., by using external APIs).
