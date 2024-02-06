#!/usr/bin/node
/**
 * Connect to redis server via redis client
 */

import { createClient } from 'redis';

const client = await createClient()
  .on('error', err => console.log('Redis client not connected to the server: ERROR_MESSAGE', err))
  .on('connect', () => {
	  console.log('Redis client connected to the server');
	});
