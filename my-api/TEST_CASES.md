# API Test Cases

## Test Cases for GET /hello

### TC-G1: GET /hello returns 200

**Covers:** GET-1, GET-2

- **Method:** GET
- **URL:** /hello
- **Expected Status:** 200

---

### TC-G2: GET /hello returns JSON

**Covers:** GET-3

- **Expected:** Content-Type is application/json

---

### TC-G3: GET /hello contains message field

**Covers:** GET-4

- **Expected JSON:** `{ "message": ... }`

---

### TC-G4: GET /hello returns correct greeting

**Covers:** GET-5

- **Expected Response Body:**
  ```json
  { "message": "Hello World!" }
  ```

---

## Test Cases for PUT /hello

### TC-P1: PUT /hello returns 200

**Covers:** PUT-1, PUT-3

- **Method:** PUT
- **Body:** `{ "message": "Hello from PUT!" }`
- **Expected Status:** 200

---

### TC-P2: PUT /hello echoes back updated message

**Covers:** PUT-2, PUT-4, PUT-5, PUT-6

- **Expected Response Body:**
  ```json
  { "updated": "Hello from PUT!" }
  ```

---

### TC-P3: PUT /hello missing message → 400

**Covers:** PUT-7

- **Method:** PUT
- **Body:** `{}` (no message field)
- **Expected Status:** 400
- **Expected Response:** Error message indicating message field is required
