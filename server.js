const express = require('express');
const cors = require('cors');
const app = express();

app.use(cors());

const prices = {
    "1": [{ "dealer": "Alex Motors", "price": "$28,000" }, { "dealer": "Delta Cars", "price": "$27,500" }],
    "2": [{ "dealer": "City Auto", "price": "$31,000" }],
    "3": [{ "dealer": "Desert Road", "price": "$45,000" }]
};

app.get('/dealer_pricing/:id', (req, res) => {
    const id = req.params.id;
    res.json(prices[id] || []);
});

app.listen(3000, () => console.log('Pricing service running on port 3000'));
