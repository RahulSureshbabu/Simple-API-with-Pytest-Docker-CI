const express = require("express");
const swaggerUi = require("swagger-ui-express");
const swaggerJsdoc = require("swagger-jsdoc");

const app = express();
app.use(express.json());

// Swagger setup
const options = {
  definition: {
    openapi: "3.0.0",
    info: {
      title: "Simple API",
      version: "1.0.0",
    },
  },
  apis: ["index.js"],
};

const swaggerSpec = swaggerJsdoc(options);
app.use("/api-docs", swaggerUi.serve, swaggerUi.setup(swaggerSpec));

/**
 * @openapi
 * /hello:
 *   get:
 *     description: Returns a simple greeting.
 *     responses:
 *       200:
 *         description: Greeting message.
 */
app.get("/hello", (req, res) => {
  res.json({ message: "Hello World!" });
});
/**
 * @openapi
 * /hello:
 *   put:
 *     description: Updates the greeting message.
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             properties:
 *               message:
 *                 type: string
 *                 example: "Hello from PUT!"
 *             required:
 *               - message
 *     responses:
 *       200:
 *         description: Updated greeting.
 *       400:
 *         description: Bad request - message is required.
 */
app.put("/hello", (req, res) => {
  const { message } = req.body;
  if (!message || typeof message !== 'string') {
    return res.status(400).json({ error: "Message is required and must be a string" });
  }
  res.json({ updated: message });
});

app.listen(3000, () => console.log("Server running at http://localhost:3000/api-docs"));
