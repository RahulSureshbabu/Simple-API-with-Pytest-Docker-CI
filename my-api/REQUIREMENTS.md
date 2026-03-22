# API Functional Requirements

## 1. Endpoint: GET /hello

**Description:** Returns a simple greeting message.

### Functional Requirements

| ID | Requirement |
|---|---|
| GET-1 | The endpoint MUST respond to GET requests at /hello. |
| GET-2 | The response MUST have HTTP status code 200 OK. |
| GET-3 | The response MUST be a JSON object. |
| GET-4 | The response MUST contain the field "message". |
| GET-5 | The message MUST equal "Hello World!". |

---

## 2. Endpoint: PUT /hello

**Description:** Updates the greeting message.

### Functional Requirements

| ID | Requirement |
|---|---|
| PUT-1 | The endpoint MUST accept PUT requests at /hello. |
| PUT-2 | The endpoint MUST require a JSON body with a "message" field. |
| PUT-3 | The response MUST have HTTP status code 200 OK. |
| PUT-4 | The response MUST be a JSON object. |
| PUT-5 | The response MUST contain the field "updated". |
| PUT-6 | The value of "updated" MUST equal the "message" sent in the request. |
| PUT-7 | If no "message" field is provided, return 400 Bad Request (this is not implemented, but SHOULD be). |
