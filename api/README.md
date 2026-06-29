# Simple Math API — homework.py

A minimal HTTP API server built with Python's standard library. It accepts two integers as query parameters and returns the result of a math operation in JSON.

No frameworks, no installs — just Python.

---

## How to Run

```bash
python3 homework.py
```

The server starts on `http://localhost:5000` and keeps running until you stop it with `Ctrl + C`.

**Requirements:** Python 3.8 or newer. No external packages needed.

---

## Endpoints

All endpoints use `GET` and accept two query parameters: `a` and `b` (both integers).

### `GET /add`

```
http://localhost:5000/add?a=5&b=3
```

```json
{
  "a": 5,
  "b": 3,
  "operation": "addition",
  "result": 8
}
```

---

### `GET /subtract`

```
http://localhost:5000/subtract?a=10&b=4
```

```json
{
  "a": 10,
  "b": 4,
  "operation": "subtraction",
  "result": 6
}
```

---

### `GET /multiply`

```
http://localhost:5000/multiply?a=6&b=7
```

```json
{
  "a": 6,
  "b": 7,
  "operation": "multiplication",
  "result": 42
}
```

---

## Error Responses

**Missing or non-integer parameters — 400 Bad Request**

```
http://localhost:5000/add?a=hello&b=3
```

```json
{
  "error": "a and b must be integers"
}
```

**Unknown endpoint — 404 Not Found**

```
http://localhost:5000/divide?a=10&b=2
```

```json
{
  "error": "Operation not found"
}
```

---

## Testing with curl

```bash
curl "http://localhost:5000/add?a=10&b=5"
curl "http://localhost:5000/subtract?a=10&b=5"
curl "http://localhost:5000/multiply?a=10&b=5"
```

Or paste the URLs directly into your browser.

