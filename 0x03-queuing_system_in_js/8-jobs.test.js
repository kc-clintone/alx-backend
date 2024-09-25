#!/usr/bin/npm test

import sinon from 'sinon';
import { expect } from 'chai';
import { createQueue } from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  const BIG_TEST = sinon.spy(console);
  const Q = createQueue({ name: 'push_notification_code_test' });

  before(() => {
    Q.testMode.enter(true);
  });

  after(() => {
    Q.testMode.clear();
    Q.testMode.exit();
  });

  afterEach(() => {
    BIG_TEST.log.resetHistory();
  });

  it('displays an error message if jobs is not an array', () => {
    expect(
      createPushNotificationsJobs.bind(createPushNotificationsJobs, {}, Q)
    ).to.throw('Jobs is not an array');
  });

  it('adds jobs to the queue with the correct type', (done) => {
    expect(Q.testMode.jobs.length).to.equal(0);
    const jobInfos = [
      {
        phoneNumber: '44556985789',
        message: 'Use the code 1982 to verify your account',
      },
      {
        phoneNumber: '9887762344',
        message: 'Use the code 1738 to verify your account',
      },
    ];
    createPushNotificationsJobs(jobInfos, Q);
    expect(Q.testMode.jobs.length).to.equal(2);
    expect(Q.testMode.jobs[0].data).to.deep.equal(jobInfos[0]);
    expect(Q.testMode.jobs[0].type).to.equal('push_notification_code_3');
    Q.process('push_notification_code_3', () => {
      expect(
        BIG_TEST.log
          .calledWith('Notification job created:', Q.testMode.jobs[0].id)
      ).to.be.true;
      done();
    });
  });

  it('registers the progress event handler for a job', (done) => {
    Q.testMode.jobs[0].addListener('progress', () => {
      expect(
        BIG_TEST.log
          .calledWith('Notification job', Q.testMode.jobs[0].id, '25% complete')
      ).to.be.true;
      done();
    });
    Q.testMode.jobs[0].emit('progress', 25);
  });

  it('registers the failed event handler for a job', (done) => {
    Q.testMode.jobs[0].addListener('failed', () => {
      expect(
        BIG_TEST.log
          .calledWith('Notification job', Q.testMode.jobs[0].id, 'failed:', 'Failed to send')
      ).to.be.true;
      done();
    });
    Q.testMode.jobs[0].emit('failed', new Error('Failed to send'));
  });

  it('registers the complete event handler for a job', (done) => {
    Q.testMode.jobs[0].addListener('complete', () => {
      expect(
        BIG_TEST.log
          .calledWith('Notification job', Q.testMode.jobs[0].id, 'completed')
      ).to.be.true;
      done();
    });
    Q.testMode.jobs[0].emit('complete');
  });
});
