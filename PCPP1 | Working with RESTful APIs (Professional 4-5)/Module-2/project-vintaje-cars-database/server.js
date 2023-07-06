const express = require('express');
const fs = require('fs');
const bodyParser = require('body-parser');

const app = express();

// Use body-parser middleware to parse JSON request bodies
app.use(bodyParser.json());

// Define a route to get all cars
app.get('/cars', (req, res) => {
  // Read the cars data from the JSON file
  const carsData = JSON.parse(fs.readFileSync('cars.json', 'utf-8'));
  res.json(carsData);
});

// Define a route to add a new car
app.post('/cars', (req, res) => {
  // Read the cars data from the JSON file
  const carsData = JSON.parse(fs.readFileSync('cars.json', 'utf-8'));
  // Add the new car to the cars data
  carsData.push(req.body);
  // Write the updated cars data back to the JSON file
  fs.writeFileSync('cars.json', JSON.stringify(carsData, null, 2));
  res.json(req.body);
});

// Define a route to update an existing car
app.put('/cars/:id', (req, res) => {
  // Read the cars data from the JSON file
  const carsData = JSON.parse(fs.readFileSync('cars.json', 'utf-8'));
  // Find the index of the car with the specified ID
  const index = carsData.findIndex(car => car.id == req.params.id);
  if (index === -1) {
    // If the index is -1, the car was not found
    return res.status(404).json({ message: 'Car not found' });
  }
  // Update the car with the new data
  carsData[index] = req.body;
  // Write the updated cars data back to the JSON file
  fs.writeFileSync('cars.json', JSON.stringify(carsData, null, 2));
  res.json(carsData[index]);
});


// Define a route to delete an existing car
app.delete('/cars/:id', (req, res) => {
  // Read the cars data from the JSON file
  const carsData = JSON.parse(fs.readFileSync('cars.json', 'utf-8'));
  // Find the index of the car with the specified ID
  const index = carsData.findIndex(car => car.id == req.params.id);
  // Remove the car from the cars data
  carsData.splice(index, 1);
  // Write the updated cars data back to the JSON file
  fs.writeFileSync('cars.json', JSON.stringify(carsData, null, 2));
  res.json({ message: 'Car deleted' });
});

// Start the server
app.listen(3000, () => {
  console.log('Server listening on port 3000');
});