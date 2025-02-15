const express = require('express');
const app = express();
const port = 3000;

app.get('/chat', (req, res) => {
    const query = req.query.query;
    const response = `आपने पूछा: ${query} - और मेरा जवाब है: हां, मैं आपकी मदद कर सकता हूँ!`;
    res.json({ data: response });
});

app.listen(port, () => {
    console.log(`AI API चालू हो गई है: http://localhost:${port}`);
});
