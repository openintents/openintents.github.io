---
title: Record a New Financial Transaction
action: com.funkyandroid.action.NEW_TRANSACTION
extras:
  -
    name: com.funkyandroid.CATEGORY
    type: String
    description: A String holding the category of an item. This should be a textual representation and not an id (e.g. Hotel expenses).
  -
    name: com.funkyandroid.DATE
    type: long
    description: Date in milliseconds from EPOC, A long value holding the date in milliseconds from the epoc as returned by System.currentTimeMillis(), (new Date()).getTime(), or Calendar.getInstance().getTimeInMillis().
  -
    name: com.funkyandroid.AMOUNT
    type: String
    description: Monetary amount, a textual representation of an amount without a currency symbol (e.g. "123.45"). The currency symbol is not included because only the receiving intent is aware of currencies it supports.
  -
    name: com.funkyandroid.PAYEE
    type: String
    description: Payee for financial transaction

---
This intent reports a financial transaction to be recorded in an expenses or banking application.

This is used, for example, by BistroMath to report the amount it has calculated for a persons tip to Funky Expenses for recording in the persons expenses account.

It is recommended that the intent brings up a page which allows the user to confirm the transaction 
before it is recorded in order to prevent malicious applications filling an expenses/banking application with junk entries and to allow the user to fill in any missing information.
