#!/usr/bin/yarn dev
import { createQueue } from 'kue';

const jobs = [
  {
    phoneNumber: '4153518544',
    message: 'This is the code 1877 to verify your account',
  },
  {
    phoneNumber: '4153518900',
    message: 'This is the code 4589 to verify your account',
  },
  {
    phoneNumber: '4153518345',
    message: 'This is the code 4309 to verify your account',
  },
  {
    phoneNumber: '4153538444',
    message: 'This is the code 4567 to verify your account',
  },
  {
    phoneNumber: '4153118098',
    message: 'This is the code 4344 to verify your account',
  },
  {
    phoneNumber: '4153718000',
    message: 'This is the code 4578 to verify your account',
  },
  {
    phoneNumber: '4159518654',
    message: 'This is the code 4300 to verify your account',
  },
  {
    phoneNumber: '4158718876',
    message: 'This is the code 4555 to verify your account',
  },
  {
    phoneNumber: '4153818890',
    message: 'This is the code 4344 to verify your account',
  },
  {
    phoneNumber: '4154318543',
    message: 'This is the code 4598 to verify your account',
  },
  {
    phoneNumber: '4151218789',
    message: 'This is the code 4301 to verify your account',
  },
];

const queue = createQueue({ name: 'push_notification_code_2' });

for (const jobInfo of jobs) {
  const job = queue.create('push_notification_code_2', jobInfo);

  job
    .on('enqueue', () => {
      console.log('Notification job created:', job.id);
    })
    .on('complete', () => {
      console.log('Notification job', job.id, 'completed');
    })
    .on('failed', (error) => {
      console.log('Notification job', job.id, 'failed:', error.message || error.toString());
    })
    .on('progress', (progress, _data) => {
      console.log('Notification job', job.id, `${progress}% complete`);
    });
  job.save();
}
