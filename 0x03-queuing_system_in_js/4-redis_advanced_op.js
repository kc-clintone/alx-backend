#!/usr/bin/yarn dev
import { createClient, print } from 'redis';

const client = createClient();

client.on('error', (error) => {
  console.log('Redis client not connected to the server:', error.toString());
});

const updateHash = (hashName, fieldName, fieldValue) => {
  client.HSET(hashName, fieldName, fieldValue, print);
};

const printHash = (hashName) => {
  client.HGETALL(hashName, (_err, reply) => console.log(reply));
};

function main() {
  const hashObject = {
    'Portland': 50,
    'Seattle': 80,
    'New York': 20,
    'Bogota': 20,
    'Cali': 40,
    'Paris': 2,
  };
  for (const [field, value] of Object.entries(hashObject)) {
    updateHash('HolbertonSchools', field, value);
  }
  printHash('HolbertonSchools');
}

client.on('connect', () => {
  console.log('Redis client connected to the server');
  main();
});
