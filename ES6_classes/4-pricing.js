import Currency from './3-currency.js';

export default class Pricing {
  constructor(amount, currency) {
    this.amount = amount;
    this.currency = currency;
  }

  get currency() {
    return this._currency;
  }

  set currency(newCurrency) {
    if (!(newCurrency instanceof Currency)) {
      throw new TypeError(`currency must be a currency`);
    }
    this._currency = newCurrency;
  }

  get amount() {
    return this._amount;
  }

  set amount(newAmount) {
    if (typeof newAmount !== 'number') {
      throw new TypeError(`amount must be a string`);
    }
    this._amount = newAmount;
  }

  displayFullPrice() {
    return `${this._amount} ${this._currency.displayFullCurrency()}`;
  }

  static convertPrice(amount, conversionRate) {
    if (typeof conversionRate !== 'number') {
      throw new TypeError(`conversionRate must be a number`);
    }
    if (typeof amount !== 'number') {
      throw new TypeError(`amount must be a number`);
    }
    return amount * conversionRate;
  }
}
