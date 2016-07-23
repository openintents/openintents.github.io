---
title: Request payment
action: org.openintents.action.REQUEST_PAYMENT
extras:
  -
    name: org.openintents.extra.AMOUNT
    type: int
    var: amount
    description: amount the use would like to receive
out:
  extras:
    -
      name: org.openintents.extra.STATE
      type: String
      var: state
      description: descriptive value about the state of the payment request, i.e. one of REQUESTED, IN_PROGRESS, AMOUNT_RECEIVED.
---
Request a payment. The user would like to initate a request for payment by another user. 
This could be e.g. a merchant asking another user to pay for goods or services.

Applications can use `startActivityForResult()` to launch this request to get information about the state of the payment request.

